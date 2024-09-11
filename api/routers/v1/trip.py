from fastapi import Depends
from datetime import datetime
from typing import List

from core.src.models.trip import Trip
from core.src.use_cases.get_available_trips import GetAvailableTripsUseCase
from api.dependencies.trip import get_view_available_trips_use_case
from utils.api_router.router import APIRouter

trip = APIRouter()

@trip.get(
    "/available_trips",
    response_model=List[Trip]
)
def get_available_trips(
        origin_city: str,
        destination_city: str,
        departure_date: datetime,
        use_case: GetAvailableTripsUseCase = Depends(get_view_available_trips_use_case),
):
    trips = use_case.execute(origin_city, destination_city, departure_date)
    return trips
