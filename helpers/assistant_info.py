"""A common function that shows possible bot commands in table view."""

from tabulate import tabulate

from constants import ASSISTANT_INFO_TABLE_DATA, ASSISTANT_INFO_TABLE_HEADERS


def assistant_info():
    """
    A function that shows all info about bot commands.
    """
    return tabulate(
        ASSISTANT_INFO_TABLE_DATA,
        ASSISTANT_INFO_TABLE_HEADERS,
        tablefmt="mixed_grid",
        stralign="left",
    )
