import base64
import requests
from etc.config import MAIN_SYSTEM_PROMPT, MAIN_CONTEXT_PROMPT, IMAGE_TO_TEXT_CONTEXT_PROMPT


def decode_image(image_path: str) -> str:
    try:
        img_response = requests.get(image_path)
        if img_response.status_code == 200:
            encoded_string = base64.b64encode(img_response.content).decode('utf-8')
            return encoded_string
        return ""
    except Exception as e:
        return ""


async def compile_text_mgs(name: str, size: str = "", color: str = "", material: str = "") -> list[dict]:
    messages = [{"role": "system", "content": MAIN_SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": MAIN_CONTEXT_PROMPT.format(text=name, size=size, color=color, material=material),
                },
                ]
    return messages


async def compile_img_mgs(dec_image: str, description: str) -> list[dict]:
    messages = [{"role": "system", "content": MAIN_SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": IMAGE_TO_TEXT_CONTEXT_PROMPT.format(description=description)
                        },
                        {
                            "type": "image_url",
                            "image_url": f'data:image/jpeg;base64,{dec_image}'
                        }
                    ],
                },
                ]
    return messages
