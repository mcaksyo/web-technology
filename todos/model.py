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
