from pydantic import BaseModel,Field

class Message(BaseModel):
    text: str = Field(min_length=5, max_length=50)