def process_payment(amount: str):
    # Define but never use variable
    unused_variable = 8 + 10
    # INTENTIONAL VULNERABILITY: eval usage

    total = eval(amount)
    return {"status": "success", "amount": total}
