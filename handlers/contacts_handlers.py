"""A module for working with a list of contacts:
adding, editing, outputting, deleting."""

from helpers.assistant_info import table_show
from helpers import custom_print, command_logger
from classes import AddressBook, Record, ContactTableFormatter

from .decorators import empty_contact_list, input_error

table_headers = ["Name", "Contact info"]


@input_error
def add_contact(name, book: AddressBook):
    """Adds a new contact to the contact list.

    Args:
        args (list): contains name and phone number
        book (class): contact list

    Returns:
        str: message that the contact has been added or updated
    """
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    return message


@empty_contact_list
@input_error
def change_contact(args, book: AddressBook):
    """Changes a contact's phone number by the name

    #     Args:
    #         args (list): contains name, old phone number and new phone number
    #         book (class): contact list

    #     Returns:
    #         str: notification that the contact has been changed, or contact not found
    #"""
    name, old_number, new_number, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError(f"No such name '{name}' was found")
    record.edit_phone(old_number, new_number)
    return "Phone changed"


@empty_contact_list
@input_error
def show_phone(args, book: AddressBook):
    """Shows a contact information

    Args:
        args (list): contains name and phone number
        book (class): contact list

    Returns:
        str: a message with information about the contact,
        or that the contact was not found
    """
    name, *_ = args
    if name:
        record = book.find(name)
        if record is None:
            custom_print(
                command_logger,
                "Contact with name {name} haven't found",
                space="top",
                level="warning",
                name=("bright_cyan", name),
            )
            raise KeyError()
        custom_print(
            command_logger,
            "{record}",
            space="top",
            level="info",
            record=("green", record),
        )
    else:
        custom_print(
            command_logger,
            "The name must contain at least one symbol",
            space="top",
            level="warning",
        )


@empty_contact_list
def show_all(book: AddressBook):
    """Shows all contacts in the list

    Args:
        contacts (dict): contact list

    Returns:
        str: message with a list of contacts
    """
    headers = ["Address Book"]
    print(table_show(headers, book.data.items()))


@empty_contact_list
@input_error
def delete_contact(args, book: AddressBook):
    """Function to delete one contact or all at once

    Args:
        args (list): contains name and phone number
        book (class): contact list

    Returns:
        str: message about deleting one or all contacts
    """
    name, *_ = args
    record = book.find(name)
    if record:
        book.delete(name)
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("green", "Contact has been deleted"),
        )
        return

    if name == "all":
        book.data.clear()
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("green", "All contacts have been deleted"),
        )
        return
    custom_print(
        command_logger,
        "The {name} is not found",
        space="top",
        level="warning",
        name=("bright_magenta", name),
    )
    return


@empty_contact_list
@input_error
def search_contact(args, book: AddressBook):
    """Search a contact in the book by name, phone or email

    Args:
        * args (list): contains name, phone number or email

    Returns:
        * record: founded contact or warning message
    """
    search_string, *_ = args
    search_string = search_string.strip()

    # find by name
    records_by_name_generator = book.find_by_name(search_string)
    formatted_contacts = ContactTableFormatter.format_contacts(
        records_by_name_generator
    )
    if len(formatted_contacts) > 0:
        print(table_show(table_headers, formatted_contacts))
        return

    # find by phone
    records_by_phone_generator = book.find_by_phone(search_string)
    formatted_contacts = ContactTableFormatter.format_contacts(
        records_by_phone_generator
    )
    if len(formatted_contacts) > 0:
        print(table_show(table_headers, formatted_contacts))
        return

    # find by email
    records_by_email_generator = book.find_by_email(search_string)
    formatted_contacts = ContactTableFormatter.format_contacts(
        records_by_email_generator
    )
    if len(formatted_contacts) > 0:
        print(table_show(table_headers, formatted_contacts))
        return

    # find by address
    records_by_address_generator = book.find_by_address(search_string)
    formatted_contacts = ContactTableFormatter.format_contacts(
        records_by_address_generator
    )
    if len(formatted_contacts) > 0:
        print(table_show(table_headers, formatted_contacts))
        return

    # find by birthday
    records_by_birthday_generator = book.find_by_birthday(search_string)
    formatted_contacts = ContactTableFormatter.format_contacts(
        records_by_birthday_generator
    )
    if len(formatted_contacts) > 0:
        print(table_show(table_headers, formatted_contacts))
        return

    custom_print(
        command_logger,
        "No contact with data '{search}' was found",
        space="top",
        level="warning",
        search=("bright_cyan", search_string),
    )


@input_error
def add_email_to_contact(args, book: AddressBook):
    """Function to add email to contact

    Args:
        args (list): contains name and email
        book (class): contact list

    Returns:
        str: message email added
    """
    name, email, *_ = args
    record = book.find(name)
    if record:
        record.add_email(email)
        return "Email added"
    else:
        return f"There is no contact {name}"


@empty_contact_list
@input_error
def add_phone_to_contact(args, book: AddressBook):
    """Function to add phone to contact

    Args:
        args (list): contains name and phone number
        book (class): contact list

    Returns:
        str: message phone added
    """
    name, number, *_ = args
    record = book.find(name)
    if record:
        record.add_phone(number)
        return "Phone added"
    else:
        return f"There is no contact {name}"


@empty_contact_list
@input_error
def add_address_to_contact(args, book: AddressBook):
    """Function to add address to contact

    Args:
        args (list): contains name and address
        book (class): contact list

    Returns:
        str: message address added
    """
    name, *address = args
    if len(address) == 1:
        address_for_record = address[0]
    else:
        address_for_record = ""
        for world in address:
            address_for_record += f"{world} "
    record = book.find(name)
    if record:
        record.add_address(address_for_record)
        return "Address added"
    else:
        return f"There is no contact {name}"
