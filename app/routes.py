from fastapi import APIRouter
from app.payment import process_payment

router = APIRouter()

@router.post("/pay")
def pay(amount: str):
    # INTENTIONAL: no validation
    return process_payment(amount)
