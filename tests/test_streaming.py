import requests
import json

def test_streaming():
    url = "http://localhost:8000/api/chat/stream"
    
    payload = {
        "message": "Tell me a short joke."
    }
    
    print("Sending request...")
    try:
        with requests.post(url, json=payload, stream=True) as r:
            r.raise_for_status()
            print("Response stream started:")
            for chunk in r.iter_content(chunk_size=None):
                if chunk:
                    print(chunk.decode('utf-8'), end='', flush=True)
            print("\nStream finished.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_streaming()
