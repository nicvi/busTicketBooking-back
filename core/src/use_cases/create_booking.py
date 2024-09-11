from datetime import datetime

class CreateBookingUseCase:
    def __init__(self, booking_repository, trip_repository, ticket_repository):
        self.booking_repository = booking_repository
        self.trip_repository = trip_repository
        self.ticket_repository = ticket_repository

    def execute(self, user_id: int, trip_id: int, seat_numbers: list[int], booking_date: datetime):
        trip = self.trip_repository.get_trip_by_id(trip_id)# Check if the trip exists and has enough available seats
        if not trip:
            raise ValueError("Trip not found")

        if trip.seats_occupied + len(seat_numbers) > trip.bus.number_of_seats:
            raise ValueError("Not enough seats available")

        booking = self.booking_repository.create_booking(user_id, trip_id, booking_date, status="booked")# Create booking

        for seat_number in seat_numbers: # Create tickets
            self.ticket_repository.create_ticket(booking.booking_id, seat_number)

        trip.seats_occupied += len(seat_numbers) # Update trip's occupied seats
        self.trip_repository.update_trip(trip)

        return booking
