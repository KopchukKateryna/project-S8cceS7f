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
    {"command": "all-notes", "usage": "all-notes", "exmp": "all-notes"},
    {
        "command": "add-tag",
        "usage": "add-tag <note-name> <tag>",
        "exmp": "add-tag todo @task",
    },
    {
        "command": "remove-tag",
        "usage": "remove-tag <note_name> <tag>",
        "exmp": "remove-tag todo @task",
    },
    {
        "command": "edit-tag",
        "usage": "edit-tag <note-name> <old_tag> <new_tag>",
        "exmp": "edit-tag todo @task @list",
    },
    {
        "command": "all-tags-by-note-name",
        "usage": "all-tags-by-note-name <note-name> ",
        "exmp": "all-tags-by-note-name todo",
    },
    {
        "command": "all-tags",
        "usage": "all-tags",
        "exmp": "all-tags",
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
