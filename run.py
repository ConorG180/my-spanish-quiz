"""
This is where the quix runs from
It contains the main function, which
builds the quiz object and runs the quiz."""

from quiz_class import Quiz


def main():
    """
    This main function is what runs the quiz from start to finish.
    It builds a quiz object from input collected from user and
    also validates user input via the quiz object."""
    print("Hello there! Welcome to the Spanish quiz!\n")
    print("So, what's your name?\n")
    while True:
        name = input("Enter your name below here:\n")
        if Quiz.validate_user_name(name):
            break
    print(f"Hi {name}!")
    print(
        f"So {name}, what level of difficulty would you like\n"
        f"to play at?"
    )
    while True:
        diff_level = input(
            'Enter "e" for easy, "m" for medium, or "h" for hard\n'
        )
        if Quiz.validate_diff(diff_level):
            break


main()
