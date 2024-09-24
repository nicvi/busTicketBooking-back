from unittest.mock import MagicMock
import pytest

@pytest.fixture
def mock_cities():
    return ["New York", "Los Angeles", "Chicago"]


@pytest.fixture
def mock_get_cities_use_case(mock_cities):
    mock_use_case = MagicMock()
    mock_use_case.execute.return_value = mock_cities
    return mock_use_case
