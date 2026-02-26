from fastapi import APIRouter, HTTPException
from app.schemas.participant_schema import ParticipantCreate, ParticipantResponse
from app.dependencies.service_dependency import participant_service

router = APIRouter()

@router.post("/participants", response_model=ParticipantResponse)
def register_participant(participant: ParticipantCreate):
    try:
        return participant_service.register_participant(participant)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/participants/{participant_id}", response_model=ParticipantResponse)
def get_participant(participant_id: int):
    try:
        return participant_service.get_participant_by_id(participant_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))