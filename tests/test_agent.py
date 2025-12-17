import sys
import os

# Add app to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.rag_service import rag_service

def test_agent():
    print("Testing Calculator Tool...")
    math_query = "What is 123 * 45?"
    response = rag_service.chat(math_query)
    print(f"Query: {math_query}")
    print(f"Response: {response}")
    
    if "5535" in response:
        print("✅ Calculator Test Passed")
    else:
        print("❌ Calculator Test Failed")

    print("\nTesting Retriever Tool...")
    # Assuming some policy data exists. If not, this might fail or return "I don't know".
    # I'll check for a generic response or if it tries to search.
    policy_query = "What is the policy on remote work?"
    response = rag_service.chat(policy_query)
    print(f"Query: {policy_query}")
    print(f"Response: {response}")
    
    # We can't strictly assert content without knowing the DB, but we can check if it didn't crash.
    print("✅ Retriever Test Completed (Check output)")

if __name__ == "__main__":
    test_agent()
