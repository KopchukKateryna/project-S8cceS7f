from prompt_toolkit import prompt
from handlers import (
    add_note,
    delete_contact,
    parse_input,
    show_all,
    show_birthday,
    show_phone,
    show_upcoming_birthdays,
    show_all_notes,
    search_contact,
    add_contact_input,
    edit_contact_input,
    edit_note,
    remove_note,
    find_note,
    add_tag_input,
    add_tags_input,
    all_tags,
    remove_tag_input,
    remove_tags_input,
    edit_tag_input,
    search_note_tags,
    sort_by_tag_input,
    edit_bot_name,
)
from helpers import (
    load_data,
    save_data,
    load_notes,
    save_notes,
    bindings_general,
    table_show,
    welcome,
    good_bye,
    display_ascii_welcome_art,
    load_bot_name,
    save_bot_name,
)
from constants import (
    ADDRESSBOOK_INFO_TABLE_DATA,
    ADDRESSBOOK_INFO_TABLE_HEADERS,
    NOTEBOOK_INFO_TABLE_DATA,
    NOTEBOOK_INFO_TABLE_HEADERS,
    COMPLETER,
)


def main():
    """The main function of the bot, manages the main cycle of command processing"""
    try:
        book = load_data()
        notes_book = load_notes()
        bot_name = load_bot_name()
        welcome(bot_name)
        while True:
            user_input = prompt(
                "Enter a command: > ",
                completer=COMPLETER,
                complete_while_typing=True,
                key_bindings=bindings_general,
                multiline=True,
            )
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                save_data(book)
                save_notes(notes_book)
                save_bot_name(bot_name)
                good_bye()
                break

            if command == "hello":
                print("How can I help you?")

            elif command == "info":
                print(
                    table_show(
                        ADDRESSBOOK_INFO_TABLE_HEADERS,
                        ADDRESSBOOK_INFO_TABLE_DATA,
                        True,
                    )
                )
                print(
                    table_show(
                        NOTEBOOK_INFO_TABLE_HEADERS, NOTEBOOK_INFO_TABLE_DATA, True
                    )
                )

            elif command == "info-addressbook":
                print(
                    table_show(
                        ADDRESSBOOK_INFO_TABLE_HEADERS,
                        ADDRESSBOOK_INFO_TABLE_DATA,
                        True,
                    )
                )

            elif command == "info-notebook":
                print(
                    table_show(
                        NOTEBOOK_INFO_TABLE_HEADERS, NOTEBOOK_INFO_TABLE_DATA, True
                    )
                )

            elif command == "add-note":
                print(add_note(notes_book))

            elif command == "edit-tag":
                edit_tag_input(notes_book)

            elif command == "add-contact":
                add_contact_input(book)
                save_data(book, "addressbook.pkl", False)
                print("Contact saved!")

            elif command == "edit-contact":
                edit_contact_input(args, book)
                save_data(book, "addressbook.pkl", False)
                print("Contact updated!")

            elif command == "phone":
                print(show_phone(args, book))

            elif command == "all-contacts":
                print(show_all(book))

            elif command == "all-notes":
                print(show_all_notes(notes_book))

            elif command == "search-note":
                print(find_note(notes_book))

            elif command == "remove-note":
                note_name = " ".join(args).strip()
                print(remove_note(note_name, notes_book))

            elif command == "all-tags":
                print(all_tags(notes_book))

            elif command == "note-tags":
                search_note_tags(notes_book)

            elif command == "delete":
                print(delete_contact(args, book))

            elif command == "remove-tag":
                remove_tag_input(notes_book)

            elif command == "remove-tags":
                remove_tags_input(notes_book)

            elif command == "add-tag":
                add_tag_input(notes_book)

            elif command == "add-tags":
                add_tags_input(notes_book)
            elif command == "edit-note":
                print(edit_note(notes_book))

            elif command == "delete-note":
                note_name = " ".join(args).strip()
                print(remove_note(note_name, notes_book))

            elif command == "delete-contact":
                print(delete_contact(args, book))

            elif command == "show-birthday":
                print(show_birthday(args, book))

            elif command == "birthdays":
                print(show_upcoming_birthdays(book))

            elif command == "search-contact":
                print(search_contact(args, book))

            elif command == "sort-by-tag":
                sort_by_tag_input(notes_book)

            elif command == "edit-bot-name":
                new_bot_name = edit_bot_name(bot_name)
                save_bot_name(new_bot_name)
                print(f"Bot name {new_bot_name} saved.")
                good_bye()
                break

            else:
                print("Invalid command.")
    except KeyboardInterrupt:
        save_data(book)
        save_notes(notes_book)
        save_bot_name(bot_name="NONAME BOT")
        display_ascii_welcome_art("Good bye")


if __name__ == "__main__":
    main()
