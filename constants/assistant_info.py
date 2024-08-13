"""!!!NEEDS CHANGES!!!!"""

BOT_COMMANDS = [
    {"command": "hello", "usage": "hello", "exmp": "hello"},
    {"command": "info", "usage": "info", "exmp": "info"},
    {"command": "add", "usage": "add <name> <number>", "exmp": "add bob 1234567890"},
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
        "usage": "add note <name> <text>",
        "exmp": "add-note todo test",
    },
    {"command": "all-notes", "usage": "all notes", "exmp": "all-notes"},
    {
        "command": "search",
        "usage": "search <name/phone/email>",
        "exmp": "search bob",
    },
]

ASSISTANT_INFO_TABLE_HEADERS = ["COMMAND", "USAGE", "EXAMPLE"]
ASSISTANT_INFO_TABLE_DATA = [
    [c["command"], c["usage"], c["exmp"]] for c in BOT_COMMANDS
]
