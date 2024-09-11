from fastapi import Depends, HTTPException, status

from core.src.models.payment import Payment
from api.dtos.payment_dto import PaymentCreateDTO
# from api.dependencies.payment import get_process_payment_use_case # implement
from utils.api_router.router import APIRouter

payment = APIRouter()

# implement: process_payment (post)
# implement: get_payment_by_id
# implement: list_payments (get)
