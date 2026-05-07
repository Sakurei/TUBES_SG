"""
Akinator Game - Main Entry Point
Jalankan file ini untuk memulai game.
"""

from game_engine import GameEngine
import ui


def main():
    while True:
        choice = ui.main_menu()

        if choice == "1":
            engine = GameEngine()
            engine.run()

            if not ui.ask_play_again():
                break

        elif choice == "2":
            ui.how_to_play()

        elif choice == "3":
            break

    ui.farewell()


if __name__ == "__main__":
    main()