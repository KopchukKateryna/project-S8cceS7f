"""An addition input module to add, change, delete fields
such as name, phone number, email, address, birthday
    """

from prompt_toolkit import prompt
from constants import COMPLETER_FOR_EDIT
from constants import COMPLETER_FOR_ADD_EDIT_DELETE
from helpers import (
    bindings_for_contact,
    bindings_for_add_edit_delete,
    custom_print,
    command_logger,
)
from ..decorators import input_error
from .inputs_helpers import (
    edit_name_in_contacts,
    add_phone_action,
    edit_phone_action,
    delete_phone_action,
    edit_or_delete_email_choise,
    add_or_not_email_choise,
    edit_or_delete_address_choise,
    add_or_not_address_choise,
    edit_or_delete_birthday_choise,
    add_or_not_birthday_choise,
)


@input_error
def edit_contact_input(args, book):
    """An addition input module to add, change, delete fields
    such as name, phone number, email, address, birthday

        Args:
            args (list): list of input arguments from main()
            book (class): class AddressBook that contains all contacts

        Raises:
            KeyError: No record in address book
    """
    record = None
    name, *_ = args
    record = book.find(name)
    if record is None:
        custom_print(
            command_logger,
            "No such name '{name}' was found",
            space="top",
            level="warning",
            name=("bright_cyan", name),
        )
        return
    while True:
        custom_print(
            command_logger,
            (
                "What field do you want to edit: "
                "{name} | {phones} | {email} | {address} | {birthday} | {exit}: "
            ),
            space="top",
            level="info",
            name=("bright_magenta"),
            phones=("bright_magenta"),
            email=("bright_magenta"),
            address=("bright_magenta"),
            birthday=("bright_magenta"),
            exit=("magenta"),
        )
        field_to_edit = prompt(
            ">> ",
            completer=COMPLETER_FOR_EDIT,
            complete_while_typing=True,
            key_bindings=bindings_for_contact,
            multiline=True,
        )
        if field_to_edit in ["name", "phones", "email", "address", "birthday"]:

            if field_to_edit == "name":
                edit_name_in_contacts(name, record, book)
                break

            if field_to_edit == "phones":
                while True:
                    custom_print(
                        command_logger,
                        (
                            "You can {add}, {edit}, {delete} phone, or {exit}. "
                            "What do you want to do?"
                        ),
                        space="top",
                        level="info",
                        add=("bright_magenta"),
                        edit=("bright_magenta"),
                        delete=("bright_magenta"),
                        exit=("magenta"),
                    )
                    action = prompt(
                        ">> ",
                        completer=COMPLETER_FOR_ADD_EDIT_DELETE,
                        complete_while_typing=True,
                        key_bindings=bindings_for_add_edit_delete,
                        multiline=True,
                    )
                    if action in ["add", "edit", "delete"]:
                        if action == "add":
                            add_phone_action(record)
                            break
                        if action == "edit":
                            edit_phone_action(record)
                            break
                        if action == "delete":
                            delete_phone_action(record)
                            break
                    if action == "exit":
                        break
                    break
                break

            if field_to_edit == "email":
                while True:
                    if record.email:
                        edit_or_delete_email_choise(record)
                        break
                    custom_print(
                        command_logger,
                        "Contact {name} has no email yet.",
                        space="top",
                        level="warning",
                        name=("bright_cyan", name),
                    )
                    add_or_not_email_choise(record)
                    break
                break

            if field_to_edit == "address":
                while True:
                    if record.address:
                        edit_or_delete_address_choise(record)
                        break
                    custom_print(
                        command_logger,
                        "Contact {name} has no address yet.",
                        space="top",
                        level="warning",
                        name=("bright_cyan", name),
                    )
                    add_or_not_address_choise(record)
                    break
                break

            if field_to_edit == "birthday":
                while True:
                    if record.birthday:
                        edit_or_delete_birthday_choise(record)
                        break
                    custom_print(
                        command_logger,
                        "Contact {name} has no birthday yet.",
                        space="top",
                        level="warning",
                        name=("bright_cyan", name),
                    )
                    add_or_not_birthday_choise(record)
                    break
                break
        elif field_to_edit == "exit":
            break

        else:
            custom_print(
                command_logger,
                "Command is wrong, if you don't want to edit something type: {exit}",
                space="top",
                level="warning",
                exit=("magenta"),
            )
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("green", "Contact updated!"),
        )
