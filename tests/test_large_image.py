import requests
import os

def test_large_image():
    url = "http://localhost:8000/api/chat"
    
    # Create a dummy large base64 string (approx 2MB)
    # Base64 uses 4 chars per 3 bytes. 2MB = ~2.6M chars.
    large_base64 = "A" * (2 * 1024 * 1024)
    
    payload = {
        "message": "What is this?",
        "image": large_base64
    }
    
    print(f"Sending payload with image size: {len(large_base64)} chars")
    
    try:
        response = requests.post(url, json=payload)
        print(f"Status Code: {response.status_code}")
        # Print only first 100 chars of response to avoid spam
        print(f"Response: {str(response.json())[:100]}...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_large_image()
