from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .bus_amenity_sql import bus_amenity_table


class BusSql(Base):
    __tablename__ = 'bus'

    id = Column(Integer, primary_key=True, autoincrement=True)
    bus_number = Column(String(50), nullable=False)
    number_of_seats = Column(Integer, nullable=False)

    amenities = relationship('AmenitySql', secondary=bus_amenity_table, back_populates='buses')
    trips = relationship('TripSql', back_populates='bus')

    def __repr__(self):
        return (f"<BusSql(id={self.id}, bus_number={self.bus_number}, "
                f"number_of_seats={self.number_of_seats})>")