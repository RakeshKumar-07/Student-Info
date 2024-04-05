import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Student(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str = Field(...)
    age: int = Field(...)
    address: dict = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "John Doe",
                "age": 25,
                "address": {
                    "city": "New York",
                    "country": "USA"
                }
            }
        }


class StudentUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    address: Optional[dict]

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "age": 25,
                "address": {
                    "city": "New York",
                    "country": "USA"
                }
            }
        }