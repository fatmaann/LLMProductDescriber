from pydantic import BaseModel, Field
from typing import Optional


class STextData(BaseModel):
    name: str = Field(..., description="Характеристики товара")
    size: Optional[str] = Field('', description="Размер товара")
    color: Optional[str] = Field('', description="Цвет товара")
    material: Optional[str] = Field('', description="Материал товара")


class SImgData(BaseModel):
    image_path: str = Field(..., description="Ссылка на изображение товара")
    description: Optional[str] = Field("", description="Описание товара")


class Result(BaseModel):
    description: str = Field(..., description="Описание товара")
