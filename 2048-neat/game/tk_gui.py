import game.utils as utils
from tkinter import *

SIZE = 500
GRID_LEN = 4
GRID_PADDING = 10
EMPTY_TILE = 0
FONT = ("Verdana", 40, "bold")


class GameGUI(Frame):
    def __init__(self, board, score=0):
        self.board = board
        self.board_size = len(board)
        self.score = score

        Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        self.grid_cells = []
        self._draw_board()

    # For decoupling view with game logic
    def set_board(self, board):
        self.board = board

    def repaint(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                val = self.board[i][j]
                if val == EMPTY_TILE:
                    self.grid_cells[i][j].config(text="", bg=_get_colour(EMPTY_TILE))
                else:
                    self.grid_cells[i][j].config(text=str(val), bg=_get_colour(val))

        self.update_idletasks()
        self.update()

    def _draw_board(self):
        background = Frame(self, bg=_get_colour(None), width=SIZE, height=SIZE)
        background.grid()
        for i in range(self.board_size):
            grid_row = []
            for j in range(self.board_size):
                cell = Frame(background, bg=_get_colour(EMPTY_TILE), width=SIZE/self.board_size, height=SIZE/self.board_size)
                cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                t = Label(master=cell, text="", bg=_get_colour(EMPTY_TILE), justify=CENTER, font=FONT, width=4, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)


# Coverts (r, g, b) to hex #rrggbb
def _get_colour(num):
    return '#%02x%02x%02x' % utils.get_colour(num)
