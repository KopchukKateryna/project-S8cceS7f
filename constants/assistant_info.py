"""!!!NEEDS CHANGES!!!!"""

BOT_COMMANDS = [
    {"command": "hello", "usage": "hello", "exmp": "hello"},
    {"command": "info", "usage": "info", "exmp": "info"},
    {"command": "add-contact", "usage": "add-contact", "exmp": "add-contact"},
    {
        "command": "change",
        "usage": "change <name> <old_number> <new_number>",
        "exmp": "change bob 1234567890 0987654321",
    },
    {
        "command": "phone",
        "usage": "phone <name>",
        "exmp": "phone bob",
    },
    {
        "command": "delete",
        "usage": "delete <name> OR delete all",
        "exmp": "delete bob OR delete all",
    },
    {"command": "all", "usage": "all", "exmp": "all"},
    {
        "command": "add-birthday",
        "usage": "add-birthday <name> <birthday>",
        "exmp": "add-birthday bob 12.12.1221",
    },
    {
        "command": "show-birthday",
        "usage": "show-birthday <name>",
        "exmp": "show-birthday bob",
    },
    {"command": "birthdays", "usage": "birthdays", "exmp": "birthdays"},
    {"command": "close", "usage": "close", "exmp": "close"},
    {"command": "exit", "usage": "exit", "exmp": "exit"},
    {
        "command": "add-note",
        "usage": "add-note <name> <text>",
        "exmp": "add-note todo test",
    },
    {"command": "all-notes", "usage": "all notes", "exmp": "all-notes"},
    {
        "command": "search",
        "usage": "search <name/phone/email>",
        "exmp": "search bob",
    },
    {
        "command": "add-phone",
        "usage": "add-phone <name> <phone>",
        "exmp": "add-phone bob 1111111111",
    },
    {
        "command": "add-email",
        "usage": "add-email <name> <email>",
        "exmp": "add-email bob email@gmail.com",
    },
    {
        "command": "add-address",
        "usage": "add-address <name> <address>",
        "exmp": "add-address bob some address",
    },
]

ASSISTANT_INFO_TABLE_HEADERS = ["COMMAND", "USAGE", "EXAMPLE"]
ASSISTANT_INFO_TABLE_DATA = [
    [c["command"], c["usage"], c["exmp"]] for c in BOT_COMMANDS
]


ADDRESSBOOK_COMMANDS = [
    {"command": "hello", "usage": "hello", "exmp": "hello", "desc": "Greets the user."},
    {"command": "info", "usage": "info", "exmp": "info",
        "desc": "Provides general information about the address book and the notebook commands."},
    {"command": "info-addressbook", "usage": "info-addressbook",
        "exmp": "info-addressbook", "desc": "Displays information about the address book."},
    {"command": "add-contact", "usage": "add-contact", "exmp": "add-contact",
        "desc": "Adds a new contact to the address book."},
    {
        "command": "change",
        "usage": "change <name> <old_number> <new_number>",
        "exmp": "change bob 1234567890 0987654321",
        "desc": "Changes the phone number of an existing contact."
    },
    {
        "command": "delete",
        "usage": "delete <name> OR delete all",
        "exmp": "delete bob OR delete all",
        "desc": "Deletes a specific contact or all contacts from the address book."
    },
    {
        "command": "phone",
        "usage": "phone <name>",
        "exmp": "phone bob",
        "desc": "Displays the phone number of the specified contact."
    },
    {
        "command": "add-phone",
        "usage": "add-phone <name> <phone>",
        "exmp": "add-phone bob 1111111111",
        "desc": "Adds a phone number to an existing contact."
    },
    {
        "command": "add-email",
        "usage": "add-email <name> <email>",
        "exmp": "add-email bob email@gmail.com",
        "desc": "Adds an email address to an existing contact."
    },
    {
        "command": "add-address",
        "usage": "add-address <name> <address>",
        "exmp": "add-address bob some address",
        "desc": "Adds a physical address to an existing contact."
    },
    {
        "command": "search",
        "usage": "search <name/phone/email>",
        "exmp": "search bob",
        "desc": "Searches for a contact by name, phone number, or email address."
    },
    {
        "command": "add-birthday",
        "usage": "add-birthday <name> <birthday>",
        "exmp": "add-birthday bob 12.12.1221",
        "desc": "Adds a birthday to an existing contact."
    },
    {
        "command": "show-birthday",
        "usage": "show-birthday <name>",
        "exmp": "show-birthday bob",
        "desc": "Displays the birthday of the specified contact."
    },
    {"command": "birthdays", "usage": "birthdays",
        "exmp": "birthdays", "desc": "Lists all upcoming birthdays."},
    {"command": "all", "usage": "all", "exmp": "all",
        "desc": "Displays all contacts in the address book."},
    {"command": "close", "usage": "close", "exmp": "close",
        "desc": "Saving Addressbook data and closes the application."},
    {"command": "exit", "usage": "exit", "exmp": "exit",
        "desc": "Exits the address book application."},
]

ADDRESSBOOK_INFO_TABLE_HEADERS = ["COMMAND", "USAGE", "EXAMPLE", "DESCRIPTION"]
ADDRESSBOOK_INFO_TABLE_DATA = [
    [c["command"], c["usage"], c["exmp"], c["desc"]] for c in ADDRESSBOOK_COMMANDS
]

NOTEBOOK_COMMANDS = [
    {"command": "hello", "usage": "hello", "exmp": "hello", "desc": "Greets the user."},
    {"command": "info", "usage": "info", "exmp": "info",
        "desc": "Provides general information about the address book and the notebook commands."},
    {"command": "info-notebook", "usage": "info-notebook", "exmp": "info-notebook",
        "desc": "Displays information about the notebook."},
    {
        "command": "add-note",
        "usage": "add-note",
        "exmp": "add-note",
        "desc": "Adds a new note with the specified name and text."
    },
    {"command": "all-notes", "usage": "all notes", "exmp": "all-notes",
        "desc": "Displays all notes in the notebook."},
    {"command": "close", "usage": "close", "exmp": "close",
        "desc": "Saving Addressbook data and closes the application."},
    {"command": "exit", "usage": "exit", "exmp": "exit",
        "desc": "Exits the address book application."},
]

NOTEBOOK_INFO_TABLE_HEADERS = ["COMMAND", "USAGE", "EXAMPLE", "DESCRIPTION"]
NOTEBOOK_INFO_TABLE_DATA = [
    [c["command"], c["usage"], c["exmp"], c["desc"]] for c in NOTEBOOK_COMMANDS
]
