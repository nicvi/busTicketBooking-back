from adapters.source.repositories.sql_repositories.sqlalchemy_route_repository import SQLAlchemyRouteRepository
from core.src.use_cases.get_routes import GetRoutesUseCase
from factories.config.sql_alchemy_session import get_db


def get_routes_use_case() -> GetRoutesUseCase:
    db = next(get_db())
    route_repository = SQLAlchemyRouteRepository(session=db)
    routes = GetRoutesUseCase(route_repository=route_repository)
    return routes
