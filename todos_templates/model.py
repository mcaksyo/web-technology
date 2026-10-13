from typing import Optional

from fastapi import Form
from pydantic import BaseModel


class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    @classmethod
    def as_form(cls, item: str = Form(...)) -> "Todo":
        return cls(item=item)
