from app.core.db import event_repo, participant_repo
from app.services.event_service import EventService
from app.services.participant_service import ParticipantService

# Single instances of services using the singleton repos
event_service = EventService(event_repo)
participant_service = ParticipantService(participant_repo, event_repo)