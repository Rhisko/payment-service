import hashlib

def weak_hash(pwd: str) -> str:
    # INTENTIONAL VULNERABILITY
    return hashlib.md5(pwd.encode()).hexdigest()
