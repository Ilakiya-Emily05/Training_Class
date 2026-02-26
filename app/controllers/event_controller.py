from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.schemas.event_schema import EventCreate, EventResponse
from app.dependencies.service_dependency import event_service

router = APIRouter()

@router.post("/events", response_model=EventResponse)
def create_event(event: EventCreate):
    try:
        return event_service.create_event(event)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/events", response_model=List[EventResponse])
def list_events(location: str = Query(None)):
    if location:
        return event_service.filter_events_by_location(location)
    return event_service.list_events()

@router.get("/events/{event_id}", response_model=EventResponse)
def get_event(event_id: int):
    try:
        return event_service.get_event_by_id(event_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))