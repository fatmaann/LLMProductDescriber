import base64
import requests


def decode_image(image_path):
    encoded_string = ""
    try:
        img_response = requests.get(image_path)
        if img_response.status_code == 200:
            encoded_string = base64.b64encode(img_response.content).decode('utf-8')
            return f"data:image/jpeg;base64,{encoded_string}"
        return f"data:image/jpeg;base64,"
    except Exception as e:
        return f"data:image/jpeg;base64,"

