"""An addition input module for adding the first contact,
    his phone number, email, address, birthday
    """

from handlers import (
    add_contact,
    add_phone_to_contact,
    add_email_to_contact,
    add_address_to_contact,
    add_birthday_to_contact,
    add_birthday,
    add_tag,
    add_tags,
    remove_tag,
    remove_tags,
    edit_tag,
    note_tags,
)

from ..validations import (
    input_name_validation,
    input_number_validation,
    input_email_validation,
    input_address_validation,
    input_birthday_validation,
    input_tag_validation,
)


def add_contact_input(book):
    """An addition input module for adding the first contact,
    his phone number, email, address, birthday

        Args:
            book (class): class AddressBook that contains all contacts
    """

    while True:
        user_input = input("Enter contact's name: ").lower()
        if input_name_validation(user_input):
            contact_name = user_input
            print(add_contact(contact_name, book))
            break
        print("The name must contain at least one symbol")

    while True:
        user_input = input("Enter contact's phone number: ").lower()
        if input_number_validation(user_input):
            contact_phone = user_input
            args = [contact_name, contact_phone]
            print(add_phone_to_contact(args, book))
            break
        print("The phone number must contain 10 only numbers")

    while True:
        y_n_input = input("Do you want to add email y/n: ").lower()
        if y_n_input == "y" or y_n_input == "n":
            if y_n_input == "y":
                while True:
                    user_input = input("Enter contact's email: ").lower()
                    if input_email_validation(user_input):
                        contact_email = user_input
                        args = [contact_name, contact_email]
                        print(add_email_to_contact(args, book))
                        break
                    print("Email format: email@email.com")
                break
            break

    while True:
        y_n_input = input("Do you want to add address y/n: ").lower()
        if y_n_input == "y" or y_n_input == "n":
            if y_n_input == "y":
                while True:
                    user_input = input("Enter contact's address: ").lower()
                    if input_address_validation(user_input):
                        contact_address = user_input
                        args = [contact_name, contact_address]
                        print(add_address_to_contact(args, book))
                        break
                    print("Address must contain at least one symbol")
                break
            break

    while True:
        y_n_input = input("Do you want to add birthday y/n: ").lower()
        if y_n_input == "y" or y_n_input == "n":
            if y_n_input == "y":
                while True:
                    user_input = input("Enter contact's birthday: ").lower()
                    if input_birthday_validation(user_input):
                        contact_birthday = user_input
                        args = [contact_name, contact_birthday]
                        print(add_birthday_to_contact(args, book))
                        break
                    print("Invalid date format. Use DD.MM.YYYY")
                break
            break

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