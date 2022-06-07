"""
This is a python module which contains the Grade class.
We import this module from our run.py file
to create and run the grade functions from there."""

import math


class Grade:
    """ Create Grade class """
    def __init__(self, score, total_words):
        self.score = score  # Number of words user got correct
        self.total_words = total_words  # Number of words in user quiz
        self.grade = ""  # User grade, determined by score
        self.grade_comment = ""  # Message/comment to user, determined by grade
        self.incorrect_answers = self.total_words - self.score
        self.score_percent = int(round((self.score * 100) / self.total_words))

    def make_grade(self, grade_letter, grade_range):

        """ This method is used to make the grade
        for the user. It calculates the number by
        subtracting the upper range of the grade
        from the user's percent and dividing it
        by 5, and then using ceiling function.
        This works out as the number at end of grade.
        Then, Concatinates grade_letter to this
        number, example B1, C2, D1, D3, A2 etc."""

        number = (grade_range - self.score_percent) / 5
        grade_number = math.ceil(number)
        grade = grade_letter + str(grade_number)
        return grade

    def assign_grade(self):
        """This method assigns values
        to the grade and grade comment properties
        grade depending the user's score"""

        if self.score_percent < 40:
            self.grade = "F"
            self.grade_comment = "You failed!! Study harder hombre!"

        elif self.score_percent >= 40 and self.score_percent < 55:
            self.grade = self.make_grade("D", 55)
            self.grade_comment = "You passed, you did ok!"

        elif self.score_percent >= 55 and self.score_percent < 70:
            self.grade = self.make_grade("C", 70)
            self.grade_comment = "You did average and passed! Good."

        elif self.score_percent >= 70 and self.score_percent < 85:
            self.grade = self.make_grade("B", 85)
            self.grade_comment = "Very good! You did above average"

        elif self.score_percent >= 85 and self.score_percent < 100:
            self.grade = self.make_grade("A", 100)
            self.grade_comment = "Very good! You nailed it!!"

        elif self.score_percent == 100:
            self.grade = "A*"
            self.grade_comment = "An A star!! 100%! You did perfect!"

    def print_grade(self):
        """ This method prints all relevant
        statistics and comments about the
        user's quiz"""
        print(
            f"Out of {self.total_words} questions,\n"
            f"You correctly answered {self.score}.\n"
            f"You incorrectly answered {self.incorrect_answers}.\n"
            f"This gives you a mark of {self.score_percent}%.\n"
            f"You got a {self.grade}!\n"
            f"{self.grade_comment}."
        )
