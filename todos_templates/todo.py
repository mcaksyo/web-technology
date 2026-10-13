from pathlib import Path as FilePath

from fastapi import APIRouter, Depends, HTTPException, Path, Request, status
from fastapi.templating import Jinja2Templates

from model import Todo

todo_router = APIRouter()
todo_list: list[Todo] = []
templates = Jinja2Templates(directory=str(FilePath(__file__).parent / "templates"))


@todo_router.post("/todo")
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse(
        request=request,
        name="todo.html",
        context={"todos": todo_list, "todo": None},
    )


@todo_router.get("/todo")
async def retrieve_todo(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="todo.html",
        context={"todos": todo_list, "todo": None},
    )


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(
    request: Request,
    todo_id: int = Path(..., title="ID задачи для просмотра."),
):
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse(
                request=request,
                name="todo.html",
                context={"todos": todo_list, "todo": todo},
            )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача с указанным ID не существует.",
    )
