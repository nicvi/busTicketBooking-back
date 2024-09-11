from fastapi import APIRouter, Depends, HTTPException, status

from core.src.models.payment import Payment
from core.src.use_cases.process_payment import ProcessPaymentUseCase
from api.dtos.payment_dto import PaymentCreateDTO
from api.dependencies.payment import get_process_payment_use_case

router = APIRouter()

@router.post("/payments", response_model=Payment, status_code=status.HTTP_201_CREATED)
def process_payment(#create_payment
    process_payment_dto: PaymentCreateDTO,
    use_case: ProcessPaymentUseCase = Depends(get_process_payment_use_case),
):
    try:
        payment = use_case.execute(
            booking_id=process_payment_dto.booking_id,
            payment_method=process_payment_dto.payment_method,
        )
        return payment
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

#get_payment
#list_payments