from http import HTTPStatus
from unittest.mock import Mock

import pytest

import core
from main import app

from .... import dependencies, dtos

params = {
    "origin_city": "New York",
    "destination_city": "Los Angeles",
    "departure_date": "2024-09-23T00:00:00"
}

@pytest.mark.asyncio
async def test_get_trips_success(client_api, mock_view_available_trips_use_case, mock_trips):
    app.dependency_overrides[dependencies.get_view_available_trips_use_case] =\
        lambda: mock_view_available_trips_use_case
    expected_response = [dtos.TripResponseDTO.from_orm(query_trip) for query_trip in mock_trips]


    response = await client_api.get("/api/trip/", params=params)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == expected_response
    del app.dependency_overrides[dependencies.get_view_available_trips_use_case]

@pytest.mark.asyncio
async def test_get_trips_exception_captured_when_use_case_throws_error(client_api, monkeypatch):
    mock_use_case = Mock()
    mock_use_case.side_effect = Exception("Something went wrong")
    monkeypatch.setattr(
        target=core.GetAvailableTrips,
        name="execute",
        value=mock_use_case
    )

    response = await client_api.get("/api/trip/", params=params)

    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert response.json() == {"detail": "Something went wrong"}
