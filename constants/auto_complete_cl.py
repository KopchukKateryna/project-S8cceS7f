from prompt_toolkit.completion import WordCompleter
from constants.assistant_info import NOTEBOOK_COMMANDS, ADDRESSBOOK_COMMANDS

notebook_commands = [c["command"] for c in NOTEBOOK_COMMANDS]
addressbook_commands = [c["command"] for c in ADDRESSBOOK_COMMANDS]

COMBINED_BOT_COMMANDS = list(set(notebook_commands + addressbook_commands))

COMMAND_CORRECTIONS = {
    # "hello"
    "hlelo": "hello",
    "hleloo": "hello",
    "helol": "hello",
    "helo": "hello",
    "ello": "hello",
    "hllo": "hello",
    # "info"
    "nifo": "info",
    "ifno": "info",
    "inof": "info",
    "infor": "info",
    "inffo": "info",
    "infro": "info",
    "ino": "info",
    # "info-addressbook"
    "info addressbook": "info-addressbook",
    "info-adressbook": "info-addressbook",
    "info-adressbok": "info-addressbook",
    "info-adresbook": "info-addressbook",
    "info-addresbook": "info-addressbook",
    "info-addressbokk": "info-addressbook",
    # "add-contact"
    "add contact": "add-contact",
    "ad-contact": "add-contact",
    "add-contct": "add-contact",
    "add-cnotact": "add-contact",
    "add-cotnact": "add-contact",
    "add-contatc": "add-contact",
    # "change"
    "chagne": "change",
    "cahnge": "change",
    "chang": "change",
    "chnage": "change",
    "chaneg": "change",
    "changee": "change",
    # "delete"
    "delte": "delete",
    "delee": "delete",
    "deltee": "delete",
    "dellete": "delete",
    "deelte": "delete",
    # "phone"
    "phne": "phone",
    "phoe": "phone",
    "pone": "phone",
    "phon": "phone",
    "phoen": "phone",
    "phnone": "phone",
    # "add-phone"
    "add phone": "add-phone",
    "ad-phone": "add-phone",
    "add-phne": "add-phone",
    "add-phoen": "add-phone",
    "add-phnone": "add-phone",
    "add-ponhe": "add-phone",
    # "add-email"
    "add email": "add-email",
    "ad-email": "add-email",
    "add-emal": "add-email",
    "add-emial": "add-email",
    "add-emai": "add-email",
    "add-emaiil": "add-email",
    # "add-address"
    "add address": "add-address",
    "ad-address": "add-address",
    "add-adress": "add-address",
    "add-adres": "add-address",
    "add-adrress": "add-address",
    "add-addess": "add-address",
    # "search"
    "serach": "search",
    "saerch": "search",
    "searh": "search",
    "sech": "search",
    "saech": "search",
    "searc": "search",
    # "add-birthday"
    "add birthday": "add-birthday",
    "ad-birthday": "add-birthday",
    "add-birtday": "add-birthday",
    "add-birthay": "add-birthday",
    "add-birhday": "add-birthday",
    # "show-birthday"
    "show birthday": "show-birthday",
    "shwo-birthday": "show-birthday",
    "show-birtday": "show-birthday",
    "show-birthay": "show-birthday",
    "show-birhday": "show-birthday",
    # "birthdays"
    "birtday": "birthdays",
    "birtdays": "birthdays",
    "brithdays": "birthdays",
    "birthdys": "birthdays",
    "brthdays": "birthdays",
    "birthdayss": "birthdays",
    # "all"
    "al": "all",
    "aall": "all",
    "alll": "all",
    "lla": "all",
    # "info-notebook"
    "info notebook": "info-notebook",
    "info-notebokk": "info-notebook",
    "info-notebok": "info-notebook",
    "info-notbok": "info-notebook",
    "info-noteboook": "info-notebook",
    # "add-note"
    "add note": "add-note",
    "ad-note": "add-note",
    "add-not": "add-note",
    "add-noet": "add-note",
    "add-nte": "add-note",
    "add-nnote": "add-note",
    # "edit-note"
    "edit note": "edit-note",
    "edit-noet": "edit-note",
    "edit-not": "edit-note",
    "eddit-note": "edit-note",
    "edit-nte": "edit-note",
    "edit-ntoe": "edit-note",
    # "remove-note"
    "remove note": "remove-note",
    "remov-note": "remove-note",
    "remove-not": "remove-note",
    "remoe-note": "remove-note",
    "remvoe-note": "remove-note",
    # "find-note"
    "find note": "find-note",
    "fidn-note": "find-note",
    "find-not": "find-note",
    "find-noet": "find-note",
    "finnd-note": "find-note",
    "fin-note": "find-note",
    # "all-notes"
    "all notes": "all-notes",
    "all-noets": "all-notes",
    "al-notes": "all-notes",
    "all-nots": "all-notes",
    "alll-notes": "all-notes",
    # "close"
    "clsoe": "close",
    "cose": "close",
    "clsose": "close",
    "cloose": "close",
    "cloe": "close",
    # "exit"
    "exi": "exit",
    "exitt": "exit",
    "exti": "exit",
    "eixt": "exit",
    "exiit": "exit",
}

COMPLETER = WordCompleter(COMBINED_BOT_COMMANDS, ignore_case=True, sentence=True)
