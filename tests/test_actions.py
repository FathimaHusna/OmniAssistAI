import requests

def test_actions():
    url = "http://localhost:8000/api/chat"
    
    # 1. Test Ticketing
    print("\n--- Test 1: Create Ticket ---")
    payload1 = {
        "message": "Please create a high priority ticket for a server outage."
    }
    try:
        response1 = requests.post(url, json=payload1)
        print(f"Response: {response1.json()['response']}")
    except Exception as e:
        print(f"Error: {e}")

    # 2. Test Email
    print("\n--- Test 2: Send Email ---")
    payload2 = {
        "message": "Send an email to admin@example.com saying the system is down."
    }
    try:
        response2 = requests.post(url, json=payload2)
        print(f"Response: {response2.json()['response']}")
    except Exception as e:
        print(f"Error: {e}")

    # 3. Test Calendar
    print("\n--- Test 3: Schedule Meeting ---")
    payload3 = {
        "message": "Schedule a meeting with the team tomorrow at 2pm to discuss the outage."
    }
    try:
        response3 = requests.post(url, json=payload3)
        print(f"Response: {response3.json()['response']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_actions()
