import uvicorn
from fastapi import FastAPI
from api.text_router import router as txt_router
from api.img_router import router as img_router

app = FastAPI()
app.include_router(txt_router)
app.include_router(img_router)

if __name__ == "__main__":
    uvicorn.run(app, port=8069)
