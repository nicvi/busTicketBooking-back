from core.src.use_cases.process_payment import ProcessPaymentUseCase
from core.src.repositories.booking_repository import BookingRepository
from core.src.repositories.payment_repository import PaymentRepository

def get_process_payment_use_case() -> ProcessPaymentUseCase:
    return ProcessPaymentUseCase(
        payment_repository=PaymentRepository(),
        booking_repository=BookingRepository(),
    )
