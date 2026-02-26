from pydantic import BaseModel, EmailStr, Field

# Request model for registering participant
class ParticipantCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    event_id: int

# Response model for participant info
class ParticipantResponse(BaseModel):
    id: int
    name: str
    email: str
    event_id: int