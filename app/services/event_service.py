from typing import List
from app.repositories.event_repository import EventRepository
from app.schemas.event_schema import EventCreate, EventResponse

class EventService:
    def __init__(self, event_repo: EventRepository):
        self.event_repo = event_repo

    def create_event(self, event: EventCreate) -> EventResponse:
        # Prevent duplicate event names
        for e in self.event_repo.get_all():
            if e.name.lower() == event.name.lower():
                raise ValueError(f"Event with name '{event.name}' already exists.")
        return self.event_repo.save(event)

    def list_events(self) -> List[EventResponse]:
        return self.event_repo.get_all()

    def get_event_by_id(self, event_id: int) -> EventResponse:
        event = self.event_repo.get_by_id(event_id)
        if not event:
            raise ValueError(f"Event with ID {event_id} not found.")
        return event

    def filter_events_by_location(self, location: str) -> List[EventResponse]:
        return self.event_repo.filter_by_location(location)