from sqlalchemy import Column, ForeignKey, Integer, orm

from .. import db_models


class TripSql(db_models.Base):
    __tablename__ = 'trip'

    id = Column(Integer, primary_key=True, autoincrement=True)
    bus_id = Column(Integer, ForeignKey('bus.id'), nullable=False)
    route_id = Column(Integer, ForeignKey('route.id'), nullable=False)
    seats_occupied = Column(Integer, nullable=False)

    bus = orm.relationship('BusSql', back_populates='trips')
    route = orm.relationship('RouteSql', back_populates='trips')
    bookings = orm.relationship('BookingSql', back_populates='trip')

    def __repr__(self):
        return (f"<TripSql(id={self.id}, bus_id={self.bus_id}, "
                f"route_id={self.route_id}, seats_occupied={self.seats_occupied})>")
