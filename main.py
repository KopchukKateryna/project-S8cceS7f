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
    custom_print,
    command_logger,
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
            custom_print(
                command_logger,
                "{msg}",
                space="top",
                level="info",
                msg=(
                    "cyan",
                    "Enter a command:",
                ),
            )
            user_input = prompt(
                ">> ",
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
                custom_print(
                    command_logger,
                    "{msg}",
                    level="info",
                    space="top",
                    msg=(
                        "magenta",
                        "How can I help you?",
                    ),
                )

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
                # done
                add_note(notes_book)

            elif command == "edit-tag":
                # done
                edit_tag_input(notes_book)

            elif command == "add-contact":
                # done
                add_contact_input(book)
                save_data(book, "addressbook.pkl", False)

            elif command == "edit-contact":
                edit_contact_input(args, book)
                save_data(book, "addressbook.pkl", False)
                # print("Contact updated!")

            elif command == "phone":
                # done
                show_phone(args, book)

            elif command == "all-contacts":
                # done
                print(show_all(book))

            elif command == "all-notes":
                # done
                print(show_all_notes(notes_book))

            elif command == "search-note":
                # done
                find_note(notes_book)

            elif command == "all-tags":
                # done
                print(all_tags(notes_book))

            elif command == "note-tags":
                # done
                search_note_tags(notes_book)

            elif command == "remove-tag":
                # done
                remove_tag_input(notes_book)

            elif command == "remove-tags":
                # done add to commands
                remove_tags_input(notes_book)

            elif command == "add-tag":
                # done
                add_tag_input(notes_book)

            elif command == "add-tags":
                # done
                add_tags_input(notes_book)

            elif command == "edit-note":
                # done
                edit_note(notes_book)

            elif command == "delete-note":
                # done
                note_name = " ".join(args).strip()
                remove_note(note_name, notes_book)

            elif command == "delete-contact":
                print(delete_contact(args, book))

            elif command == "show-birthday":
                # done
                show_birthday(args, book)

            elif command == "birthdays":
                # done
                show_upcoming_birthdays(book)

            elif command == "search-contact":
                print(search_contact(args, book))

            elif command == "sort-by-tag":
                # done
                sort_by_tag_input(notes_book)

            elif command == "edit-bot-name":
                new_bot_name = edit_bot_name(bot_name)
                save_bot_name(new_bot_name)
                print(f"Bot name {new_bot_name} saved.")
                good_bye()
                break

            else:
                custom_print(
                    command_logger,
                    "Invalid command",
                    space="top",
                    level="warning",
                )
    except KeyboardInterrupt:
        save_data(book)
        save_notes(notes_book)
        save_bot_name(bot_name="NONAME BOT")
        display_ascii_welcome_art("Good bye")


if __name__ == "__main__":
    main()
