#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: M Barnon

# ####################### Imports ###########################
import sys
from board import Board
from bot import Bot
from gui import Window
# ###########################################################
def run():
    b = Board()
    bot = Bot(b)
    moves  = 9
    print("\npossible moves: ")
    b.print_help()
    while not b.end():
        a_moves = b.available_moves()
        print(f"Available moves : {a_moves} ")
        pos = int(input("Enter input (0 to quit): "))
        if pos == 0:
            break
        if pos in a_moves:
            b.update_x(pos)
            if not b.check_win() and not b.end():
                b.update_o(bot.make_move())
            print(b)
            moves -= 1
        else:
            print("[!] Move not available!\n")
            pass
    if b.check_win():
        print(f"{b.get_winner()} wins !\n\n...GAMEOVER...")
        print(f"Winning moves: {b.get_winning_moves()}")
    elif b.end():
        print("DRAW !")
    else:
        print("Quitting . . .")


# ######################## Main #############################
def main(argv=None)->None:
    while 1:
        run()
        another_game = str(input("Another game ? (y/n) : "))
        if another_game == "n":
            break
    pass
# ###########################################################

# ##################### Driver Code #########################
if __name__ == "__main__":
    if "-h" in sys.argv or "--help" in sys.argv or "-H" in sys.argv or "--HELP" in sys.argv:
        print("Tic Tac Toe terminal version\n\nAuthor: M. Barnon")
    else:
        main()
# ###########################################################
# ######################### EOF #############################
