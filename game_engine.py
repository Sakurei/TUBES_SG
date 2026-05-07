"""
Module: game_engine.py
Mengatur alur satu sesi permainan Akinator.
"""

from decision_tree import DecisionTree
from questions import QUESTION_TEXT
from score_manager import calculate_score, save_score
import ui


class GameEngine:
    """Menjalankan satu sesi permainan."""

    def __init__(self, player_name):
        self.player_name   = player_name
        self.tree          = DecisionTree()
        self.question_count = 0

    def _ask(self, attribute):
        """Callback yang diberikan ke decision tree untuk bertanya ke user."""
        self.question_count += 1
        question = QUESTION_TEXT.get(attribute, attribute)
        return ui.ask_question(question, self.question_count)

    def run(self):
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
