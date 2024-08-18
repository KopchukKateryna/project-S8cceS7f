"""birthday handlers"""

from helpers import table_show, custom_print, command_logger

from classes import AddressBook

from .decorators import input_error


@input_error
def add_birthday_to_contact(args, book: AddressBook):
    """Adds a birthday to the contact.

    Args:
        args (list): contains name and birthday
        book (class): contact list

    Returns:
        str: message that the birthday has been added to contact
    """
    name, date, *_ = args
    record = book.find(name)
    if record:
        record.add_birthday(date)
        return "Birthday added"
    else:
        return f"There is no contact {name}"


@input_error
def show_birthday(args, book: AddressBook):
    """Shows a birthday of the contact.

    Args:
        args (list): contains name
        book (class): contact list

    Returns:
        str: message that shows contact name and birthday
    """
    name, *_ = args
    record = book.find(name)
    if record:
        if not record.birthday:
            custom_print(
                command_logger,
                "There is no birthday for contact {name}",
                space="top",
                level="warning",
                name=("bright_cyan", name),
            )
        else:
            msg = f"{name}'s birthday: {record.birthday}"
            custom_print(
                command_logger,
                "{msg}",
                space="top",
                level="info",
                msg=("green", msg),
            )

    else:
        custom_print(
            command_logger,
            "Contact with name {name} haven't found.",
            space="top",
            level="warning",
            name=("bright_cyan", name),
        )


@input_error
def show_upcoming_birthdays(book: AddressBook):
    """Shows all contacts with congratulations dates for the next X days.

    Args:
        book (AddressBook): contact list.

    Returns:
        str: message with a list of contacts with congratulations dates.
    """
    try:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=(
                "cyan",
                "Type the number of days from today to check for upcoming birthdays:",
            ),
        )
        days = int(input(">> ").strip())
    except ValueError:
        custom_print(
            command_logger,
            "Invalid input! Please enter a valid number of days.",
            space="top",
            level="warning",
        )
        return

    upcoming_birthdays = book.get_upcoming_birthdays(days)

    if len(upcoming_birthdays) == 0:
        custom_print(
            command_logger,
            "No contacts that need to be congratulated within the specified period.",
            space="top",
            level="warning",
        )
        return

    headers = ["Name", "Congratulation date"]
    table_data = [
        [key["name"], key["congratulation_date"]] for key in upcoming_birthdays
    ]
    print(table_show(headers, table_data))
