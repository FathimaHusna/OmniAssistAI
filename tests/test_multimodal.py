import requests
import base64

def test_multimodal():
    url = "http://localhost:8000/api/chat"
    
    # 1. Send Image
    print("--- Turn 1: Sending Image ---")
    image_base64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==" # Red pixel
    
    payload1 = {
        "message": "What color is this image?",
        "image": image_base64
    }
    
    try:
        response1 = requests.post(url, json=payload1)
        print(f"Response 1: {response1.json()['response']}")
    except Exception as e:
        print(f"Error 1: {e}")
        return

    # 2. Follow-up Question (No Image)
    print("\n--- Turn 2: Follow-up Question ---")
    payload2 = {
        "message": "Are you sure? What was the image again?"
    }
    
    try:
        response2 = requests.post(url, json=payload2)
        print(f"Response 2: {response2.json()['response']}")
    except Exception as e:
        print(f"Error 2: {e}")

if __name__ == "__main__":
    test_multimodal()
