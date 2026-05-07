"""
Akinator Game - Main Entry Point
Jalankan file ini untuk memulai game.
"""

from game_engine import GameEngine
from score_manager import get_leaderboard
import ui


def main():
    player_name = None

    while True:
        choice = ui.main_menu()

        if choice == "1":
            # Minta nama pemain jika belum ada
            if player_name is None:
                player_name = ui.get_player_name()

            # ✅ Buat GameEngine, bukan menu.run()
            engine = GameEngine(player_name)
            engine.run()

            if not ui.ask_play_again():
                break

        elif choice == "2":
            # ✅ Panggil get_leaderboard() lalu tampilkan
            scores = get_leaderboard()
            ui.show_leaderboard(scores)

        elif choice == "3":
            # ✅ Tambahkan pilihan 3 yang hilang
            ui.how_to_play()

        elif choice == "4":
            break

    ui.farewell()


if __name__ == "__main__":
    main()