from typing import List

from pydantic import BaseModel, ConfigDict


class Todo(BaseModel):
    id: int
    item: str

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "id": 1,
                    "item": "Простая схема!",
                }
            ]
        }
    )


class TodoItem(BaseModel):
    item: str

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "item": "Прочитать следующую главу книги",
                }
            ]
        }
    )


class TodoItems(BaseModel):
    todos: List[TodoItem]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "todos": [
                        {"item": "Пример схемы 1!"},
                        {"item": "Пример схемы 2!"},
                    ]
                }
            ]
        }
    )
