from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("home")
def get_home():
    return "hi"


if __name__ == "__main__":
    uvicorn.run(app, port=8081)
