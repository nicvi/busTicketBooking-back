from sqlalchemy import Table, Column, Integer, ForeignKey

from .base import Base

bus_amenity_table = Table('bus_amenity', Base.metadata,
    Column('bus_id', Integer, ForeignKey('bus.id'), primary_key=True),
    Column('amenity_id', Integer, ForeignKey('amenity.id'), primary_key=True)
)
