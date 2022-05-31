"""
This is a python module which contains the Quiz class.
We import this module from our run.py file
to create and run the quiz from there. """

import re
from easy_spanish_dict import easy_words
from medium_spanish_dict import medium_words
from hard_spanish_dict import hard_words
from grade_class import Grade
import random
from os import system, name, execv
from time import sleep
from sys import executable, argv


class Quiz:
    """ Create Quiz class """
    def __init__(self, user_name, difficulty_level, word_count):
        self.user_name = user_name
        self.difficulty_level = difficulty_level
        self.word_count = word_count
        self.score = 0

    @staticmethod
    def validate_user_name(name):
        """
        This method is used to validate the user's
        name once they enter it to to the terminal
        returns true/false to determine if while
        loop will continue or break"""
        try:
            if len(name) > 20:
                raise ValueError(
                    f"Your name {name} cannot be more than 20 characters!\n"
                    f"You entered {len(name)}!\n"
                )
            elif name.replace(" ", "").isalpha() is not True:
                raise ValueError(
                    f"Your name can only contain letters!\n"
                    f"No numbers or special characters allowed!\n"
                    f"You entered {name}.\n"
                )
        except ValueError as e:
            print(f"Invalid data:\n{e}Give it another go.")
            Quiz.clear_terminal(3.5)
            return False
        return True

    @staticmethod
    def validate_diff(level):
        """ 
        This method is used to validate the user's chosen
        difficulty level"""
        diff_regex = "^[e|m|h]{1}$"

        try:
            validity = re.search(diff_regex, level.lower())
            # Confirm user input contains only "e", "m", or "h"
            if bool(validity) is False or level.isalpha() is False:
                raise ValueError(
                    'You need to enter either "e", "m", or "h"\n'
                    'without any other characters.\n'
                )
        except ValueError as e:
            print(f"Invalid data: {e}Give it another go.")
            Quiz.clear_terminal(3)
            return False
        return True

    @staticmethod
    def print_difficulty(level):
        if level.lower() == "e":
            level = "easy"
        elif level.lower() == "m":
            level = "medium"
        else:
            level = "hard"
        return level
    
    @staticmethod
    def validate_word_count(num):
        try:
            int(num)
            if int(num) < 1 or int(num) > 100:
                raise ValueError(
                    "Please enter a number between 1 and 100.\n"
                    "No more, no less!\n"
                )
        except ValueError as e:
            print(f"Invalid data: {e}Give it another go")
            Quiz.clear_terminal(2)
            return False
        return True

    @staticmethod
    def clear_terminal(timeout=0):
        sleep(timeout)
        system("cls" if name == "nt" else "clear")

    @staticmethod
    def script_restart():
        execv(executable, ['python'] + argv)

    def set_score(self, correct):
        if correct:
            self.score += 1
    
    def get_score(self):
        return self.score

    def play(self):
        """
        Play the quiz."""
        # Depending on difficulty, populate quiz words array
        # from different dictionaries.
        if self.difficulty_level == "e":
            quiz_words = [word for word in random.sample(
                easy_words, k=int(self.word_count))]

        if self.difficulty_level == "m":
            quiz_words = [word for word in random.sample(
                medium_words, k=int(self.word_count))]

        if self.difficulty_level == "h":
            quiz_words = [word for word in random.sample(
                hard_words, k=int(self.word_count))]

        for word in quiz_words:
            for key, value in word.items():
                user_answer = input(    
                    f"Question {quiz_words.index(word) + 1}!\n"
                    f"your word is: {key}.\n"
                )
                correct_answers = value.split("/")
                correct_answers = [answ.lower() for answ in correct_answers]
                if user_answer.lower() in correct_answers:
                    print("Correct!")
                    if len(correct_answers) > 1:
                        correct_answers.remove(user_answer.lower())
                        print(
                            f"Other correct answers include:\n"
                            f"{'/'.join(correct_answers)}"
                        )
                    self.set_score(True)
                else:
                    print("Not correct!")
                    print(
                        f"Your answer should be any of the following:\n"
                        f"{'/'.join(correct_answers)}"
                    )
                    self.set_score(False)
                self.clear_terminal(2)
    
    def end_game(self):
        play_again = input(
            f"So {self.user_name}, do you want to play again with the same settings?\n"
            "Type y for yes, r to restart, or e to exit\n"

        )
        if play_again == "y":
            self.score = 0
            self.play()
            user_grade = Grade(self.score, int(self.word_count))
            user_grade.assign_grade()
            user_grade.print_grade()
            self.end_game()
        elif play_again == "r":
            self.script_restart()
        elif play_again == "e":
            exit()
