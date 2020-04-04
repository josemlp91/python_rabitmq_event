from datetime import datetime
from pydantic import BaseModel, UUID1

class Animal(BaseModel):
    name: str

class AnimalEventData(BaseModel):
    id: UUID1
    type: str
    ocurred_on: datetime
    attributes: Animal


class AnimalEvent(BaseModel):
    data: AnimalEventData