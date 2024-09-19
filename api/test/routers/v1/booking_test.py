from http import HTTPStatus
from unittest.mock import Mock

import pytest
# from aiohttp.test_utils import TestClient
from more_itertools.more import side_effect
from pytest_mock import mocker
from fastapi.testclient import TestClient


import api
import core
# import core
from api.routers.v1 import booking
from api.test.fixtures import client_api
from core import GetBookingById
from core.test.fixtures.booking_fixture import mock_booking
from core.test.fixtures.booking_use_case_fixture import mock_get_booking_by_id_use_case
from main import app

from api import get_booking_by_id_use_case


@pytest.mark.asyncio
async def test_get_booking_by_id_success(client_api, mock_get_booking_by_id_use_case, mock_booking):
    app.dependency_overrides[get_booking_by_id_use_case] = lambda: mock_get_booking_by_id_use_case
    expected_response = {
        "id": mock_booking.id,
        "user_id": mock_booking.user_id,
        "booking_date": mock_booking.booking_date.isoformat(),
        "status": mock_booking.status,
        'trip_id': mock_booking.trip_id
    }

    response = await client_api.get("/api/booking/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == expected_response
    del app.dependency_overrides[get_booking_by_id_use_case]

@pytest.mark.asyncio
async def test_get_booking_by_id_failure(monkeypatch,mock_booking):
    client = TestClient(app)
    mock_use_case = Mock()
    mock_use_case.side_effect = Exception("Something went wrong")

    def mock_execute(self, booking_id):
        raise Exception("Something went wrong")

    # app.dependency_overrides[get_booking_by_id_use_case] = lambda: mock_use_case
    # monkeypatch.setattr(api.dependencies.booking, "get_booking_by_id_use_case", lambda: mock_use_case)
    monkeypatch.setattr(
        target = GetBookingById,
        name = "execute",
        value = mock_use_case.side_effect
    )
    # core.src.use_cases.get_booking_by_id.py


    # Call the API endpoint
    response = client.get("/api/booking/1")
    print(f"===> response: {response}")
    print(f"===> response.text: {response.text}")

    # Check if HTTP 500 Internal Server Error is returned
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    # Check if the returned error message matches the one raised
    assert response.json() == {"detail": "Something went wrong"}
