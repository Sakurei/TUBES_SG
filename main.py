"""
Akinator Game - Main Entry Point
Jalankan file ini untuk memulai game.
"""

from game_engine import GameEngine
<<<<<<< HEAD
=======
from score_manager import get_leaderboard
>>>>>>> 29d1287bcdba08a2068453270c0b5ed4e5b374e0
import ui


def main():
<<<<<<< HEAD
=======
    player_name = None

>>>>>>> 29d1287bcdba08a2068453270c0b5ed4e5b374e0
    while True:
        choice = ui.main_menu()

        if choice == "1":
<<<<<<< HEAD
            engine = GameEngine()
=======
            # Minta nama pemain jika belum ada
            if player_name is None:
                player_name = ui.get_player_name()

            # ✅ Buat GameEngine, bukan menu.run()
            engine = GameEngine(player_name)
>>>>>>> 29d1287bcdba08a2068453270c0b5ed4e5b374e0
            engine.run()

            if not ui.ask_play_again():
                break

        elif choice == "2":
<<<<<<< HEAD
            ui.how_to_play()

        elif choice == "3":
=======
            # ✅ Panggil get_leaderboard() lalu tampilkan
            scores = get_leaderboard()
            ui.show_leaderboard(scores)

        elif choice == "3":
            # ✅ Tambahkan pilihan 3 yang hilang
            ui.how_to_play()

        elif choice == "4":
>>>>>>> 29d1287bcdba08a2068453270c0b5ed4e5b374e0
            break

    ui.farewell()


if __name__ == "__main__":
    main()