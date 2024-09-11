from http import HTTPStatus

from fastapi import Depends, HTTPException, status

from api.dtos.booking_dto import BookingResponseDTO
from api.dependencies.booking import get_booking_by_id_use_case
from core.src.use_cases.get_booking_by_id import GetBookingById
from utils.api_router.router import APIRouter

booking = APIRouter()

# implement: get_all_bookings
# implement: create_booking

@booking.get(
    "/{booking_id}",
     name="get_booking",
     status_code=status.HTTP_200_OK,
     response_model=BookingResponseDTO)
def get_booking_by_id(
        booking_id: int,
        use_case: GetBookingById = Depends(get_booking_by_id_use_case)
) -> BookingResponseDTO:
    try:
        query_booking = use_case.execute(booking_id)
        response = BookingResponseDTO.from_orm(query_booking)
        return response
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))
