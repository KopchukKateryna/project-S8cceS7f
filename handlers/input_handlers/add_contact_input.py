"""An addition input module for adding the first contact,
    his phone number, email, address, birthday
    """

from helpers import custom_print, command_logger
from handlers import (
    add_contact,
    add_phone_to_contact,
    add_email_to_contact,
    add_address_to_contact,
    add_birthday_to_contact,
)

from ..validations import (
    input_name_validation,
    input_number_validation,
    input_email_validation,
    input_address_validation,
    input_birthday_validation,
)


def add_contact_input(book):
    """An addition input module for adding the first contact,
    his phone number, email, address, birthday

        Args:
            book (class): class AddressBook that contains all contacts
    """

    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter a contact's name: "),
        )
        user_input = input(">> ").lower().strip()
        if not input_name_validation(user_input):
            custom_print(
                command_logger,
                "The name must contain at least one symbol.",
                space="top",
                level="warning",
            )
            continue
        contact_name = user_input
        if not book.find(contact_name):
            msg = add_contact(contact_name, book)
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
            "Contact {name} already exists.",
            space="top",
            level="warning",
            name=("bright_cyan", contact_name),
        )

    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter contact's phone number: "),
        )
        user_input = input(">> ").lower().strip()
        if input_number_validation(user_input):
            contact_phone = user_input
            args = [contact_name, contact_phone]
            msg = add_phone_to_contact(args, book)
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
            "The phone number must contain 10 only numbers.",
            space="top",
            level="warning",
        )

    while True:
        custom_print(
            command_logger,
            "Do you want to add email {y}/{n}: ",
            space="top",
            level="info",
            y=("bright_magenta"),
            n=("bright_magenta"),
        )
        y_n_input = input(">> ").lower().strip()
        if y_n_input == "y" or y_n_input == "n":
            if y_n_input == "y":
                while True:
                    custom_print(
                        command_logger,
                        "{msg}",
                        space="top",
                        level="info",
                        msg=("cyan", "Please, enter contact's email: "),
                    )
                    user_input = input(">> ").lower().strip()
                    if input_email_validation(user_input):
                        contact_email = user_input
                        args = [contact_name, contact_email]
                        msg = add_email_to_contact(args, book)
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
                break
            break

    while True:
        custom_print(
            command_logger,
            "Do you want to add address {y}/{n}: ",
            space="top",
            level="info",
            y=("bright_magenta"),
            n=("bright_magenta"),
        )
        y_n_input = input(">> ").lower().strip()
        if y_n_input == "y" or y_n_input == "n":
            if y_n_input == "y":
                while True:
                    custom_print(
                        command_logger,
                        "{msg}",
                        space="top",
                        level="info",
                        msg=("cyan", "Please, enter contact's address: "),
                    )
                    user_input = input(">> ").lower().strip()
                    if input_address_validation(user_input):
                        contact_address = user_input
                        args = [contact_name, contact_address]
                        msg = add_address_to_contact(args, book)
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
                break
            break

    while True:
        custom_print(
            command_logger,
            "Do you want to add birthday {y}/{n}: ",
            space="top",
            level="info",
            y=("bright_magenta"),
            n=("bright_magenta"),
        )
        y_n_input = input(">> ").lower().strip()
        if y_n_input == "y" or y_n_input == "n":
            if y_n_input == "y":
                while True:
                    custom_print(
                        command_logger,
                        "{msg}",
                        space="top",
                        level="info",
                        msg=("cyan", "Please, enter contact's birthday: "),
                    )
                    user_input = input(">> ").lower().strip()
                    if input_birthday_validation(user_input):
                        contact_birthday = user_input
                        args = [contact_name, contact_birthday]
                        msg = add_birthday_to_contact(args, book)
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
                break
            break
    custom_print(
        command_logger,
        "{msg}",
        space="top",
        level="info",
        msg=("green", "Contact saved!"),
    )
