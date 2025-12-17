from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.messages import HumanMessage
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools.retriever import create_retriever_tool
from langchain_core.tools import tool
import numexpr
from app.core.config import settings

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

from app.services.tools import create_ticket, send_email, schedule_meeting

@tool
def calculator(expression: str) -> str:
    """Calculate the result of a mathematical expression."""
    try:
        return str(numexpr.evaluate(expression))
    except Exception as e:
        return f"Error calculating: {e}"

class RAGService:
    def __init__(self):
        if not settings.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")
            
        self.embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
        self.vectorstore = Chroma(
            persist_directory=settings.CHROMA_DB_DIR, 
            embedding_function=self.embeddings
        )
        self.retriever = self.vectorstore.as_retriever()
        self.llm = ChatOpenAI(model="gpt-4o", openai_api_key=settings.OPENAI_API_KEY)

        # Define Tools
        self.retriever_tool = create_retriever_tool(
            self.retriever,
            "search_knowledge_base",
            "Searches and returns documents regarding company policies and information."
        )
        
        self.tools = [self.retriever_tool, calculator, create_ticket, send_email, schedule_meeting]

        # Define Agent
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are OmniAssist, a helpful enterprise AI assistant. You can answer questions based on the provided context, use tools, and analyze images provided by the user. If you don't know, say so."),
            ("placeholder", "{chat_history}"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ])

        self.agent = create_tool_calling_agent(self.llm, self.tools, self.prompt)
        self.agent_executor = AgentExecutor(agent=self.agent, tools=self.tools, verbose=True)
        
        # Simple in-memory history (global for now)
        self.chat_history = ChatMessageHistory()

    def chat(self, query: str, image_base64: str = None):
        print(f"Received query: {query}")
        print(f"Image present: {bool(image_base64)}")
        
        content = [{"type": "text", "text": query}]
        if image_base64:
            content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image_base64}"
                }
            })
        
        print(f"Invoking agent with content: {content}")
            
        # Invoke agent with history
        response = self.agent_executor.invoke({
            "input": content,
            "chat_history": self.chat_history.messages
        })
        
        output = response["output"]
        
        # Update history
        # Note: We store the raw query text, not the complex content list, for history readability if possible,
        # but for the agent to work correctly with images in history, we might need to be careful.
        # LangChain's ChatMessageHistory handles strings or messages.
        # For simplicity, we'll add the user message as the complex content or just text if no image.
        
        if image_base64:
             self.chat_history.add_user_message(HumanMessage(content=content))
        else:
             self.chat_history.add_user_message(query)
             
        self.chat_history.add_ai_message(output)
        
        return output

    async def astream_chat(self, query: str, image_base64: str = None):
        """
        Async generator that yields chunks of the response.
        """
        content = [{"type": "text", "text": query}]
        if image_base64:
            content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image_base64}"
                }
            })
            
        # Update history (User)
        if image_base64:
             self.chat_history.add_user_message(HumanMessage(content=content))
        else:
             self.chat_history.add_user_message(query)

        # We will collect the final answer to update history (AI)
        final_answer = ""
        
        # Use astream_events to get token-level streaming
        # We filter for 'on_chat_model_stream' events from the 'agent' (not tools)
        async for event in self.agent_executor.astream_events(
            {
                "input": content,
                "chat_history": self.chat_history.messages
            },
            version="v2"
        ):
            kind = event["event"]
            
            # Stream tokens from the LLM
            if kind == "on_chat_model_stream":
                chunk = event["data"]["chunk"]
                if chunk.content:
                    # We yield the content directly
                    yield chunk.content
                    final_answer += chunk.content
                    
        # Update history (AI)
        self.chat_history.add_ai_message(final_answer)

rag_service = RAGService()
