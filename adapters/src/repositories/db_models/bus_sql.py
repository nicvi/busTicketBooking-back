from sqlalchemy import Column, Integer, String, orm

from .. import db_models


class BusSql(db_models.Base):
    __tablename__ = 'bus'

    id = Column(Integer, primary_key=True, autoincrement=True)
    bus_number = Column(String(50), nullable=False)
    number_of_seats = Column(Integer, nullable=False)

    amenities = orm.relationship('AmenitySql', secondary=db_models.bus_amenity_table, back_populates='buses')
    trips = orm.relationship('TripSql', back_populates='bus')

    def __repr__(self):
        return (f"<BusSql(id={self.id}, bus_number={self.bus_number}, "
                f"number_of_seats={self.number_of_seats})>")
