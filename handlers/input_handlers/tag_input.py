"""An addition input module for adding the first contact,
    his phone number, email, address, birthday
    """

from helpers import custom_print, command_logger
from handlers import (
    add_tag,
    add_tags,
    remove_tag,
    remove_tags,
    edit_tag,
    note_tags,
    sort_by_tag,
)
from ..validations import (
    input_name_validation,
    input_tag_validation,
    input_note_validation,
)


def add_tag_input(book):
    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter the note name:"),
        )
        note = input(">> ").lower()
        if input_name_validation(note):
            if input_note_validation(note, book):
                custom_print(
                    command_logger,
                    "{msg}",
                    space="top",
                    level="info",
                    msg=("cyan", "Please, enter the tag:"),
                )
                tag = input(">> ").lower()
                if input_tag_validation(tag):
                    msg = add_tag(note, tag, book)
                    custom_print(
                        command_logger,
                        "{msg}",
                        space="top",
                        level="info",
                        msg=("green", msg),
                    )
                    break
                else:
                    custom_print(
                        command_logger,
                        "Invalid tag name. Use #tag_name",
                        space="top",
                        level="warning",
                    )
                    break
            else:
                custom_print(
                    command_logger,
                    "Note with name {note} haven't found",
                    space="top",
                    level="warning",
                    note=("bright_cyan", note),
                )
                break
        else:
            custom_print(
                command_logger,
                "The name must contain at least one symbol",
                space="top",
                level="warning",
            )


def add_tags_input(book):
    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter the note name:"),
        )
        note = input(">> ").lower()
        if input_name_validation(note):
            if input_note_validation(note, book):
                custom_print(
                    command_logger,
                    "{msg}",
                    space="top",
                    level="info",
                    msg=("cyan", "Type tags separate by white space: "),
                )
                tags = input(">> ").lower()
                if input_tag_validation(tags):
                    args = [note, tags]
                    msg = add_tags(args, book)
                    custom_print(
                        command_logger,
                        "{msg}",
                        space="top",
                        level="info",
                        msg=("green", msg),
                    )
                    break
                else:
                    custom_print(
                        command_logger,
                        "Invalid tag format. You need input at least 1 tag(exp. #dog)",
                        space="top",
                        level="warning",
                    )
                    break
            else:
                custom_print(
                    command_logger,
                    "Note with name {note} haven't found",
                    space="top",
                    level="warning",
                    note=("bright_cyan", note),
                )
                break
        else:
            custom_print(
                command_logger,
                "The name must contain at least one symbol",
                space="top",
                level="warning",
            )


def remove_tag_input(book):
    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter the note name:"),
        )
        note = input(">> ").lower()
        if input_name_validation(note):
            if input_note_validation(note, book):
                custom_print(
                    command_logger,
                    "{msg}",
                    space="top",
                    level="info",
                    msg=("cyan", "Please, type tag:"),
                )
                tag = input(">> ").lower()
                if input_tag_validation(tag):
                    msg = remove_tag(note, tag, book)
                    custom_print(
                        command_logger,
                        "{msg}",
                        space="top",
                        level="info",
                        msg=("green", msg),
                    )
                    break
                else:
                    custom_print(
                        command_logger,
                        "Invalid tag name. Use #tag_name",
                        space="top",
                        level="warning",
                    )
                    break
            else:
                custom_print(
                    command_logger,
                    "Note with name {note} haven't found",
                    space="top",
                    level="warning",
                    note=("bright_cyan", note),
                )
                break
        else:
            custom_print(
                command_logger,
                "The name must contain at least one symbol",
                space="top",
                level="warning",
            )


def remove_tags_input(book):
    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter the note name:"),
        )
        note = input(">> ").lower()
        if input_name_validation(note):
            if input_note_validation(note, book):
                custom_print(
                    command_logger,
                    "{msg}",
                    space="top",
                    level="info",
                    msg=("cyan", "Type tags separate by white space: "),
                )
                tags = input(">> ").lower()
                if input_tag_validation(tags):
                    args = [note, tags]
                    msg = remove_tags(args, book)
                    custom_print(
                        command_logger,
                        "{msg}",
                        space="top",
                        level="info",
                        msg=("green", msg),
                    )
                    break
                else:
                    custom_print(
                        command_logger,
                        "Invalid tag format. You need input at least 1 tag(exp. #dog)",
                        space="top",
                        level="warning",
                    )
                    break
            else:
                custom_print(
                    command_logger,
                    "Note with name {note} haven't found",
                    space="top",
                    level="warning",
                    note=("bright_cyan", note),
                )
                break
        else:
            custom_print(
                command_logger,
                "The name must contain at least one symbol",
                space="top",
                level="warning",
            )


def edit_tag_input(book):
    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter the note name:"),
        )
        note = input(">> ").lower()
        if input_name_validation(note):
            if input_note_validation(note, book):
                custom_print(
                    command_logger,
                    "{msg}",
                    space="top",
                    level="info",
                    msg=("cyan", "Please, enter a old tag:"),
                )
                old_tag = input(">> ").lower()
                if input_tag_validation(old_tag):
                    custom_print(
                        command_logger,
                        "{msg}",
                        space="top",
                        level="info",
                        msg=("cyan", "Please, enter a new tag:"),
                    )
                    new_tag = input(">> ").lower()
                    if input_tag_validation(new_tag):
                        msg = edit_tag(note, old_tag, new_tag, book)
                        custom_print(
                            command_logger,
                            "{msg}",
                            space="top",
                            level="info",
                            msg=("green", msg),
                        )
                        break
                    else:
                        custom_print(
                            command_logger,
                            "Invalid tag format. Use #tag_name",
                            space="top",
                            level="warning",
                        )
                        break
                else:
                    custom_print(
                        command_logger,
                        "Invalid tag format. Use #tag_name",
                        space="top",
                        level="warning",
                    )
                    break
            else:
                custom_print(
                    command_logger,
                    "Note with name {note} haven't found",
                    space="top",
                    level="warning",
                    note=("bright_cyan", note),
                )
                break
        else:
            custom_print(
                command_logger,
                "The name must contain at least one symbol",
                space="top",
                level="warning",
            )


def search_note_tags(book):
    while True:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter the note name:"),
        )
        note = input(">> ").lower()
        if input_name_validation(note):
            if input_note_validation(note, book):
                print(note_tags(note, book))
                break
            else:
                custom_print(
                    command_logger,
                    "Note with name {note} haven't found",
                    space="top",
                    level="warning",
                    note=("bright_cyan", note),
                )
                break
        else:
            custom_print(
                command_logger,
                "The name must contain at least one symbol",
                space="top",
                level="warning",
            )


def sort_by_tag_input(book):
    while True:
        custom_print(
            command_logger,
            "Type sort by {asc} or {desc}:",
            space="top",
            level="info",
            asc=("bright_magenta"),
            desc=("bright_magenta"),
        )
        sort = input(">> ").strip().lower()
        if sort == "asc" or sort == "desc":
            print(sort_by_tag(sort, book))
            break
        else:
            custom_print(
                command_logger,
                "Invalid sort option. Please type {asc} or {desc}",
                space="top",
                level="warning",
                asc=("bright_magenta"),
                desc=("bright_magenta"),
            )
