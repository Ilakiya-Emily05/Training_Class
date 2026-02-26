from typing import List, Optional
from app.schemas.participant_schema import ParticipantCreate, ParticipantResponse

class ParticipantRepository:
    def __init__(self):
        self.participants: List[ParticipantResponse] = []
        self.counter = 1  # auto-increment ID

    def save(self, participant: ParticipantCreate) -> ParticipantResponse:
        new_participant = ParticipantResponse(
            id=self.counter,
            name=participant.name,
            email=participant.email,
            event_id=participant.event_id
        )
        self.participants.append(new_participant)
        self.counter += 1
        return new_participant

    def get_by_id(self, participant_id: int) -> Optional[ParticipantResponse]:
        for p in self.participants:
            if p.id == participant_id:
                return p
        return None

    def get_by_email(self, email: str) -> Optional[ParticipantResponse]:
        for p in self.participants:
            if p.email.lower() == email.lower():
                return p
        return None

    def get_all(self) -> List[ParticipantResponse]:
        return self.participants