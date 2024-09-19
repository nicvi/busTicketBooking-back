from pydantic import BaseModel  # , EmailStr # allow this import


class UserCreateDTO(BaseModel):
    name: str
    email: str
    phone_number: str
    password: str

class UserResponseDTO(BaseModel):
    id: int
    name: str
    email: str
    phone_number: str

    class Config:
        orm_mode = True
