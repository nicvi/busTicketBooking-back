import uuid

from sqlalchemy import Column, DateTime, Integer, String, orm
from sqlalchemy.dialects.postgresql import UUID

from .. import db_models


class RouteSql(db_models.Base):
    __tablename__ = 'route'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    origin_city = Column(String(100), nullable=False)
    destination_city = Column(String(100), nullable=False)
    departure_date = Column(DateTime, nullable=False)


    trips = orm.relationship('TripSql', back_populates='route')

    def __repr__(self):
        return (f"<Route(id={self.id}, origin_city={self.origin_city},"
                f" destination_city={self.destination_city},"
                f" departure_date={self.departure_date})>")
