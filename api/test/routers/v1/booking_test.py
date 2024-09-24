from http import HTTPStatus
from unittest.mock import Mock

import pytest

import core
from main import app
from .... import dependencies

@pytest.mark.asyncio
async def test_get_booking_by_id_success(client_api, mock_get_booking_by_id_use_case, mock_booking):
    app.dependency_overrides[dependencies.get_booking_by_id_use_case] = lambda: mock_get_booking_by_id_use_case
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
    del app.dependency_overrides[dependencies.get_booking_by_id_use_case]

@pytest.mark.asyncio
async def test_get_booking_by_id_failure(client_api, monkeypatch):
    mock_use_case = Mock()
    mock_use_case.side_effect = Exception("Something went wrong")
    monkeypatch.setattr(
        target = core.GetBookingById,
        name = "execute",
        value = mock_use_case
    )
    response = await client_api.get("/api/booking/1")

    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert response.json() == {"detail": "Something went wrong"}
