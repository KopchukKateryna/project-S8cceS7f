from constants.assistant_info import (
    NOTEBOOK_COMMANDS,
    ADDRESSBOOK_COMMANDS,
    COMMAND_EDIT_CONTACT,
)
from classes import CustomWordCompleter

notebook_commands = [c["command"] for c in NOTEBOOK_COMMANDS]
addressbook_commands = [c["command"] for c in ADDRESSBOOK_COMMANDS]
edit_contact_commands = [c["command"] for c in COMMAND_EDIT_CONTACT]

COMBINED_BOT_COMMANDS = list(set(notebook_commands + addressbook_commands))

COMMAND_CORRECTIONS = {
    # "hello"
    "hl": "hello",
    "hlelo": "hello",
    "hleloo": "hello",
    "helol": "hello",
    "helo": "hello",
    "ello": "hello",
    "hllo": "hello",
    # "info"
    "if": "info",
    "nifo": "info",
    "ifno": "info",
    "inof": "info",
    "infor": "info",
    "inffo": "info",
    "infro": "info",
    "ino": "info",
    # "info-addressbook"
    "iab": "info-addressbook",
    "info addressbook": "info-addressbook",
    "info-adressbook": "info-addressbook",
    "info-adressbok": "info-addressbook",
    "info-adresbook": "info-addressbook",
    "info-addresbook": "info-addressbook",
    "info-addressbokk": "info-addressbook",
    # "add-contact"
    "adc": "add-contact",
    "add contact": "add-contact",
    "ad-contact": "add-contact",
    "add-contct": "add-contact",
    "add-cnotact": "add-contact",
    "add-cotnact": "add-contact",
    "add-contatc": "add-contact",
    # "delete-contact"
    "dc": "delete-contact",
    "delete contact": "delete-contact",
    "delte-contact": "delete-contact",
    "delee-contact": "delete-contact",
    "deltee-contact": "delete-contact",
    "dellete-contact": "delete-contact",
    "deelte-contact": "delete-contact",
    # "phone"
    "p": "phone",
    "phne": "phone",
    "phoe": "phone",
    "pone": "phone",
    "phon": "phone",
    "phoen": "phone",
    "phnone": "phone",
    # "search-contact"
    "sc": "search-contact",
    "search contact": "search-contact",
    "serch-contact": "search-contact",
    "seach-contact": "search-contact",
    "sarch-contact": "search-contact",
    "searh-contact": "search-contact",
    "searc-contact": "search-contact",
    # "show-birthday"
    "sb": "show-birthday",
    "show birthday": "show-birthday",
    "shwo-birthday": "show-birthday",
    "show-birtday": "show-birthday",
    "show-birthay": "show-birthday",
    "show-birhday": "show-birthday",
    # "birthdays"
    "b": "birthdays",
    "birtday": "birthdays",
    "birtdays": "birthdays",
    "brithdays": "birthdays",
    "birthdys": "birthdays",
    "brthdays": "birthdays",
    "birthdayss": "birthdays",
    # "all"
    "alc": "all-contacts",
    "all contacts": "all-contacts",
    "all-contcts": "all-contacts",
    "al-cntacts": "all-contacts",
    "all-contact": "all-contacts",
    "alll-contacts": "all-contacts",
    # "info-notebook"
    "in": "info-notebook",
    "info notebook": "info-notebook",
    "info-notebokk": "info-notebook",
    "info-notebok": "info-notebook",
    "info-notbok": "info-notebook",
    "info-noteboook": "info-notebook",
    # "add-note"
    "adn": "add-note",
    "add note": "add-note",
    "ad-note": "add-note",
    "add-not": "add-note",
    "add-noet": "add-note",
    "add-nte": "add-note",
    "add-nnote": "add-note",
    # "edit-note"
    "edn": "edit-note",
    "edit note": "edit-note",
    "edit-noet": "edit-note",
    "edit-not": "edit-note",
    "eddit-note": "edit-note",
    "edit-nte": "edit-note",
    "edit-ntoe": "edit-note",
    # "delete-note"
    "dn": "delete-note",
    "delte-note": "delete-note",
    "delee-note": "delete-note",
    "deltee-note": "delete-note",
    "dellete-note": "delete-note",
    "deelte-note": "delete-note",
    # "search-note"
    "sn": "search-note",
    "serch-note": "search-note",
    "seach-note": "search-note",
    "sarch-note": "search-note",
    "searh-note": "search-note",
    "searc-note": "search-note",
    # "all-notes"
    "aln": "all-notes",
    "all notes": "all-notes",
    "all-noets": "all-notes",
    "al-notes": "all-notes",
    "all-nots": "all-notes",
    "alll-notes": "all-notes",
    # "close"
    "cl": "close",
    "clsoe": "close",
    "cose": "close",
    "clsose": "close",
    "cloose": "close",
    "cloe": "close",
    # "exit"
    "ex": "exit",
    "exi": "exit",
    "exitt": "exit",
    "exti": "exit",
    "eixt": "exit",
    "exiit": "exit",
}

COMMAND_FOR_EDIT_CONTACT = {
    # "name"
    "n": "name",
    "name": "name",
    "anme": "name",
    "nm": "name",
    # "phones"
    "p": "phones",
    "ps": "phones",
    "ph": "phones",
    "phones": "phones",
    "hpones": "phones",
    # "email"
    "e": "email",
    "em": "email",
    "eml": "email",
    "meail": "email",
    "email": "email",
    # "address"
    "adr": "address",
    "ad": "address",
    "adress": "address",
    "adres": "address",
    "address": "address",
    # "birthday"
    "b": "birthday",
    "birthday": "birthday",
    "br": "birthday",
    "bith": "birthday",
    "birt": "birthday",
    "bd": "birthday",
    # "exit"
    "ex": "exit",
    "exi": "exit",
    "exitt": "exit",
    "exti": "exit",
    "eixt": "exit",
    "exiit": "exit",
}

COMPLETER = CustomWordCompleter(
    COMBINED_BOT_COMMANDS, COMMAND_CORRECTIONS, ignore_case=True
)
COMPLETER_FOR_EDIT = CustomWordCompleter(
    edit_contact_commands, COMMAND_FOR_EDIT_CONTACT, ignore_case=True
)
