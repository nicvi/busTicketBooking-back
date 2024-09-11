class CancelBookingUseCase:
    def __init__(self, booking_repository, trip_repository, ticket_repository):
        self.booking_repository = booking_repository
        self.trip_repository = trip_repository
        self.ticket_repository = ticket_repository

    def execute(self, booking_id: int):
        # Find the booking
        booking = self.booking_repository.get_booking_by_id(booking_id)
        if not booking:
            raise ValueError("Booking not found")

        # Cancel the booking
        booking.status = "canceled"
        self.booking_repository.update_booking(booking)

        # Free up the seats in the trip
        trip = self.trip_repository.get_trip_by_id(booking.trip_id)
        occupied_seats = len(self.ticket_repository.get_tickets_by_booking(booking_id))
        trip.seats_occupied -= occupied_seats
        self.trip_repository.update_trip(trip)

        self.ticket_repository.cancel_tickets_by_booking(booking_id)# Optionally, delete the tickets or mark them as canceled
