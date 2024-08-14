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
)

from handlers.notes_handlers import (
    add_note,
    show_all_notes,
    find_note,
)
from handlers.parse_input import parse_input

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
    "find_note",
]
