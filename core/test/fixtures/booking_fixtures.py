from datetime import datetime
from unittest.mock import MagicMock

import pytest


@pytest.fixture
def mock_booking():
    mock_booking = MagicMock()
    mock_booking.id = 1
    mock_booking.user_id = 1
    mock_booking.booking_date = datetime.today()
    mock_booking.status = "active"
    mock_booking.trip_id = 1
    return mock_booking

@pytest.fixture
def mock_get_booking_by_id_use_case(mock_booking):
    mock_use_case = MagicMock()
    mock_use_case.execute.return_value = mock_booking
    return mock_use_case
