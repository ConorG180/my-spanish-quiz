"""
This is where the quix runs from
It contains the main function, which
builds the quiz object and runs the quiz."""

from quiz_class import Quiz

squiz = Quiz("G-dog", "hard", 5)
print(squiz.user_name, squiz.difficulty_level, squiz.word_count)
print(squiz)
