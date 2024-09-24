from sqlalchemy import Column, Integer, String, orm

from .. import db_models


class AmenitySql(db_models.Base):
    __tablename__ = 'amenity'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    buses = orm.relationship('BusSql', secondary=db_models.bus_amenity_table, back_populates='amenities')

    def __repr__(self):
        return f"<AmenitySql(id={self.id}, name={self.name})>"
