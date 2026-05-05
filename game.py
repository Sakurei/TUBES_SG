import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.yes = None
        self.no = None

    def is_leaf(self):
        return self.yes is None and self.no is None

def main_menu():
    print("\n" + "="*30)
    print("   AKINATOR TOKOH SEJARAH")
    print("="*30)
    print("1. Start Game")
    print("2. Exit")
    choice = input("Pilih menu (1/2): ")
    if choice == '1':
        start_game()
    else:
        print("Sampai jumpa!")
        sys.exit()

def start_game():
    print("\nPikirkan satu tokoh sejarah (Nasional/Internasional)...")
    print("Akinator akan mencoba menebaknya!")
    input("Tekan Enter jika sudah siap...")
    
    play_recursive(root)
    main_menu()

