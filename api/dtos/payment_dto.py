from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PaymentCreateDTO(BaseModel):
    booking_id: int
    payment_method: str
    payment_status: str
    payment_date: datetime

class PaymentResponseDTO(BaseModel):
    id: int
    booking_id: int
    payment_method: str
    payment_status: str
    payment_date: datetime

    class Config:
        orm_mode = True