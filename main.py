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
from helpers.assistant_info import assistant_info
from helpers.pickle_utils import load_data, save_data
from classes import NotesBook

logger = setup_logging()


def main():
    """The main function of the bot, manages the main cycle of command processing"""
    book = load_data()
    print("Welcome to the assistant bot!")
    print(
        (
            "The table below summarizes information about the commands. "
            "But if you forget something in the process, just call the 'info' command "
            "and you will see this table again."
        )
    )
    print(assistant_info())
    print()

    notes_book = NotesBook()

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break

        if command == "hello":
            print("How can I help you?")

        elif command == "info":
            print(assistant_info())

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

        elif command == "all":
            print(show_all(book))

        elif command == "all-notes":
            print(show_all_notes(notes_book))

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

        elif command == "search":
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
