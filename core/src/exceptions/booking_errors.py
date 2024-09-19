class BookingNotFoundError(Exception):
    def __init__(self, error_msg: str = "Booking not found"):
        super().__init__(error_msg)

        self.error_msg = error_msg
