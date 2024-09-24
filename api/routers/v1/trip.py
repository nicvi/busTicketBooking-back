from datetime import datetime
from http import HTTPStatus

from fastapi import Depends, HTTPException, status

import core

from ... import config, dependencies, dtos

trip = config.APIRouter()

@trip.get(
    path="/",
    name="get_trips",
    status_code=status.HTTP_200_OK,
    response_model=list[dtos.TripResponseDTO]
)
def get_available_trips(
        origin_city: str,
        destination_city: str,
        departure_date: datetime,
        use_case: core.GetAvailableTrips = Depends(dependencies.get_view_available_trips_use_case),
):
    try:
        query_trips = use_case.execute(origin_city, destination_city, departure_date)
        response = [dtos.TripResponseDTO.from_orm(query_trip) for query_trip in query_trips]
        return response
    except Exception as error:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(error))
