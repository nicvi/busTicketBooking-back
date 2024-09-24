from abc import ABC, abstractmethod

from .. import models


class TicketRepository(ABC):

    @abstractmethod
    def get_ticket_by_id(self, ticket_id: int) -> models.Ticket:
        pass

    @abstractmethod
    def list_tickets_by_booking(self, booking_id: int) -> list[models.Ticket]:
        pass

    @abstractmethod
    def create_ticket(self, ticket: models.Ticket) -> models.Ticket:
        pass

    @abstractmethod
    def delete_ticket(self, ticket_id: int) -> None:
        pass
