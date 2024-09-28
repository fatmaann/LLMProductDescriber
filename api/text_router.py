from typing import Annotated
from fastapi import APIRouter, Depends

from llmmodel.schemas import STextData, Result
from llmmodel.llm_connection import text_to_text_req

router = APIRouter(
    prefix="/text",
    tags=["Text Request"],
)


@router.post("")
async def make_description(text_data: Annotated[STextData, Depends()]) -> Result:
    description = await text_to_text_req(text_data)
    return {"description": description}
