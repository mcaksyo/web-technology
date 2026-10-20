from pydantic import BaseModel, ConfigDict, EmailStr, Field

from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: list[Event] = Field(default_factory=list)


class NewUser(User):
    username: str

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "email": "fastapi@packt.com",
                    "password": "Strong!123",
                    "username": "FastPackt",
                    "events": [],
                }
            ]
        }
    )


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "email": "fastapi@packt.com",
                    "password": "Strong!123",
                }
            ]
        }
    )
