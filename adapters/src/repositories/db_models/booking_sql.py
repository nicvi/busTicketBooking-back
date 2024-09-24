from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, orm

from .. import db_models


class BookingSql(db_models.Base):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    booking_date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)
    trip_id = Column(Integer, ForeignKey('trip.id'), nullable=False)

    trip = orm.relationship('TripSql', back_populates='bookings')

    def __repr__(self):
        return (f"<BookingSql(id={self.id}, user_id={self.user_id}, "
                f"booking_date={self.booking_date})>, "
                f"status={self.status})>, "
                f"trip_id={self.trip_id})>")
