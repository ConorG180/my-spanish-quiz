"""
This is a python module which contains the Quiz class.
We import this module from our run.py file
to create and run the quiz from there. """


class Quiz:
    """ Create quiz class """
    def __init__(self, user_name, difficulty_level, word_count):
        self.user_name = user_name
        self.difficulty_level = difficulty_level
        self.word_count = word_count
