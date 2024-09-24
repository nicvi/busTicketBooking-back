from sqlalchemy import Column, ForeignKey, Integer, Table

from .. import db_models

bus_amenity_table = Table('bus_amenity', db_models.Base.metadata,
    Column('bus_id', Integer, ForeignKey('bus.id'), primary_key=True),
    Column('amenity_id', Integer, ForeignKey('amenity.id'), primary_key=True)
)
