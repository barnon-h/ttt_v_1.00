# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# Author: M Barnon


class Board:

    """  Board Class for Tic Tac Toe game """
    
    """
        Methods - 
        ---------
        get_board()
        end()
        get_winner()
        check_win()
        available_moves()
        update_x()
        update_o()
    """

    # ################# Class Variables ########################
    x = 1
    o = 0

    # ################ Class Constructor #######################
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]

    # #################### get_board ###########################
    def get_board(self):
        tmp = Board()
        tmp.board = [i.copy() for i in self.board]
        return tmp

    def print_help(self):
        bar = '-' * 9 + "\n"
        line = '' + bar
        count = 1
        for i in self.board:
            line += "| "
            for j in i:
                tmp = count
                count += 1
                line += str(tmp) + " "
            line += '|\n' + bar
        print(line)

    # ################### toString #############################
    def __str__(self)->str:
        bar = '-' * 9 + "\n"
        line = '' + bar
        for i in self.board:
            line += "| "
            for j in i:
                tmp = 'x' if j == Board.x else 'o'
                line += tmp + " " if j is not None else "  "
            line += "|\n" + bar
        return line

    # ####################### end ##############################
    def end(self)->bool:
        """
        returns True if game has ended (out of moves or game won)
        """
        if len(self.available_moves()) == 0:
            return True
        return False

    # ###################### get_winner #########################
    def get_winner(self)->str:
        """
            returns a string with the winning symbol
        """
        if self.check_win():
            if self.__check_row()[0]:
                winning_moves = self.__check_row()[1]
            elif self.__check_col()[0]:
                winning_moves = self.__check_col()[1]
            elif self.__check_diagonal()[0]:
                winning_moves = self.__check_diagonal()[1]
        tmp = [self.__address_to_index(i) for i in winning_moves][0]
        win = self.board[tmp[0]][tmp[1]]
        win = 'x' if win == 1 else 'o'
        return win

    # ##################### check_win ###########################
    def check_win(self)->bool:
        """
            returns True if game has been won
        """
        return self.__check_row()[0] or self.__check_col()[0] or self.__check_diagonal()[0]

    def get_winning_moves(self):
        if self.__check_row()[0]:
            return self.__check_row()[1]
        elif self.__check_diagonal()[0]:
            return self.__check_diagonal()[1]
        elif self.__check_col()[0]:
            return self.__check_col()[1]
    # #################### available_moves ######################
    def available_moves(self)->list:
        """
            returns a list of empty spots on the board
        """
        l = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == None:
                    l.append((i,j))
        l = [self.__index_to_address(i[0], i[1]) for i in l]
        return l

    # ################### update_x ##############################
    def update_x(self, pos)->None:
        """
            updates given position in the board with x
        """
        assert pos > 0 and pos < 10
        self.__update(pos, Board.x)

    # #################### update_o #############################
    def update_o(self, pos):
        """
            updates given position in the board with y
        """
        assert pos > 0 and pos < 10
        self.__update(pos, Board.o)
  
    # ####################### clear #############################
    def clear(self, pos):
        i, j = self.__address_to_index(pos)
        self.board[i][j] = None
    # ################### HELPERS ###############################

    def __update(self, pos, sym)->None:
        """
            updates the board given position and symbol
        """
        i,j = self.__address_to_index(pos)
        self.board[i][j] = sym

    def __address_to_index(self, pos):
        """
            returns array index given position
        """
        out = None
        if pos == 1:
            out = (0,0)
        elif pos == 2:
            out = (0,1)
        elif pos == 3:
            out = (0,2)
        elif pos == 4:
            out = (1,0)
        elif pos == 5:
            out = (1,1)
        elif pos == 6:
            out = (1,2)
        elif pos == 7:
            out = (2,0)
        elif pos == 8:
            out = (2,1)
        elif pos == 9:
            out = (2,2)
        return out

    def __index_to_address(self, i, j):
        """
            returns position given array index
        """
        out = None
        if i == 0:
            if j == 0:
                out = 1
            elif j == 1:
                out = 2
            elif j == 2:
                out = 3
        elif i == 1:
            if j == 0:
                out = 4
            elif j == 1:
                out = 5
            elif j == 2:
                out = 6
        elif i == 2:
            if j == 0:
                out = 7
            elif j == 1:
                out = 8
            elif j == 2:
                out = 9
        return out

    def __check_row(self):
        """
            Checks all rows for possible wins
            returns (boolean, list of winning moves)
        """
        for i in range(len(self.board)):
            tmp = self.board
            if tmp[i][0] is not None and tmp[i][0] == tmp[i][1] and tmp[i][0] == tmp[i][2]:
                l = [(i,0), (i,1), (i,2)]
                l = [self.__index_to_address(j[0], j[1]) for j in l]
                return True, l
        return False, 0

    def __check_col(self):
        """
            checks all columns for possible wins
            returns (boolean, list of winning moves)
        """
        for i in range(len(self.board[0])):
            col_1 = self.board[0][i]
            col_2 = self.board[1][i]
            col_3 = self.board[2][i]
            if col_1 is not None and col_1 == col_2 and col_1 == col_3 :
                l = [(0, i), (1, i), (2, i)]
                l = [self.__index_to_address(i[0], i[1]) for i in l]
                return True, l
        return False, 0

    def __check_diagonal(self):
        """
            checks both diagonals for possible wins
            returns (boolen, list of winning moves)
        """
        tmp = self.board
        if tmp[0][0] is not None:
            if tmp[0][0] == tmp[1][1] and tmp[1][1] == tmp[2][2]:
                l = [(0,0), (1,1), (2,2)]
                l = [self.__index_to_address(i[0], i[1]) for i in l]
                return True, l
        if tmp[2][0] is not None:
            if tmp[2][0] == tmp[1][1] and tmp[1][1] == tmp[0][2]:
                l = [(2,0), (1,1), (0,2)]
                l = [self.__index_to_address(i[0], i[1]) for i in l]
                return True, l
        return False, 0

    # ---------------------- Board --------------------------

# ######################## Main #############################
def main(argv=None)->None:
    b = Board()
    b.update_o(7)
    b.update_o(5)
    b.update_x(3)
    t = b.get_board()
    b.update_x(1)
    t.update_x(2)
    t.update_x(1)
    print(b)
    print("t")
    print(t)
    print(b.check_win())
    print(t.check_win())
    print(b.available_moves())
# ###########################################################

# ##################### Driver Code #########################
if __name__ == "__main__":
    main()
# ###########################################################
# ######################### EOF #############################
