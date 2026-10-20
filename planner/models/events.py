from pydantic import BaseModel, ConfigDict


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: list[str]
    location: str

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "id": 1,
                    "title": "FastAPI Book Launch",
                    "image": "https://linktomyimage.com/image.png",
                    "description": (
                        "We will be discussing the contents of the FastAPI book "
                        "in this event."
                    ),
                    "tags": ["python", "fastapi", "book", "launch"],
                    "location": "Google Meet",
                }
            ]
        }
    )
