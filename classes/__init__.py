"""All classes of the bot are collected here"""

from classes.address_book import AddressBook
from classes.record import Record
from classes.notes_book import NotesBook
from classes.note import Note
from classes.contact_table_formatter import ContactTableFormatter
from classes.custom_word_completer import CustomWordCompleter

__all__ = [
    "AddressBook",
    "Record",
    "NotesBook",
    "Note",
    "ContactTableFormatter",
    "CustomWordCompleter",
]
