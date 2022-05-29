"""
This is where the quix runs from
It contains the main function, which
builds the quiz object and runs the quiz."""

from quiz_class import Quiz
from grade_class import Grade


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
    print(
        f"Thank you {name}, you have chosen the "
        f"{Quiz.print_difficulty(diff_level)} level\n"
        f"And finally, how many words do you want in your quiz?\n"
        f"Please note, the maxiumum amount is 100 words."
    )
    while True:
        word_count = input(
            "Enter the number of words you want to be tested on\n"
            "below this statement. Your number should be from 1 - 100\n"
        )
        if Quiz.validate_word_count(word_count):
            break
    print(
        f"Thank you {name}! We will now begin your quiz"
    )
    user_quiz = Quiz(name, diff_level, word_count)
    user_quiz.play()
    score = user_quiz.get_score()
    user_grade = Grade(score, int(word_count))
    user_grade.assign_grade()
    user_grade.print_grade()


main()
