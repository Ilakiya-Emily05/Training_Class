from pydantic import BaseModel, Field
from typing import Optional

# Request model for creating an event
class EventCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    location: str = Field(..., min_length=2, max_length=50)
    capacity: int = Field(..., gt=0)

# Response model for sending event data back
class EventResponse(BaseModel):
    id: int
    name: str
    location: str
    capacity: int