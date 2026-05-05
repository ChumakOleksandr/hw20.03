from fastapi import FastAPI

app = FastAPI()


@app.get("/greeting")
def greeting():
    return {"respond": "Привіт з сервера2"}
