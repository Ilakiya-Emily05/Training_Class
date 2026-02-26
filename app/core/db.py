from app.repositories.event_repository import EventRepository
from app.repositories.participant_repository import ParticipantRepository

# Single instances for the whole app
event_repo = EventRepository()
participant_repo = ParticipantRepository()