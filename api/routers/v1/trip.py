from datetime import datetime

from fastapi import Depends

import core

from ... import APIRouter, dependencies, dtos

trip = APIRouter()

@trip.get(
    "/available_trips",
    response_model=list[dtos.TripResponseDTO]
)
def get_available_trips(
        origin_city: str,
        destination_city: str,
        departure_date: datetime,
        use_case: core.GetAvailableTrips = Depends(dependencies.get_view_available_trips_use_case),
):
    trips = use_case.execute(origin_city, destination_city, departure_date)
    return trips
