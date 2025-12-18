import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from api.core.config import settings

def ingest_docs():
    print(f"Loading documents from {settings.DATA_DIR}...")
    loader = DirectoryLoader(settings.DATA_DIR, glob="**/*.txt", loader_cls=TextLoader)
    docs = loader.load()
    
    if not docs:
        print("No documents found.")
        return

    print(f"Loaded {len(docs)} documents.")
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    print(f"Split into {len(splits)} chunks.")

    print("Creating vector store...")
    # Initialize embeddings
    if not settings.OPENAI_API_KEY:
        print("Error: OPENAI_API_KEY not set.")
        return

    embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
    
    # Create and persist FAISS vector store
    vectorstore = FAISS.from_documents(
        documents=splits,
        embedding=embeddings
    )
    vectorstore.save_local(settings.CHROMA_DB_DIR)
    print(f"Vector store created at {settings.CHROMA_DB_DIR}")

if __name__ == "__main__":
    ingest_docs()
