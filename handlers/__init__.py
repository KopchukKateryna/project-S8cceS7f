"""This module provides handler functions for parsing input, managing contacts,
and handling birthdays."""

from handlers.parse_input import parse_input
from handlers.contacts_handlers import (
    add_contact,
    change_contact,
    show_all,
    show_phone,
    delete_contact
    )
from handlers.birthday_handlers import (
    add_birthday,
    show_birthday,
    show_upcoming_birthdays
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
    "show_upcoming_birthdays"
    ]
