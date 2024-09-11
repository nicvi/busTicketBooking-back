from datetime import datetime

class ProcessPaymentUseCase:
    def __init__(self, payment_repository, booking_repository):
        self.payment_repository = payment_repository
        self.booking_repository = booking_repository

    def execute(self, booking_id: int, payment_method: str):
        # Check if the booking exists
        booking = self.booking_repository.get_booking_by_id(booking_id)
        if not booking:
            raise ValueError("Booking not found")

        # Create a payment record
        payment = self.payment_repository.create_payment(booking_id, payment_method, "pending", datetime.now())

        # Update booking status to 'paid'
        booking.status = "paid"
        self.booking_repository.update_booking(booking)

        return payment
