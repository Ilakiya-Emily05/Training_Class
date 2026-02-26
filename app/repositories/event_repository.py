from typing import List, Optional
from app.schemas.event_schema import EventResponse, EventCreate

class EventRepository:
    def __init__(self):
        self.events: List[EventResponse] = []
        self.counter = 1  # auto-increment ID

    def save(self, event: EventCreate) -> EventResponse:
        new_event = EventResponse(
            id=self.counter,
            name=event.name,
            location=event.location,
            capacity=event.capacity
        )
        self.events.append(new_event)
        self.counter += 1
        return new_event

    def get_all(self) -> List[EventResponse]:
        return self.events

    def get_by_id(self, event_id: int) -> Optional[EventResponse]:
        for event in self.events:
            if event.id == event_id:
                return event
        return None

    def filter_by_location(self, location: str) -> List[EventResponse]:
        return [event for event in self.events if event.location.lower() == location.lower()]