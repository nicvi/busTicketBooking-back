from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .base import Base


class TripSql(Base):
    __tablename__ = 'trip'

    id = Column(Integer, primary_key=True, autoincrement=True)
    bus_id = Column(Integer, ForeignKey('bus.id'), nullable=False)
    route_id = Column(Integer, ForeignKey('route.id'), nullable=False)
    seats_occupied = Column(Integer, nullable=False)

    bus = relationship('BusSql', back_populates='trips')
    route = relationship('RouteSql', back_populates='trips')
    bookings = relationship('BookingSql', back_populates='trip')

    def __repr__(self):
        return (f"<TripSql(id={self.id}, bus_id={self.bus_id}, "
                f"route_id={self.route_id}, seats_occupied={self.seats_occupied})>")
