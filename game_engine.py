"""
Module: game_engine.py
Mengatur alur satu sesi permainan Akinator.
"""

from decision_tree import DecisionTree
from questions import QUESTION_TEXT
import ui


class GameEngine:
    """Menjalankan satu sesi permainan."""

    def __init__(self):
        self.tree          = DecisionTree()
        self.question_count = 0

    def _ask(self, attribute):
        """Callback yang diberikan ke decision tree untuk bertanya ke user."""
        self.question_count += 1
        question = QUESTION_TEXT.get(attribute, attribute)
        return ui.ask_question(question, self.question_count)

    def run(self):
        """Menjalankan sesi permainan."""
        self.question_count = 0
        guessed_character = self.tree.start_traversal(self._ask)
        ui.show_guess(guessed_character)
        correct = ui.ask_correct()
        if correct:
            ui.show_win(self.question_count)
        else:
            ui.show_lose()
