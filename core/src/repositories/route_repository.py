from abc import ABC, abstractmethod

from .. import models


class RouteRepository(ABC):
    @abstractmethod
    def get_route_by_id(self, route_id: int) -> models.Route:
        pass

    @abstractmethod
    def get_routes(self, origin_city: str, destination_city: str) -> list[models.Route]:
        pass

    @abstractmethod
    def save_route(self, route: models.Route):
        pass
