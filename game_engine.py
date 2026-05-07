"""
Module: game_engine.py
Mengatur alur satu sesi permainan Akinator.
"""

from decision_tree import DecisionTree
from questions import QUESTION_TEXT
<<<<<<< HEAD
=======
from score_manager import calculate_score, save_score
>>>>>>> 29d1287bcdba08a2068453270c0b5ed4e5b374e0
import ui


class GameEngine:
    """Menjalankan satu sesi permainan."""

<<<<<<< HEAD
    def __init__(self):
=======
    def __init__(self, player_name):
        self.player_name   = player_name
>>>>>>> 29d1287bcdba08a2068453270c0b5ed4e5b374e0
        self.tree          = DecisionTree()
        self.question_count = 0

    def _ask(self, attribute):
        """Callback yang diberikan ke decision tree untuk bertanya ke user."""
        self.question_count += 1
        question = QUESTION_TEXT.get(attribute, attribute)
        return ui.ask_question(question, self.question_count)

    def run(self):
<<<<<<< HEAD
        """Menjalankan sesi permainan."""
        self.question_count = 0
        guessed_character = self.tree.start_traversal(self._ask)
        ui.show_guess(guessed_character)
        correct = ui.ask_correct()
        if correct:
            ui.show_win()
        else:
            ui.show_lose()
=======
        """
        Menjalankan sesi permainan.
        Mengembalikan skor yang didapat pemain.
        """
        self.question_count = 0

        # Traversal rekursif melalui pohon
        guessed_character = self.tree.start_traversal(self._ask)

        # Tampilkan tebakan
        ui.show_guess(guessed_character)

        # Cek apakah tebakan benar
        correct = ui.ask_correct()
        score   = calculate_score(self.question_count, correct)

        if correct:
            ui.show_win(score)
            save_score(self.player_name, score, self.question_count)
        else:
            ui.show_lose()

        return score
>>>>>>> 29d1287bcdba08a2068453270c0b5ed4e5b374e0
