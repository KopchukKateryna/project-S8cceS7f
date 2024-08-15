from prompt_toolkit import prompt
from handlers import (
    add_birthday,
    add_note,
    change_contact,
    delete_contact,
    parse_input,
    show_all,
    show_birthday,
    show_phone,
    show_upcoming_birthdays,
    show_all_notes,
    search_contact,
    add_email_to_contact,
    add_phone_to_contact,
    add_address_to_contact,
    add_contact_input,
    edit_note,
    remove_note,
    find_note,
    add_tag,
    add_tags,
    edit_tag,
    remove_tag,
    remove_tags,
    all_tags,
    all_tags_by_note_name,
    notes_by_tag
)
from helpers import setup_logging
from helpers import (
    load_data,
    save_data,
    load_notes,
    save_notes,
    bindings,
    table_show,
    welcome,
    good_bye,
)
from constants import (
    ADDRESSBOOK_INFO_TABLE_DATA,
    ADDRESSBOOK_INFO_TABLE_HEADERS,
    NOTEBOOK_INFO_TABLE_DATA,
    NOTEBOOK_INFO_TABLE_HEADERS,
    COMPLETER,
)

logger = setup_logging()


def main():
    """The main function of the bot, manages the main cycle of command processing"""
    book = load_data()
    notes_book = load_notes()
    welcome()
    while True:
        user_input = prompt(
            "Enter a command: > ",
            completer=COMPLETER,
            complete_while_typing=True,
            key_bindings=bindings,
            multiline=True,
        )
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            save_notes(notes_book)
            good_bye()
            break

        if command == "hello":
            print("How can I help you?")

        elif command == "info":
            print(
                table_show(
                    ADDRESSBOOK_INFO_TABLE_HEADERS, ADDRESSBOOK_INFO_TABLE_DATA, True
                )
            )
            print(
                table_show(NOTEBOOK_INFO_TABLE_HEADERS, NOTEBOOK_INFO_TABLE_DATA, True)
            )

        elif command == "info-addressbook":
            print(
                table_show(
                    ADDRESSBOOK_INFO_TABLE_HEADERS, ADDRESSBOOK_INFO_TABLE_DATA, True
                )
            )

        elif command == "info-notebook":
            print(
                table_show(NOTEBOOK_INFO_TABLE_HEADERS, NOTEBOOK_INFO_TABLE_DATA, True)
            )

        elif command == "add-note":
            print(add_note(notes_book))

        elif command == "add-contact":
            add_contact_input(book)

        elif command == "change":
            print(change_contact(args, book))
        
        elif command == "edit-tag":
            print(edit_tag(args, notes_book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all-contacts":
            print(show_all(book))

        elif command == "all-notes":
            print(show_all_notes(notes_book))

        elif command == "find-note":
            print(find_note(notes_book))

        elif command == "edit-note":
            print(edit_note(notes_book))

        elif command == "remove-note":
            note_name = " ".join(args).strip()
            print(remove_note(note_name, notes_book))
        elif command == "all-tags":
            print(all_tags(notes_book))
        
        elif command == "note-tags":
            print(all_tags_by_note_name(args, notes_book))

        elif command == "notes-by-tag":
            print(notes_by_tag(args, notes_book))

        elif command == "delete":
            print(delete_contact(args, book))
        
        elif command == "remove-tag":
            print(remove_tag(args, notes_book))

        elif command == "remove-tags":
            print(remove_tags(args, notes_book))

        elif command == "add-birthday":
            print(add_birthday(args, book))
        
        elif command == "add-tag":
            print(add_tag(args, notes_book))
        
        elif command == "add-tags":
            print(add_tags(args, notes_book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(show_upcoming_birthdays(book))

        elif command == "search-contact":
            print(search_contact(args, book))

        elif command == "add-phone":
            print(add_phone_to_contact(args, book))

        elif command == "add-email":
            print(add_email_to_contact(args, book))

        elif command == "add-address":
            print(add_address_to_contact(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
