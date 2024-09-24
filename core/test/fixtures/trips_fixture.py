from unittest.mock import MagicMock
import pytest

@pytest.fixture
def mock_trips():
    mock_trip = MagicMock()
    mock_trip.id = 1
    mock_trip.bus_id = 1
    mock_trip.route_id = 1
    mock_trip.seats_occupied = 1
    return [mock_trip]

@pytest.fixture
def mock_view_available_trips_use_case(mock_trips):
    mock_use_case = MagicMock()
    mock_use_case.execute.return_value = mock_trips
    return mock_use_case
