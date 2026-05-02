import os
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.payment import process_payment

router = APIRouter()

@router.post("/pay")
def pay(amount: str):
    # INTENTIONAL: no validation
    return process_payment(amount)


@router.get("/download")
def download(file: str):
    # INTENTIONAL VULNERABILITY: path traversal
    with open(f"./files/{file}", "r") as content:
        return {"content": content.read()}


@router.get("/goto")
def goto(url: str):
    # INTENTIONAL VULNERABILITY: open redirect
    return RedirectResponse(url)
