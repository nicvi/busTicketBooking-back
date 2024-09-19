from abc import ABC, abstractmethod

from core.src.models.route import Route


class RouteRepository(ABC):
    @abstractmethod
    def get_route_by_id(self, route_id: int) -> Route:
        pass

    @abstractmethod
    def get_routes(self, origin_city: str, destination_city: str) -> list[Route]:
        pass

    @abstractmethod
    def save_route(self, route: Route):
        pass
