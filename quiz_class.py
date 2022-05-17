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
        except ValueError as e:
            print(f"Invalid data:\n {e} Give it another go.")
            return False
        return True
