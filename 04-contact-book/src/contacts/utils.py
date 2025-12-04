import re


def is_valid_email(email: str) -> bool:
    return re.match(r"^[^@]+@[^@\s]+\.[^@\s]+$", email) is not None


def is_valid_phone(phone: str) -> bool:
    return len(phone.strip()) > 0
