import argparse

from contacts.core import add_contact
from contacts.models import ContactCreate


def build_arg_parser():
    parser = argparse.ArgumentParser(
        description="Manage your contacts - add, search & delete."
    )
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add new contact")
    add_parser.add_argument("name", type=str, help="Contact Name")
    add_parser.add_argument("--phone", type=str, help="Contact Phone number")
    add_parser.add_argument("--email", type=str, help="Contact Email")

    return parser


def main():
    arg_parser = build_arg_parser()
    args = arg_parser.parse_args()

    if args.command == "add":
        contact = ContactCreate(name=args.name, phone=args.phone, email=args.email)
        add_contact(contact)
        return

    print(arg_parser.format_help())
