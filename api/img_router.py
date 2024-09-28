from typing import Annotated
from fastapi import APIRouter, Depends

from llmmodel.schemas import SImgData, Result
from llmmodel.llm_connection import image_to_text_req

router = APIRouter(
    prefix="/img",
    tags=["Image Request"],
)


@router.post("")
async def make_description(img_data: Annotated[SImgData, Depends()]) -> Result:
    description = await image_to_text_req(img_data)
    return {"description": description}
