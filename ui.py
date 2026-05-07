"""
Module: ui.py
Semua fungsi tampilan terminal untuk game Akinator.
"""

import os
import time


# ------------------------------------------------------------------ #
#  Warna ANSI                                                          #
# ------------------------------------------------------------------ #
class Color:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    CYAN    = "\033[96m"
    YELLOW  = "\033[93m"
    GREEN   = "\033[92m"
    RED     = "\033[91m"
    MAGENTA = "\033[95m"
    BLUE    = "\033[94m"
    WHITE   = "\033[97m"
    DIM     = "\033[2m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_slow(text, delay=0.03):
    """Mencetak teks karakter per karakter agar terasa dramatis."""
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()


def banner():
    """Menampilkan banner judul game."""
    clear_screen()
    print(Color.CYAN + Color.BOLD)
    print("=" * 60)
    print(r"""
     █████╗ ██╗  ██╗██╗███╗   ██╗ █████╗ ████████╗ ██████╗ ██████╗ 
    ██╔══██╗██║ ██╔╝██║████╗  ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
    ███████║█████╔╝ ██║██╔██╗ ██║███████║   ██║   ██║   ██║██████╔╝
    ██╔══██║██╔═██╗ ██║██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██╗
    ██║  ██║██║  ██╗██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    """)
    print("           🏛️  Tebak Tokoh Sejarah Dunia  🏛️")
    print("=" * 60)
    print(Color.RESET)


def main_menu():
    """Menampilkan menu utama dan mengembalikan pilihan user."""
    banner()
    print(Color.YELLOW + Color.BOLD + "  MENU UTAMA\n" + Color.RESET)
    print(Color.WHITE + "  [1]  🎮  Mulai Permainan")
    print("  [2]  🏆  Papan Skor Teratas")
    print("  [3]  📖  Cara Bermain")
    print("  [4]  ❌  Keluar" + Color.RESET)
    print()
    return input(Color.CYAN + "  Pilih menu (1-4): " + Color.RESET).strip()


def how_to_play():
    """Menampilkan panduan bermain."""
    clear_screen()
    print(Color.CYAN + Color.BOLD + "\n  📖  CARA BERMAIN\n" + Color.RESET)
    lines = [
        "1. Pikirkan salah satu tokoh sejarah dalam pikiranmu.",
        "2. Akinator akan mengajukan serangkaian pertanyaan.",
        "3. Jawab setiap pertanyaan dengan  Ya  atau  Tidak.",
        "4. Akinator akan mencoba menebak tokoh yang kamu pikirkan.",
        "5. Semakin sedikit pertanyaan, semakin tinggi skormu!",
        "",
        "Daftar tema: Tokoh Eropa, Asia, Timur Tengah, Afrika, Amerika",
        "             Ilmuwan, Filsuf, Pemimpin Militer, Revolusioner, dll.",
    ]
    for line in lines:
        print(Color.WHITE + "  " + line + Color.RESET)
    print()
    input(Color.DIM + "  Tekan Enter untuk kembali..." + Color.RESET)


def ask_question(question_text, question_number):
    """Menampilkan pertanyaan dan mendapatkan jawaban user (ya/tidak)."""

    print(Color.YELLOW + f"\n  Pertanyaan #{question_number}:" + Color.RESET)
    print(Color.WHITE + f"  ❓ {question_text}" + Color.RESET)

    while True:
        ans = input(Color.CYAN + "  Jawaban (ya/tidak/y/t): " + Color.RESET).strip().lower()
        if ans in ("ya", "y"):
            return True
        elif ans in ("tidak", "t"):
            return False
        else:
            print(Color.RED + "  ⚠️  Masukkan 'ya' atau 'tidak'." + Color.RESET)


def show_thinking():
    """Animasi 'sedang berpikir'."""
    print()
    print_slow(Color.MAGENTA + "  🔮 Akinator sedang membaca pikiranmu", delay=0.04)
    for _ in range(3):
        time.sleep(0.5)
        print(Color.MAGENTA + "  .", end="", flush=True)
    print(Color.RESET)
    time.sleep(0.5)


def show_guess(character_name):
    """Menampilkan tebakan Akinator secara dramatis."""
    show_thinking()
    print()
    print(Color.GREEN + Color.BOLD + "  ✨ AKINATOR MENEBAK ✨" + Color.RESET)
    print()
    print_slow(Color.WHITE + Color.BOLD + f"  👉  {character_name.upper()}  👈" + Color.RESET, delay=0.05)
    print()


def ask_correct():
    """Menanyakan apakah tebakan benar."""
    while True:
        ans = input(Color.CYAN + "  Apakah tebakan Akinator BENAR? (ya/tidak): " + Color.RESET).strip().lower()
        if ans in ("ya", "y"):
            return True
        elif ans in ("tidak", "t"):
            return False
        print(Color.RED + "  ⚠️  Masukkan 'ya' atau 'tidak'." + Color.RESET)


def show_win(score):
    """Animasi menang."""
    print()
    print(Color.GREEN + Color.BOLD + "  🎉 BENAR! Akinator menang! 🎉" + Color.RESET)
    print(Color.YELLOW + f"  ⭐ Skor kamu: {score} poin" + Color.RESET)
    print()


def show_lose():
    """Tampilan kalah."""
    print()
    print(Color.RED + Color.BOLD + "  😔 Akinator kalah kali ini..." + Color.RESET)
    print(Color.WHITE + "  Tokoh kamu akan membuat Akinator lebih pintar!" + Color.RESET)
    print()


def get_player_name():
    """Meminta nama pemain."""
    print()
    name = input(Color.CYAN + "  Masukkan nama kamu: " + Color.RESET).strip()
    return name if name else "Pemain"


def ask_play_again():
    """Menanyakan apakah ingin main lagi."""
    ans = input(Color.YELLOW + "\n  Main lagi? (ya/tidak): " + Color.RESET).strip().lower()
    return ans in ("ya", "y")


def show_leaderboard(scores):
    """Menampilkan papan skor teratas."""
    clear_screen()
    print(Color.YELLOW + Color.BOLD + "\n  🏆  PAPAN SKOR TERATAS\n" + Color.RESET)
    if not scores:
        print(Color.DIM + "  Belum ada skor tersimpan.\n" + Color.RESET)
    else:
        print(Color.WHITE + f"  {'No':<4} {'Nama':<20} {'Skor':<8} {'Pertanyaan'}" + Color.RESET)
        print("  " + "-" * 44)
        for i, entry in enumerate(scores[:10], 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "  "
            print(Color.WHITE +
                  f"  {i:<4} {entry['name']:<20} {entry['score']:<8} {entry['questions']} pertanyaan" +
                  Color.RESET)
    print()
    input(Color.DIM + "  Tekan Enter untuk kembali..." + Color.RESET)


def farewell():
    """Pesan perpisahan."""
    clear_screen()
    print()
    print_slow(Color.CYAN + Color.BOLD + "  Terima kasih sudah bermain Akinator! Sampai jumpa! 🏛️" + Color.RESET)
    print()
