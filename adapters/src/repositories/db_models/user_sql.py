from sqlalchemy import Column, Integer, String

from .base import Base


class UserSql(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=True)
    password = Column(String(255), nullable=False)

    def __repr__(self):
        return (f"<id(id={self.id}, "
                f"name={self.name}, "
                f"email={self.email}, "
                f"phone_number={self.phone_number})>")
