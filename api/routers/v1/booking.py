from http import HTTPStatus

from fastapi import Depends, HTTPException, status

import core

from ... import APIRouter, dependencies, dtos

booking = APIRouter()

@booking.get(
    "/{booking_id}",
     name="get_booking",
     status_code=status.HTTP_200_OK,
     response_model=dtos.BookingResponseDTO)
def get_booking_by_id(
        booking_id: int,
        use_case: core.GetBookingById = Depends(dependencies.get_booking_by_id_use_case)
) -> dtos.BookingResponseDTO:
    try:
        query_booking = use_case.execute(booking_id)
        print(f"===> query_booking: {query_booking}")
        response = dtos.BookingResponseDTO.from_orm(query_booking)
        return response
    except Exception as e:
        print(f"===> Exception: {str(e)}")
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))
