from abc import ABC, abstractmethod

from .. import models


class UserRepository(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id: int) -> models.User:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> models.User:
        pass

    @abstractmethod
    def save_user(self, user: models.User):
        pass
