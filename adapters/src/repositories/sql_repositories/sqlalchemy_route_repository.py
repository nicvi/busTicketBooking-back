from sqlalchemy.orm import Session

import core


class SQLAlchemyRouteRepository(core.RouteRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_route_by_id(self, route_id: int) -> core.Route:
        pass

    def get_routes(self, origin_city: str, destination_city: str) -> list[core.Route]:
        pass

    def save_route(self, route: core.Route):
        pass
