import requests

def test_invalid_image():
    url = "http://localhost:8000/api/chat"
    
    payload = {
        "message": "What is this?",
        "image": "NOT_A_VALID_BASE64_STRING"
    }
    
    try:
        response = requests.post(url, json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_invalid_image()
