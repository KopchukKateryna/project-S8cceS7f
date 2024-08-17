import pyfiglet
import time
import sys

team_name = "NO NAME BOT"
bye_msg = "SEE YOU LATER"


def display_ascii_welcome_art(msg: str):
    """Display a welcome message in ASCII art.

    Args:
        msg (str) - The message to display.
    """
    ascii_art = pyfiglet.figlet_format(msg, font="big")
    print(ascii_art)


def live_print(text, delay=0.05):
    """Print text to the console with a delay.

    Args:
        text (str) - The text to print.
        delay (float) - The delay between each character in seconds.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def create_bot_name():
    """Creates the name of the main bot

    Returns:
        str: bot name in string format
    """
    bot_name = input(">>> ").upper()
    return bot_name


def pre_wellcome():
    """Display a first welcome message and ASCII art."""
    time.sleep(0.4)
    display_ascii_welcome_art("NONAME BOT")
    live_print("Welcome to the NONAME BOT.\n")
    live_print("Your private contact-book and note-book.\n")
    live_print("Make it personal.\n")
    live_print("Enter the name for your bot:\n")
    bot_name = create_bot_name()
    time.sleep(0.4)
    display_ascii_welcome_art("wellcome")
    time.sleep(0.4)
    display_ascii_welcome_art(bot_name)
    live_print("Preparing your environment...\n")
    live_print(f"Initializing {bot_name}...\n")
    time.sleep(0.2)
    live_print("Loading your Contact Book...\n")
    time.sleep(0.4)
    live_print("Loading your NoteBook...\n")
    time.sleep(0.3)
    live_print("Setup complete!\n")
    return bot_name


def welcome(bot_name):
    """Display a welcome message."""
    time.sleep(0.4)
    live_print(f"\nWelcome to the {bot_name}!\n")


def good_bye():
    """Display a good bye message and ASCII art."""
    live_print("Saving your Contact Book...\n")
    time.sleep(0.2)
    live_print("Saving your NoteBook...\n")
    time.sleep(0.3)

    display_ascii_welcome_art(bye_msg)
    live_print("Goodbye!\n")


if __name__ == "__main__":
    welcome()
    good_bye()
    pre_wellcome()
