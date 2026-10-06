from fastapi import FastAPI

from todo import todo_router

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Привет Мир! Яныбин Владлен ИВТ-ПО-401Б"}


app.include_router(todo_router)
