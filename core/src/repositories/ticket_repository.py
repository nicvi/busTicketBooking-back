# core/src/repositories/ticket_repository.py

from abc import ABC, abstractmethod
from typing import List
from core.src.models.ticket import Ticket


class TicketRepository(ABC):

    @abstractmethod
    def get_ticket_by_id(self, ticket_id: int) -> Ticket:
        pass

    @abstractmethod
    def list_tickets_by_booking(self, booking_id: int) -> List[Ticket]:
        pass

    @abstractmethod
    def create_ticket(self, ticket: Ticket) -> Ticket:
        pass

    @abstractmethod
    def delete_ticket(self, ticket_id: int) -> None:
        pass
