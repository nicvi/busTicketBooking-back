# api/app/api/src/routers/contact.py check in client bff
import re
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, validator


class ContactBase(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    position: Optional[str]
    location: Optional[str]
    time_zone: Optional[str]
    is_main_contact: Optional[bool] = False
    linkedin_profile: Optional[str]


class ContactCreateIn(ContactBase):
    client_id: UUID
    name: str = Field(..., min_length=2, max_length=100)

    @validator("name")
    @classmethod
    def check_name_is_not_empty(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Name cannot be empty or just whitespace")
        return value

    @validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        if not value:
            return value
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        if re.fullmatch(regex, value):
            return value
        raise ValueError("Invalid email format")


class ContactEditIn(ContactBase):
    @validator("name")
    @classmethod
    def check_name_is_not_empty(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Name cannot be empty or just whitespace")
        return value

    @validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        if not value:
            return value
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        if re.fullmatch(regex, value):
            return value
        raise ValueError("Invalid email format")


class ContactOut(ContactBase):
    client_id: UUID
    id: UUID
    is_archived: bool


class ContactEditOut(ContactBase):
    id: UUID
    contact_id: UUID


class ContactListOut(BaseModel):
    contacts: List[ContactOut]

class ContactDeleteOut(BaseModel):
    is_archived: bool
