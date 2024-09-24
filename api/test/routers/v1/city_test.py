from http import HTTPStatus
from unittest.mock import Mock

import pytest

import core
from main import app

from .... import dependencies


@pytest.mark.asyncio
async def test_get_cities_success(client_api, mock_get_cities_use_case, mock_cities):
    app.dependency_overrides[dependencies.get_cities_use_case] = lambda: mock_get_cities_use_case
    expected_response = mock_cities

    response = await client_api.get("/api/city/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == expected_response
    del app.dependency_overrides[dependencies.get_cities_use_case]

@pytest.mark.asyncio
async def test_get_cities_exception_captured_when_use_case_throws_error(client_api, monkeypatch):
    mock_use_case = Mock()
    mock_use_case.side_effect = Exception("Something went wrong")
    monkeypatch.setattr(
        target=core.GetCities,
        name="execute",
        value=mock_use_case
    )

    response = await client_api.get("/api/city/")

    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert response.json() == {"detail": "Something went wrong"}
