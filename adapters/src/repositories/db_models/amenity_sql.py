from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .bus_amenity_sql import bus_amenity_table


class AmenitySql(Base):
    __tablename__ = 'amenity'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    buses = relationship('BusSql', secondary=bus_amenity_table, back_populates='amenities')

    def __repr__(self):
        return f"<AmenitySql(id={self.id}, name={self.name})>"
