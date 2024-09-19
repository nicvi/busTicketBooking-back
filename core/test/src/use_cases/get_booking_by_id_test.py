import unittest
from datetime import datetime
from unittest.mock import MagicMock

from core.src.models.booking import Booking
from core.src.repositories.booking_repository import BookingRepository
from core.src.use_cases.get_booking_by_id import GetBookingById


class TestGetBookingById(unittest.TestCase):
    def setUp(self):
        self.mock_booking_repository = MagicMock(spec=BookingRepository)
        self.get_booking_by_id = GetBookingById(self.mock_booking_repository)

    def test_execute_with_valid_booking(self):
        # Define test data
        booking_id = 1
        booking = Booking(
            id=booking_id,
            user_id=123,
            booking_date=datetime.today().date(),
            status="confirmed",
            trip_id=10
        )
        self.mock_booking_repository.get_booking_by_id.return_value = booking

        result = self.get_booking_by_id.execute(booking_id)

        self.mock_booking_repository.get_booking_by_id.assert_called_once_with(booking_id)
        self.assertEqual(result, booking)

    def test_execute_with_invalid_booking(self):
        booking_id = 999
        self.mock_booking_repository.get_booking_by_id.return_value = None

        result = self.get_booking_by_id.execute(booking_id)

        self.mock_booking_repository.get_booking_by_id.assert_called_once_with(booking_id)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
