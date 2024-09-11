class ViewUserBookingsUseCase:
    def __init__(self, booking_repository):
        self.booking_repository = booking_repository

    def execute(self, user_id: int):
        # Fetch bookings for the user
        bookings = self.booking_repository.get_bookings_by_user(user_id)
        return bookings
