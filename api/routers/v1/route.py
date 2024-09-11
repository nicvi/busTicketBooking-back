from http import HTTPStatus

from fastapi import Depends, HTTPException, status

from api.dependencies.route import get_routes_use_case
from api.dtos.route_dto import RouteResponseDTO
from core.src.use_cases.get_routes import GetRoutesUseCase
from utils.api_router.router import APIRouter
from typing import List

route = APIRouter()

#get_route
@route.get(
    "/{origin_city}/{destination_city}",
     name="get_routes",
     status_code=status.HTTP_200_OK,
     response_model=List)
def get_routes(
        origin_city: str,
        destination_city: str,
        use_case: GetRoutesUseCase = Depends(get_routes_use_case)
) -> List[RouteResponseDTO]:
    try:
        query_booking = use_case.execute(origin_city, destination_city)# convert it to dto response
        response = []
        return response
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))
