import pytest

from unittest.mock import MagicMock


@pytest.fixture
def mock_get_booking_by_id_use_case(mock_booking):
    mock_use_case = MagicMock()
    mock_use_case.execute.return_value = mock_booking
    return mock_use_case