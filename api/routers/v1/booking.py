from http import HTTPStatus

from fastapi import Depends, HTTPException, status
from datetime import datetime

from core.src.use_cases.create_booking import CreateBookingUseCase
from core.src.use_cases.cancel_booking import CancelBookingUseCase
from api.dtos.booking_dto import BookingCreateDTO, BookingResponseDTO
from api.dependencies.booking import get_create_booking_use_case, get_cancel_booking_use_case, get_booking_use_case
from core.src.use_cases.get_booking import GetBookingUseCase
from utils.api_router.router import APIRouter

booking = APIRouter()

@booking.post("/", name= "create_booking", response_model=BookingResponseDTO, status_code=status.HTTP_201_CREATED)
def create_booking(
    create_booking_dto: BookingCreateDTO,
    use_case: CreateBookingUseCase = Depends(get_create_booking_use_case),
):
    try:
        booking_generated = use_case.execute(
            user_id=create_booking_dto.user_id,
            trip_id=create_booking_dto.trip_id,
            seat_numbers=create_booking_dto.seat_numbers,
            booking_date=datetime.now(),
        )
        return booking_generated
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

#get_booking
@booking.get(
    "/{booking_id}",
     name="get_booking",
     status_code=status.HTTP_200_OK,
     response_model=BookingResponseDTO)
def get_booking(
        booking_id: int,
        use_case: GetBookingUseCase = Depends(get_booking_use_case)
) -> BookingResponseDTO:
    try:
        query_booking = use_case.execute(booking_id)
        response = BookingResponseDTO(query_booking)
        return response
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))

#list_bookings

@booking.delete("/{booking_id}", name= "cancel booking", status_code=status.HTTP_204_NO_CONTENT)
def cancel_booking(
    booking_id: int,
    use_case: CancelBookingUseCase = Depends(get_cancel_booking_use_case),
):
    try:
        use_case.execute(booking_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@booking.get("/", name = "get", status_code=status.HTTP_200_OK)# delete it
async def get():
    return {"app": "bus booking", "version": "0.1"}