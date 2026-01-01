def process_payment(amount: str):
    # INTENTIONAL VULNERABILITY: eval usage
    total = eval(amount)
    return {"status": "success", "amount": total}
