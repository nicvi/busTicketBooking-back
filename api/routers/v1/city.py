from http import HTTPStatus

from fastapi import Depends, HTTPException, status

import core

from ... import APIRouter, dependencies

city = APIRouter()

@city.get(
    "/",
    name="get_cities",
    status_code=status.HTTP_200_OK,
    response_model=list[str])
def get_cities(use_case: core.GetCities = Depends(dependencies.get_cities_use_case)):
    try:
        cities = use_case.execute()
        return cities
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))
