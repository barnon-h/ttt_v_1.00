#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: M Barnon

# ####################### Imports ###########################
from board import Board
import math

class Bot:

    def __init__(self, board:Board):
        self.board = board
        self.b = self.board.get_board()

    def observe(self):
        self.b = self.board.get_board()

    def make_move(self):
        self.observe()
        score, move = self.minimax(alpha=-2, beta=2)
        return move

    def minimax(self, 
                alpha=-math.inf,
                beta=math.inf,
                depth:int = 10,
                is_max:bool=True
                ):

        # Depth lock
        if depth <= 0:
            return(0, 0)

        # Base case
        if self.b.check_win():
            # Winner decided
            return (1, 0) if self.b.get_winner() == 'o' else (-1, 0)
        elif self.b.end():
            # Draw
            return(0, 0)

        # Recursive case
        min_score = math.inf
        max_score = - math.inf

        pos = -1

        if is_max:
            # Max case
            for move in self.b.available_moves():
                self.b.update_o(move)
                score, position = self.minimax(
                    alpha=alpha,
                    beta=beta,
                    depth = depth-1, 
                    is_max=False
                )

                if score > max_score:
                    max_score = score
                    pos = move
                self.b.clear(move)

                if max_score >= beta:
                    return (max_score, pos)
                
                if max_score > alpha:
                    alpha = max_score

            return (max_score, pos)
        
        elif not is_max:
            # Min case
            for move in self.b.available_moves():
                self.b.update_x(move)
                score, position = self.minimax(
                    alpha = alpha,
                    beta = beta,
                    depth=depth-1, 
                    is_max=True
                )

                if score < min_score:
                    min_score = score
                    pos = move
                self.b.clear(move)

                if min_score <= alpha:
                    return (min_score, pos)

                if min_score < beta:
                    beta = min_score

            return (min_score, pos)

# ######################## Main #############################
def main(argv=None)->None:
    bd = Board()
    bd.update_x(5)
    #bd.update_x(2)
    #bd.update_o(3)
    #bd.update_x(4)
    #bd.update_x(5)
    #bd.update_o(6)
    #bd.update_o(7)
    #bd.update_o(8)
    #bd.update_x(9)
    print(bd)
    b = Bot(bd)
    print(b.make_move())

# ###########################################################

# ##################### Driver Code #########################
if __name__ == "__main__":
    main()
# ###########################################################
# ######################### EOF #############################
