from dataclasses import dataclass


@dataclass
class ContactBase:
    name: str
    phone: str | None
    email: str | None


@dataclass
class Contact(ContactBase):
    id: int
    created_at: str


@dataclass
class ContactCreate(ContactBase):
    pass
