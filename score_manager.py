"""
Module: score_manager.py
Mengelola penyimpanan dan pembacaan skor pemain (leaderboard).
"""

import json
import os

SCORE_FILE = os.path.join(os.path.dirname(__file__), "scores.json")


def _load_scores():
    """Memuat skor dari file JSON."""
    if not os.path.exists(SCORE_FILE):
        return []
    try:
        with open(SCORE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def _save_scores(scores):
    """Menyimpan skor ke file JSON."""
    with open(SCORE_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)


def calculate_score(questions_asked, correct):
    """
    Menghitung skor berdasarkan jumlah pertanyaan.
    Semakin sedikit pertanyaan → skor lebih tinggi.
    """
    if not correct:
        return 0
    base = 1000
    penalty = questions_asked * 50
    return max(base - penalty, 100)


def save_score(player_name, score, questions_asked):
    """Menyimpan skor baru ke leaderboard."""
    scores = _load_scores()
    scores.append({
        "name": player_name,
        "score": score,
        "questions": questions_asked,
    })
    # Urutkan dari skor tertinggi
    scores.sort(key=lambda x: x["score"], reverse=True)
    _save_scores(scores)


def get_leaderboard():
    """Mengembalikan daftar skor terurut (tertinggi ke terendah)."""
    return _load_scores()
