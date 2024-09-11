from abc import ABC, abstractmethod
from core.src.models.payment import Payment

class PaymentRepository(ABC):
    @abstractmethod
    def save_payment(self, payment: Payment):
        pass

    @abstractmethod
    def get_payment_by_id(self, payment_id: int) -> Payment:
        pass

    @abstractmethod
    def get_payments_by_booking_id(self, booking_id: int) -> list[Payment]:
        pass
