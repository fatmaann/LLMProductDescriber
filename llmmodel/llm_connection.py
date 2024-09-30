from mistralai import Mistral
from llmmodel.utils import decode_image
from llmmodel.schemas import STextData, SImgData
from config import API_KEY, TEXT_MODEL, MAIN_SYSTEM_PROMPT, \
    MAIN_CONTEXT_PROMPT, IMAGE_TO_TEXT_MODEL, IMAGE_TO_TEXT_CONTEXT_PROMPT, \
    IMAGE_TO_TEXT_SYSTEM_PROMPT

client = Mistral(api_key=API_KEY)


async def text_to_text_req(product: STextData):
    llm_response = client.chat.complete(
        model=TEXT_MODEL,
        messages=[
            {
                "role": "system",
                "content": MAIN_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": MAIN_CONTEXT_PROMPT.format(text=product.name,
                                                      size=product.size,
                                                      color=product.color,
                                                      material=product.material),
            },
        ],
    )
    return llm_response.choices[0].message.content


async def image_to_text_req(product: SImgData):
    dec_image = decode_image(product.image_path)
    model_response = client.chat.complete(
        model=IMAGE_TO_TEXT_MODEL,
        messages=[
            {
                "role": "system",
                "content": IMAGE_TO_TEXT_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": IMAGE_TO_TEXT_CONTEXT_PROMPT.format(description=product.description)
                    },
                    {
                        "type": "image_url",
                        "image_url": dec_image
                    }
                ],
            },
        ],
    )
    return model_response.choices[0].message.content
