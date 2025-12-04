from datetime import datetime

import ulid

from contacts.storage import load_contacts, save_contacts
from contacts.utils import is_valid_email, is_valid_phone


def add_contact(
    name: str, phone: str | None, email: str | None
) -> None | dict[str, str | None]:
    if phone and not is_valid_phone(phone):
        print("Invalid phone, must not be empty!")
        return None

    if email and not is_valid_email(email):
        print("Invalid email!")
        return None

    contacts = load_contacts()

    new_contact = {
        "id": str(ulid.new()),
        "name": name,
        "phone": phone,
        "email": email,
        "created_at": datetime.now().__str__(),
    }

    contacts.append(new_contact)
    save_contacts(contacts)

    return new_contact


def search_contacts(query: str):
    contacts = load_contacts()
    found = [c for c in contacts if query.lower() in str(c["name"]).lower()]
    return found


def print_contacts(contacts: list[dict[str, str | None]]):
    if len(contacts) == 0:
        return

    row_format = " %-26s | %-20s | %-15s | %s "
    print(row_format % ("Id", "Name", "Phone", "Email"))

    for c in contacts:
        print(row_format % (c["id"], c["name"], c["phone"], c["email"]))


def delete_contact(id: str) -> bool:
    contacts = load_contacts()
    index = next((i for i, c in enumerate(contacts) if c["id"] == id), -1)

    if index <= -1:
        return False

    del contacts[index]
    save_contacts(contacts)
    return True
