from prompt_toolkit import prompt
from constants import COMPLETER_FOR_EDIT_DELETE
from helpers import bindings_for_edit_delete, custom_print, command_logger
from ..validations import (
    input_name_validation,
    input_number_validation,
    input_email_validation,
    input_address_validation,
    input_birthday_validation,
)

from .fields_handlers import (
    edit_name,
    add_phone,
    edit_phone,
    delete_phone,
    add_email,
    edit_email,
    delete_email,
    add_address,
    edit_address,
    delete_address,
    add_birthday,
    edit_birthday,
    delete_birthday,
)


def edit_phone_in_contacts(old_phone, record):
    """Asks to input new phone for edit_phone function

    Args:
        old_phone (str): phone number to edit
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter new phone number: "),
        )
        new_phone = input(">> ").lower().strip()
        if input_number_validation(new_phone):
            msg = edit_phone(old_phone, new_phone, record)
            custom_print(
                command_logger,
                "{msg}",
                space="top",
                level="info",
                msg=("green", msg),
            )
            break
        custom_print(
            command_logger,
            "The phone number must contain 10 only numbers",
            space="top",
            level="warning",
        )


def edit_email_in_contacts(record):
    """Asks to input new email for edit_email function

    Args:
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter new email: "),
        )
        new_email = input(">> ").lower().strip()
        if input_email_validation(new_email):
            msg = edit_email(new_email, record)
            custom_print(
                command_logger,
                "{msg}",
                space="top",
                level="info",
                msg=("green", msg),
            )
            break
        custom_print(
            command_logger,
            "Email format should be email@email.com",
            space="top",
            level="warning",
        )


def edit_address_in_contacts(record):
    """Asks to input new address for edit_address function

    Args:
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter new address: "),
        )
        new_address = input(">> ").lower()
        if input_address_validation(new_address):
            msg = edit_address(new_address, record)
            custom_print(
                command_logger,
                "{msg}",
                space="top",
                level="info",
                msg=("green", msg),
            )
            break
        custom_print(
            command_logger,
            "Address must contain at least one symbol",
            space="top",
            level="warning",
        )


def edit_birthday_in_contacts(record):
    """Asks to input new birthday for edit_birthday function

    Args:
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter new birthday: "),
        )
        new_birthday = input("Enter new birthday: ").lower()
        if input_birthday_validation(new_birthday):
            msg = edit_birthday(new_birthday, record)
            custom_print(
                command_logger,
                "{msg}",
                space="top",
                level="info",
                msg=("green", msg),
            )
            break
        custom_print(
            command_logger,
            "Invalid date format. Use DD.MM.YYYY.",
            space="top",
            level="warning",
        )


def edit_name_in_contacts(old_name, record, book):
    """Asks to input new name for edit_name function

    Args:
        old_name (str): old name of contact
        record (object): record of current contact
        book (class): class AddressBook that contains all contacts
    """
    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter a new contact's name: "),
        )
        new_name = input(">> ").lower()
        if input_name_validation(new_name):
            msg = edit_name(old_name, new_name, record, book)
            custom_print(
                command_logger,
                "{msg}",
                space="top",
                level="info",
                msg=("green", msg),
            )
            break
        custom_print(
            command_logger,
            "The name must contain at least one symbol.",
            space="top",
            level="warning",
        )


def add_phone_action(record):
    """Asks to enter phone number to add. Check if number already exist.
    Proposes 'edit or delete phone' if exist. Adds phone if not exist.

    Args:
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter phone number to add: "),
        )
        number = input(">> ").lower().strip()
        if input_number_validation(number):
            number_in_contacts = record.find_phone(number)
            if number_in_contacts:
                custom_print(
                    command_logger,
                    "Number {number} already exist.",
                    space="top",
                    level="warning",
                    number=("bright_cyan", number),
                )
                edit_or_delete_phone_choise(number, record)
                break
            msg = add_phone(number, record)
            custom_print(
                command_logger,
                "{msg}",
                space="top",
                level="info",
                msg=("green", msg),
            )
            break
        custom_print(
            command_logger,
            "The phone number must contain 10 only numbers",
            space="top",
            level="warning",
        )


def edit_phone_action(record):
    """Asks to enter phone number to edit. Check if number already exist.
    Proposes 'add or not phone' if not exist, or 'edit or delete phone' if exist

    Args:
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter phone number to edit: "),
        )
        old_phone = input(">> ").lower().strip()
        if input_number_validation(old_phone):
            number_in_contacts = record.find_phone(old_phone)
            if not number_in_contacts:
                custom_print(
                    command_logger,
                    "Number {phone} has not found.",
                    space="top",
                    level="warning",
                    phone=("bright_cyan", old_phone),
                )
                add_or_not_phone_choise(old_phone, record)
                break
            edit_or_delete_phone_choise(old_phone, record)
            break
        custom_print(
            command_logger,
            "The phone number must contain 10 only numbers.",
            space="top",
            level="warning",
        )


def delete_phone_action(record):
    """Asks to enter phone number to delete. Check if number already exist.
    Prints message if not exist, or deletes phone if exist

    Args:
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter phone number to delete: "),
        )
        number = input(">> ").lower().strip()
        if input_number_validation(number):
            number_in_contacts = record.find_phone(number)
            if not number_in_contacts:
                custom_print(
                    command_logger,
                    "Number {number} has not found.",
                    space="top",
                    level="warning",
                    number=("bright_cyan", number),
                )
                break
            delete_phone(number, record)
            break
        custom_print(
            command_logger,
            "The phone number must contain 10 only numbers.",
            space="top",
            level="warning",
        )


def add_email_action(record):
    """Asks to enter email to add for add_email function.

    Args:
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter email to add: "),
        )
        email = input(">> ").lower().strip()
        if input_email_validation(email):
            msg = add_email(email, record)
            custom_print(
                command_logger,
                "{msg}",
                space="top",
                level="info",
                msg=("green", msg),
            )
            break
        custom_print(
            command_logger,
            "Email format should be email@email.com",
            space="top",
            level="warning",
        )


def add_address_action(record):
    """Asks to enter address to add for add_address fonction.

    Args:
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter address to add: "),
        )
        address = input(">> ").lower()
        if input_address_validation(address):
            msg = add_address(address, record)
            custom_print(
                command_logger,
                "{msg}",
                space="top",
                level="info",
                msg=("green", msg),
            )
            break
        custom_print(
            command_logger,
            "Address must contain at least one symbol.",
            space="top",
            level="warning",
        )


def add_birthday_action(record):
    """Asks to enter birthday to add for add_birthday fonction.

    Args:
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter birthday to add: "),
        )
        birthday = input(">> ").lower().strip()
        if input_birthday_validation(birthday):
            msg = add_birthday(birthday, record)
            custom_print(
                command_logger,
                "{msg}",
                space="top",
                level="info",
                msg=("green", msg),
            )
            break
        custom_print(
            command_logger,
            "Invalid date format. Use DD.MM.YYYY.",
            space="top",
            level="warning",
        )


def edit_or_delete_phone_choise(number, record):
    """Asks 'Do you want to edit or delete' phone number.
    If 'edit': moves to edit_phone_in_contacts().
    If 'delete: delete_phone()

    Args:
        number (str): phone number to edit or delete
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "Do you want to {edit} or {delete} it? ",
            space="top",
            level="info",
            edit=("bright_magenta"),
            delete=("bright_magenta"),
        )
        edit_or_delete_input = prompt(
            ">> ",
            completer=COMPLETER_FOR_EDIT_DELETE,
            complete_while_typing=True,
            key_bindings=bindings_for_edit_delete,
            multiline=True,
        )
        if edit_or_delete_input in ["edit", "delete"]:
            if edit_or_delete_input == "edit":
                edit_phone_in_contacts(number, record)
                break
            if edit_or_delete_input == "delete":
                delete_phone(number, record)
                break


def add_or_not_phone_choise(number, record):
    """Asks 'Do you want to add' phone number to contact.
    If yes: add_phone().

    Args:
        old_phone (str): phone number to edit
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "Do you want to add it {y}/{n} ?: ",
            space="top",
            level="info",
            y=("bright_magenta"),
            n=("bright_magenta"),
        )
        y_or_n = input(">> ").lower().strip()
        if y_or_n == "y" or y_or_n == "n":
            if y_or_n == "y":
                msg = add_phone(number, record)
                custom_print(
                    command_logger,
                    "{msg}",
                    space="top",
                    level="info",
                    msg=("green", msg),
                )
                break
            break


def edit_or_delete_email_choise(record):
    """Asks 'Do you want to edit or delete' email.
    If 'edit': moves to edit_email_in_contacts().
    If 'delete: delete_email()

    Args:
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "Do you want to {edit} or {delete} it? ",
            space="top",
            level="info",
            edit=("bright_magenta"),
            delete=("bright_magenta"),
        )
        edit_or_delete_input = prompt(
            ">> ",
            completer=COMPLETER_FOR_EDIT_DELETE,
            complete_while_typing=True,
            key_bindings=bindings_for_edit_delete,
            multiline=True,
        )
        if edit_or_delete_input in ["edit", "delete"]:
            if edit_or_delete_input == "edit":
                edit_email_in_contacts(record)
                break
            msg = delete_email(record)
            custom_print(
                command_logger,
                "{msg}",
                space="top",
                level="info",
                msg=("green", msg),
            )
            break


def add_or_not_email_choise(record):
    """Asks 'Do you want to add' email to contact.
    If yes: moves to add_email_action().

    Args:
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "Do you want to add it? {y}/{n}: ",
            space="top",
            level="info",
            y=("bright_magenta"),
            n=("bright_magenta"),
        )
        y_or_n = input(">> ").lower().strip()
        if y_or_n == "y" or y_or_n == "n":
            if y_or_n == "y":
                add_email_action(record)
                break
            break


def edit_or_delete_address_choise(record):
    """Asks 'Do you want to edit or delete' address.
    If 'edit': moves to edit_address_in_contacts().
    If 'delete: delete_address()

    Args:
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "Do you want to edit or delete it? {edit}/{delete}: ",
            space="top",
            level="info",
            edit=("bright_magenta"),
            delete=("bright_magenta"),
        )
        edit_or_delete_input = prompt(
            ">> ",
            completer=COMPLETER_FOR_EDIT_DELETE,
            complete_while_typing=True,
            key_bindings=bindings_for_edit_delete,
            multiline=True,
        )
        if edit_or_delete_input in ["edit", "delete"]:
            if edit_or_delete_input == "edit":
                edit_address_in_contacts(record)
                break
            msg = delete_address(record)
            custom_print(
                command_logger,
                "{msg}",
                space="top",
                level="info",
                msg=("green", msg),
            )
            break


def add_or_not_address_choise(record):
    """Asks 'Do you want to add' address to contact.
    If yes: moves to add_address_action().

    Args:
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "Do you want to add it? {y}/{n}: ",
            space="top",
            level="info",
            y=("bright_magenta"),
            n=("bright_magenta"),
        )
        y_or_n = input(">> ").lower().strip()
        if y_or_n == "y" or y_or_n == "n":
            if y_or_n == "y":
                add_address_action(record)
                break
            break


def edit_or_delete_birthday_choise(record):
    """Asks 'Do you want to edit or delete' birthday.
    If 'edit': moves to edit_birthday_in_contacts().
    If 'delete: delete_birthday()

    Args:
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "Do you want to edit or delete it? {edit}/{delete}: ",
            space="top",
            level="info",
            edit=("bright_magenta"),
            delete=("bright_magenta"),
        )
        edit_or_delete_input = prompt(
            ">> ",
            completer=COMPLETER_FOR_EDIT_DELETE,
            complete_while_typing=True,
            key_bindings=bindings_for_edit_delete,
            multiline=True,
        )
        if edit_or_delete_input in ["edit", "delete"]:
            if edit_or_delete_input == "edit":
                edit_birthday_in_contacts(record)
                break
            msg = delete_birthday(record)
            custom_print(
                command_logger,
                "{msg}",
                space="top",
                level="info",
                msg=("green", msg),
            )
            break


def add_or_not_birthday_choise(record):
    """Asks 'Do you want to add' birthday to contact.
    If yes: moves to add_birthday_action().

    Args:
        record (oblect): record of current contact
    """
    while True:
        custom_print(
            command_logger,
            "Do you want to add it? {y}/{n}: ",
            space="top",
            level="info",
            y=("bright_magenta"),
            n=("bright_magenta"),
        )
        y_or_n = input(">> ").lower().strip()
        if y_or_n == "y" or y_or_n == "n":
            if y_or_n == "y":
                add_birthday_action(record)
                break
            break
