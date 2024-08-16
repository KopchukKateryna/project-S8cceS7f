"""An addition input module for adding the first contact,
    his phone number, email, address, birthday
    """

from handlers import (
    add_tag,
    add_tags,
    remove_tag,
    remove_tags,
    edit_tag,
    note_tags,
)

from ..validations import (
    input_name_validation,
    input_tag_validation,
)

def add_tag_input(book):
    while True:
        note = input("Enter note name: ").lower()
        if input_name_validation(note):
            tag = input("Enter tag: ").lower()
            if input_tag_validation(tag):
                print(add_tag(note, tag, book))
                break
            else:
                print("Invalid tag name. Use #aaa")
                break
        else:
            print("The name must contain at least one symbol")

def add_tags_input(book):
    while True:
        note = input("Enter note name: ").lower()
        if input_name_validation(note):
            tags = input("Enter tags separate by white splace: ").lower()
            if input_tag_validation(tags):
                args = [note, tags]
                print(add_tags(args, book))
                break
            else:
                print("Invalid tag format. You need input at least 1 tag(exp. #aaa)")
                break
        else:
            print("The name must contain at least one symbol")

def remove_tag_input(book):
    while True:
        note = input("Enter note name: ").lower()
        if input_name_validation(note):
            tag = input("Enter tag: ").lower()
            if input_tag_validation(tag):
                print(remove_tag(note, tag, book))
                break
            else:
                print("Invalid tag name. Use #aaa")
                break
        else:
            print("The name must contain at least one symbol")

def remove_tags_input(book):
    while True:
        note = input("Enter note name: ").lower()
        if input_name_validation(note):
            tags = input("Enter tags separate by white splace: ").lower()
            if input_tag_validation(tags):
                args = [note, tags]
                print(remove_tags(args, book))
                break
            else:
                print("Invalid tag format. You need input at least 1 tag(exp. #aaa)")
                break
        else:
            print("The name must contain at least one symbol")

def edit_tag_input(book):
    while True:
        note = input("Enter note name: ").lower()
        if input_name_validation(note):
            old_tag = input("Enter old tag: ").lower()
            if input_tag_validation(old_tag):
               new_tag = input("Enter new tag: ").lower()
               if input_tag_validation(new_tag):
                    print(edit_tag(note, old_tag, new_tag, book))
                    break
               else:
                    print("Invalid tag name. Use #aaa")
                    break
            else:
                print("Invalid tag name. Use #aaa")
                break
        else:
            print("The name must contain at least one symbol")

def search_note_tags(book):
    while True:
        note = input("Enter note name: ").lower()
        if input_name_validation(note):
            print(note_tags(note, book))
            break
        else:
            print("The name must contain at least one symbol")    