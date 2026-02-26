from typing import List
from app.repositories.participant_repository import ParticipantRepository
from app.repositories.event_repository import EventRepository
from app.schemas.participant_schema import ParticipantCreate, ParticipantResponse

class ParticipantService:
    def __init__(self, participant_repo: ParticipantRepository, event_repo: EventRepository):
        self.participant_repo = participant_repo
        self.event_repo = event_repo

    def register_participant(self, participant: ParticipantCreate) -> ParticipantResponse:
        # Check if event exists
        event = self.event_repo.get_by_id(participant.event_id)
        if not event:
            raise ValueError(f"Event with ID {participant.event_id} does not exist.")

        # Check event capacity
        participants_in_event = [
            p for p in self.participant_repo.get_all() if p.event_id == participant.event_id
        ]
        if len(participants_in_event) >= event.capacity:
            raise ValueError(f"Event '{event.name}' is full.")

        # Check unique email
        if self.participant_repo.get_by_email(participant.email):
            raise ValueError(f"Email '{participant.email}' is already registered.")

        return self.participant_repo.save(participant)

    def get_participant_by_id(self, participant_id: int) -> ParticipantResponse:
        participant = self.participant_repo.get_by_id(participant_id)
        if not participant:
            raise ValueError(f"Participant with ID {participant_id} not found.")
        return participant