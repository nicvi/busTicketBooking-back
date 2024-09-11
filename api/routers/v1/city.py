from http import HTTPStatus

from fastapi import Depends, status, HTTPException

from api.dependencies.city import get_cities_use_case
from core.src.use_cases.get_cities import GetCitiesUseCase
from typing import List
from utils.api_router.router import APIRouter

city = APIRouter()

@city.get(
    "/",
    name="get_cities",
    status_code=status.HTTP_200_OK,
    response_model=List)
def get_cities(use_case: GetCitiesUseCase = Depends(get_cities_use_case)):
    try:
        cities = use_case.execute()
        return cities
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))
