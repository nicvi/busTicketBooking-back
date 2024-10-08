from pydantic import BaseModel, EmailStr


class UserCreateDTO(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    password: str

class UserResponseDTO(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone_number: str

    class Config:
        orm_mode = True
