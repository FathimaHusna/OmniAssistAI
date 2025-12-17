import requests
import base64

def test_png():
    url = "http://localhost:8000/api/chat"
    
    # Base64 for a 1x1 PNG (Red)
    # This is a valid PNG.
    png_base64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
    
    # The backend currently hardcodes "data:image/jpeg;base64,..."
    # So we are testing if sending a PNG data but labeled as JPEG works.
    
    payload = {
        "message": "What is this image?",
        "image": png_base64
    }
    
    try:
        response = requests.post(url, json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_png()
