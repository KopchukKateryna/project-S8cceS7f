import pyfiglet
import time
import sys

team_name = "NO NAME BOT"
bye_msg = "SEE YOU LATER"


def display_ascii_welcome_art(msg: str):
    ascii_art = pyfiglet.figlet_format(msg, font="big")
    print(ascii_art)


def live_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def welcome():
    display_ascii_welcome_art(team_name)

    live_print(f"Welcome to the {team_name}.\n")
    live_print("Preparing your environment...\n")
    live_print(f"Initializing {team_name}...\n")
    time.sleep(0.2)
    live_print("Loading your Contact Book...\n")
    time.sleep(0.4)
    live_print("Loading your NoteBook...\n")
    time.sleep(0.3)
    live_print("Setup complete!\n")


def good_bye():
    live_print("Saving your Contact Book...\n")
    time.sleep(0.2)
    live_print("Saving your NoteBook...\n")
    time.sleep(0.3)

    display_ascii_welcome_art(bye_msg)
    live_print("Goodbye!\n")


if __name__ == "__main__":
    welcome()
    good_bye()
