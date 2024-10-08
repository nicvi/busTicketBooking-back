from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    email: str
    phone_number: str
    password: str
