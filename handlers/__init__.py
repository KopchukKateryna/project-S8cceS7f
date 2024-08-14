"""This module provides handler functions for parsing input, managing contacts,
and handling birthdays."""

from handlers.birthday_handlers import (
    add_birthday,
    show_birthday,
    show_upcoming_birthdays,
)

from handlers.contacts_handlers import (
    add_contact,
    change_contact,
    delete_contact,
    show_all,
    show_phone,
    search_contact,
    add_email_to_contact,
    add_phone_to_contact,
    add_address_to_contact,
)

from handlers.notes_handlers import (
    add_note,
    show_all_notes,
)
from handlers.parse_input import parse_input
from handlers.input_handlers import add_contact_input

from handlers.validations import (
    input_name_validation,
    input_number_validation,
    input_email_validation,
    input_address_validation,
    input_birthday_validation,
)

__all__ = [
    "parse_input",
    "add_contact",
    "change_contact",
    "show_all",
    "show_phone",
    "delete_contact",
    "add_birthday",
    "show_birthday",
    "show_upcoming_birthdays",
    "add_note",
    "show_all_notes",
    "search_contact",
    "add_email_to_contact",
    "add_phone_to_contact",
    "add_address_to_contact",
    "add_contact_input",
    "input_name_validation",
    "input_number_validation",
    "input_email_validation",
    "input_address_validation",
    "input_birthday_validation",
]
