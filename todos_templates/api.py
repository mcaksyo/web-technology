from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from todo import todo_router

app = FastAPI(title="Todo с Jinja2")
app.include_router(todo_router)


@app.get("/", include_in_schema=False)
async def home() -> RedirectResponse:
    return RedirectResponse(url="/todo", status_code=303)
