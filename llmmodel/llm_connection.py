from mistralai import Mistral
from llmmodel.utils import decode_image, compile_text_mgs, compile_img_mgs
from llmmodel.schemas import STextData, SImgData
from config import API_KEY, TEXT_MODEL, IMAGE_TO_TEXT_MODEL

client = Mistral(api_key=API_KEY)


async def text_to_text_req(product: STextData):
    model_response = client.chat.complete(
        model=TEXT_MODEL,
        messages=await compile_text_mgs(**product.__dict__),
    )
    return model_response.choices[0].message.content


async def image_to_text_req(product: SImgData):
    dec_image = decode_image(product.image_path)
    if dec_image:
        model_response = client.chat.complete(
            model=IMAGE_TO_TEXT_MODEL,
            messages=await compile_img_mgs(dec_image, product.description),
        )
        return model_response.choices[0].message.content
    if product.description:
        model_response = client.chat.complete(
            model=TEXT_MODEL,
            messages=await compile_text_mgs(product.description),
        )
        return model_response.choices[0].message.content
    return "The request could not be completed. Please check the image link and description."
