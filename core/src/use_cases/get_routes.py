from core.src.repositories.route_repository import RouteRepository
from core.src.models.route import Route
from typing import List


class GetRoutesUseCase:
    def __init__(self, route_repository: RouteRepository):
        self.route_repository = route_repository

    def execute(self, origin_city: str, destination_city: str) -> List[Route]:
        print("===> here in execute GetRoutesUseCase")
        routes = self.route_repository.get_routes(origin_city, destination_city)
        print(f"===> routes {routes}")
        return routes
