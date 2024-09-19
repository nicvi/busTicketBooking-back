import pytest

import httpx

from main import app

@pytest.fixture
def client_api():
    transport = httpx.ASGITransport(app=app)
    return httpx.AsyncClient(transport=transport, base_url="http://test")
