from dataclasses import asdict
from datetime import datetime

from contacts.models import Contact, ContactCreate
from contacts.storage import load_contacts, save_contacts


def add_contact(contact: ContactCreate):
    contacts = load_contacts()

    created_at = datetime.now().__str__()
    new_contact = Contact(**asdict(contact), id=len(contacts), created_at=created_at)
    contacts.append(asdict(new_contact))

    save_contacts(contacts)

