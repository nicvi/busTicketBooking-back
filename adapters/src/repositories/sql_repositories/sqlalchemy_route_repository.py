from sqlalchemy.orm import Session

from core.src.models.route import Route
from core.src.repositories.route_repository import RouteRepository


class SQLAlchemyRouteRepository(RouteRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_route_by_id(self, route_id: int) -> Route:
        pass

    def get_routes(self, origin_city: str, destination_city: str) -> list[Route]:
        pass

    def save_route(self, route: Route):
        pass
