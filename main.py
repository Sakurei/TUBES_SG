"""
Akinator Game - Main Entry Point
Jalankan file ini untuk memulai game.
"""

from game_engine import GameEngine
import ui


def main():
    player_name = None

    while True:
        choice = ui.main_menu()

        if choice == "1":
            engine = GameEngine()
            engine.run()

            if not ui.ask_play_again():
                break

        elif choice == "3":
            ui.how_to_play()

        elif choice == "2":
            # ✅ Panggil get_leaderboard() lalu tampilkan
            ui.show_leaderboard([]) 

        elif choice == "5":
            break

        elif choice == "4":
            ui.list_characters()

    ui.farewell()


if __name__ == "__main__":
    main()