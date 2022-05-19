"""
This is a python module which contains the Quiz class.
We import this module from our run.py file
to create and run the quiz from there. """

import re


class Quiz:
    """ Create quiz class """
    def __init__(self, user_name, difficulty_level, word_count):
        self.user_name = user_name
        self.difficulty_level = difficulty_level
        self.word_count = word_count

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
            elif name.isalpha() is not True:
                raise ValueError(
                    f"Your name can only contain letters!\n"
                    f"No numbers or special characters allowed!\n"
                    f"You entered {name}.\n"
                )
        except ValueError as e:
            print(f"Invalid data:\n{e} Give it another go.")
            return False
        return True

    @staticmethod
    def validate_diff(level):
        """ 
        This method is used to validate the user's chosen
        difficulty level"""
        diff_regex = "^[^\W_]e|m|h{1,1}$"
        try:
            validity = re.search(level.lower(), diff_regex)
            # Confirm user input contains only "e", "m", or "h"
            if bool(validity) is False or level.isalpha() is False:
                raise ValueError(
                    'You need to enter either "e", "m", or "h"\n'
                    'without any other characters.'
                )
        except ValueError as e:
            print(f"Invalid data: {e} Give it another go.")
            return False
        return True