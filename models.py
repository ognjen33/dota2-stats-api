from pydantic import BaseModel


class SimpleModel(BaseModel):
    id: int
    name: str
