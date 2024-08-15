"""A common function that shows possible bot commands in table view."""

from tabulate import tabulate


def table_show(headers, data):
    """Show data in table view."""
    return tabulate(
        data,
        headers,
        tablefmt="mixed_grid",
        stralign="left",
    )
