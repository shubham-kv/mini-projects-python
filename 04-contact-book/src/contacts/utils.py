import re


def is_valid_email(email: str):
    return re.match(r"^[^@]+@[^@\s]+\.[^@\s]+$", email) is not None


def is_valid_phone(phone: str):
    return phone.isdigit()
