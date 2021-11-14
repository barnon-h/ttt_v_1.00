#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: M Barnon

# ####################### Imports ###########################
import sys
import time
import random
import tkinter as tk
from board import Board
from bot import Bot
# ###########################################################

class Window:
    
    '''
            Game window class
    '''
    def __init__(self):
        self.bg = "#1e2121"
        self.under_menu_bg = '#53e0cb'
        self.root = tk.Tk()
        self.height = 800
        self.move= None
        self.canvas = tk.Canvas(self.root, bg=self.bg, height=self.height,width=self.height, bd=0, highlightthickness=0)
        self.under_menu = tk.Canvas(self.root, bg=self.under_menu_bg, height=self.height*0.06, width=self.height, bd=0, highlightthickness=0)
        self.setup_menu()

        self.board = Board()
        self.bot = Bot(self.board)
        self.setup_under_bar()
        self.root.mainloop()

    def rounded_square(self, x1,y1,x2,y2, radius=25):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2,y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1,y1]
        return points

    # under bar
    def setup_under_bar(self):
        step = 20
        self.accent = "#8f9493"
        accent=self.accent
        for i in range(-300,self.height+step+100, step):
            y2 = self.height*0.1
            y1= -10
            self.under_menu.create_line(i, y1, i+90,y2, width=10, fill='#3b3d3d', smooth=True)
            self.under_menu.create_line(i-15, y1, i-90-15,y2, width=10, fill=accent, smooth=True)
        self.under_menu.create_line(0, 0, self.height, 0, width= 3, fill=accent, smooth=True)
        b1,t = self.draw_buttons(self.height-100, 'Q',text_color = '#eb4034')
        self.under_menu.tag_bind(b1, '<Button-1>', self.quit)
        self.under_menu.tag_bind(t, '<Button-1>', self.quit)
        self.under_menu.pack()

    def quit(self,event):
        sys.exit()

    def draw_buttons(self, x1, text='',text_color='white'):
        accent = self.accent
        x2 = x1 + 80
        points = self.rounded_square(x1 ,8, x2, 41)
        self.under_menu.create_polygon(points, smooth=True, fill=accent)

        x1 = x1 + 5
        x2 = x2-5
        points = self.rounded_square(x1, 8+2, x2, 40)
        self.under_menu.create_polygon(points, smooth=True, fill=self.under_menu_bg)

        x1 = x1 +1
        x2 = x2-1
        points = self.rounded_square(x1, 8+3, x2, 39)
        b1 = self.under_menu.create_polygon(points, smooth=True, fill='#3c4445')

        x1 = x1+33
        t = self.under_menu.create_text(x1, 7+17, fill=text_color, font="Mono 21 bold", text=text)
        return b1, t
    # ############# Start menu ##############
    def setup_menu(self):
        x1 = self.height/2 - 100
        y1= 2*self.height /3
        t_color = '#8b8e99'
        b1,t1 = self.draw_menu_buttons(x1, y1, text = 'Easy Play',text_color=t_color, color='black')
        self.canvas.tag_bind(b1, '<Button-1>', self.play)
        self.canvas.tag_bind(t1, '<Button-1>', self.play)

        b2,t2= self.draw_menu_buttons(x1, y1+50, text="Fair Game",text_color=t_color, color='black')
        self.canvas.tag_bind(b2, '<Button-1>', self.play_random)
        self.canvas.tag_bind(t2, '<Button-1>', self.play_random)

        b3, t3 = self.draw_menu_buttons(x1, y1+100, text="Under-dog",text_color=t_color, color='black')
        self.canvas.tag_bind(b3, '<Button-1>', self.play_hard)
        self.canvas.tag_bind(t3, "<Button-1>", self.play_hard)

        # symbol and app info
        color = self.under_menu_bg
        x1 = self.height/3+55
        y1 = self.height/3-100
        for i in range(3):
            self.canvas.create_line(x1,y1,x1,y1+200, fill = color, width = 5)
            x1 += 80
        x1 = self.height/3+75
        self.canvas.create_line(x1-70, y1, x1+190, y1, fill=color, width=12)
        self.canvas.pack()

    def draw_menu_buttons(self, x, y, color='White',text='',text_color='white'):
        x2 = x+200
        y2 = y+45
        x3 = x 
        x4 = x2 - 1
        y3 = y - 1
        y4 = y2 - 1
        points = self.rounded_square(x3,y3,x4,y4)
        self.canvas.create_polygon(points, smooth = True, fill = self.under_menu_bg)
        x3 = x3+1
        x4 = x4-1
        y3 = y+1
        y4 = y4-1
        points = self.rounded_square(x3,y3,x4,y4)
        b1 = self.canvas.create_polygon(points, smooth=True, fill = color)

        x1 = x + 100
        t = self.canvas.create_text(x1, y+20, font = "Mono 21 bold italic", text=text, fill = text_color)

        return b1,t


    def play(self, event):
        re,t = self.draw_buttons(self.height-200,"R", text_color="#7c8e8f")
        self.under_menu.tag_bind(re, '<Button-1>', self.reset)
        self.under_menu.tag_bind(t, '<Button-1>', self.reset)
        home,t2 = self.draw_buttons(self.height-300,"H", text_color = "#7c8e84")
        self.under_menu.tag_bind(home, '<Button-1>', self.home)
        self.under_menu.tag_bind(t2, '<Button-1>', self.home)
        self.setup_board()
        self.mode = 1

    def play_hard(self, event):
        re,t1 = self.draw_buttons(self.height-200, "R", text_color="#7c8e8f")
        self.under_menu.tag_bind(re, '<Button-1>', self.reset)
        self.under_menu.tag_bind(t1, '<Button-1>', self.reset)
        home,t2 = self.draw_buttons(self.height-300, "H", text_color='#7c8e8f')
        self.under_menu.tag_bind(home, '<Button-1>', self.home)
        self.under_menu.tag_bind(t2, '<Button-1>', self.home)
        self.setup_board()
        bot_move = random.randint(1,9)
        self.board.update_o(bot_move)
        x,y = self.board_pos(bot_move)
        self.draw_o(x,y)
        self.mode = 2

    def play_random(self, event):
        coin = random.randint(1,10)
        if coin <=5:
            self.play(event)
        else:
            self.play_hard(event)
        self.mode=3

    def reset(self, event):
        if self.mode == 1:
            self.play(event)
        elif self.mode == 2:
            self.play_hard(event)
        elif self.mode == 3:
            self.play_random(event)

    def home(self, event):

        self.canvas.delete('all')
        self.under_menu.delete('all')

        self.setup_menu()
        self.setup_under_bar()
    # ############# Game board ##############

    def draw_squares(self, sq_l, sq_b):
        sq1 = self.canvas.create_rectangle(
            25,
            25,
            25 + self.height/3-30,
            25 + self.height/3-30,
            outline = sq_l, fill=sq_b)
        sq2 = self.canvas.create_rectangle(
            35 + self.height/3-30,
            25,
            25 + 2*self.height/3-30,
            25 + self.height/3-30,
            outline = sq_l, fill=sq_b)
        sq3 = self.canvas.create_rectangle(
            5+(2 * self.height)/3,
            25,
            self.height-25,
            25 + self.height/3-30,
            outline = sq_l, fill=sq_b)

        sq4 = self.canvas.create_rectangle(
            25,
            35 + self.height/3-30,
            25 + self.height/3-30,
            25 + 2*self.height/3-30,
            outline = sq_l, fill=sq_b)
        sq5 = self.canvas.create_rectangle(
            35 + self.height/3-30,
            35 + self.height/3 - 30,
            25 + 2*self.height/3-30,
            25 + 2*self.height/3-30,
            outline = sq_l, fill=sq_b)
        sq6 = self.canvas.create_rectangle(
            5+(2 * self.height)/3,
            35 + self.height/3-30,
            self.height-25,
            25 + 2*self.height/3-30,
            outline = sq_l, fill=sq_b)

        sq7 = self.canvas.create_rectangle(
            25,
            35 + 2*self.height/3-30,
            25 + self.height/3-30,
            self.height-25,
            outline = sq_l, fill=sq_b)
        sq8 = self.canvas.create_rectangle(
            35 + self.height/3-30,
            35 + 2*self.height/3 - 30,
            25 + 2*self.height/3-30,
            self.height-25,
            outline = sq_l, fill=sq_b)
        sq9 = self.canvas.create_rectangle(
            5+(2 * self.height)/3,
            35 + 2*self.height/3-30,
            self.height-25,
            self.height-25,
            outline = sq_l, fill=sq_b)

        self.canvas.tag_bind(sq1, '<Button-1>', self.game_click)
        self.canvas.tag_bind(sq2, '<Button-1>', self.game_click)
        self.canvas.tag_bind(sq3, '<Button-1>', self.game_click)

        self.canvas.tag_bind(sq4, '<Button-1>', self.game_click)
        self.canvas.tag_bind(sq5, '<Button-1>', self.game_click)
        self.canvas.tag_bind(sq6, '<Button-1>', self.game_click)

        self.canvas.tag_bind(sq7, '<Button-1>', self.game_click)
        self.canvas.tag_bind(sq8, '<Button-1>', self.game_click)
        self.canvas.tag_bind(sq9, '<Button-1>', self.game_click)

    def game_click(self, event):
        x = event.x
        y = event.y

        move = self.get_clicked_square(x,y)
        self.move = move

        a = self.board.available_moves()
        if self.board.end() or self.board.check_win():
            if self.mode == 1:
                self.play(event)
            elif self.mode == 2:
                self.play_hard(event)
            elif self.mode == 3:
                self.play_random(event)

        elif self.move in a and not self.board.check_win() and not self.board.end():
            self.board.update_x(self.move)
            x,y = self.board_pos(self.move)
            self.draw_x(x,y)

            if not self.board.end() and not self.board.check_win():
                bot_move = self.bot.make_move()
                self.board.update_o(bot_move)
                x,y = self.board_pos(bot_move)
                self.draw_o(x,y)

                if self.board.check_win():
                    winning_moves = self.board.get_winning_moves()
                    winner = self.board.get_winner()

                    for i in winning_moves:
                        x,y = self.board_pos(i)

                        if winner == 'o':
                            self.draw_o(x,y,'red')

                        elif winner == 'x':
                            self.draw_x(x,y,'#2ae8e5')


    def get_clicked_square(self, x, y):
        move = -1
        if x < self.height/3 and y < self.height/3:
            move = 1
        elif x > self.height/3 and x < 2*self.height/3 and y < self.height/3:
            move = 2
        elif x > 2*self.height/3 and x < self.height and y < self.height/3:
            move = 3

        if x < self.height/3 and y > self.height/3 and y < 2*self.height/3:
            move = 4
        elif x > self.height/3 and x < 2*self.height/3 and y > self.height/3 and y < 2*self.height/3:
            move = 5
        elif x > 2*self.height/3 and x < self.height and y > self.height/3 and y < 2*self.height/3:
            move = 6

        if x < self.height/3 and y > 2*self.height/3 and y < self.height:
            move = 7
        elif x > self.height/3 and x < 2*self.height/3 and y > 2*self.height/3 and y < self.height:
            move = 8
        elif x > 2*self.height/3 and x < self.height and y > 2*self.height/3 and y < self.height:
            move = 9
        return move

    def board_pos(self, pos):
        if pos == 1:
            return (self.height/6+10, self.height/6+10)
        elif pos == 2:
            return (self.height/2, self.height/6+10)
        elif pos == 3:
            return (5*self.height/6-10, self.height/6+10)
        elif pos == 4:
            return (self.height/6 + 10, self.height/2)
        elif pos == 5:
            return (self.height/2, self.height/2)
        elif pos == 6:
            return (5*self.height/6 - 10, self.height/2)
        elif pos == 7:
            return (self.height/6 + 10, 5*self.height/6-10)
        elif pos == 8:
            return (self.height/2, 5*self.height/6-10)
        elif pos == 9:
            return (5*self.height/6-10, 5*self.height/6-10)
        else:
            print("Error !")

    def draw_x(self, mid_x=400, mid_y=400, color="#50d9bb"):
        x1 = mid_x - 100
        y1 = mid_y - 100

        x2 = mid_x + 100
        y2 = mid_y + 100

        x3 = x1
        y3 = y1 + 200

        x4 = x2
        y4 = y2 - 200
        self.canvas .create_line(x1, y1, x2, y2, fill=color, width=35, smooth=True)
        self.canvas.create_line(x3,y3, x4,y4, fill=color, width=35, smooth=True)

    def draw_o(self, mid_x=400, mid_y=400, color = '#f27474'):
        r = 100
        s_r = r-40
        self.canvas.create_oval(mid_x-r, mid_y-r, mid_x+r, mid_y+r, fill=color)
        self.canvas.create_oval(mid_x-s_r, mid_y-s_r, mid_x+s_r, mid_y+s_r, fill = self.bg)

    def draw_lines(self, color='white'):
        h = self.height
        self.canvas.create_line(h/3, (h)-(h-25) , h/3, h-25, fill=color, width=9)
        self.canvas.create_line(2/3 * h, h-25, 2/3*h, 25, fill=color, width=9)
        self.canvas.create_line(25, h/3, h-25, h/3, fill=color, width=9)
        self.canvas.create_line(25, h*2/3, h-25, 2/3*h, fill=color, width=9)

    def setup_board(self):
        self.board = Board()
        self.bot = Bot(self.board)
        self.draw_squares(sq_l="#252929", sq_b="#17191a")
        self.draw_lines(color="#252929")
        self.canvas.pack()

 ######################## Main #############################
def main(argv=None)->None:
    w = Window()
    return
# ###########################################################

# ##################### Driver Code #########################
if __name__ == "__main__":
    b = Board()
    main()
# ###########################################################
# ######################### EOF #############################
