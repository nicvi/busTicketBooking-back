import uuid

from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class RouteSql(Base):
    __tablename__ = 'route'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    origin_city = Column(String(100), nullable=False)
    destination_city = Column(String(100), nullable=False)
    departure_date = Column(DateTime, nullable=False)


    trips = relationship('TripSql', back_populates='route')

    def __repr__(self):
        return (f"<Route(id={self.id}, origin_city={self.origin_city},"
                f" destination_city={self.destination_city},"
                f" departure_date={self.departure_date})>")
