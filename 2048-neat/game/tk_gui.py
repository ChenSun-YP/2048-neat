import game.utils as utils
from tkinter import *

WINDOW_SIZE = 1000
BOARD_DISPLAY_SIZE = 500
GRID_PADDING = 10
EMPTY_TILE = 0
FONT = ("Verdana", 40, "bold")


class GameGUI(Frame):
    def __init__(self, game):
        self.game = game
        self.board = game.Board()
        self.board_size = len(self.board)
        self.score = game.Score()

        Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        self.board_grid_cells = []
        self.score_grid_cells = []
        self._draw_board()
        self._draw_score()

    # For decoupling view with game logic
    # def set_board(self, board):
    #     self.board = board
    #
    # def set_score(self, score):
    #     self.score = score

    def set_game(self, game):
        self.game = game

    def repaint(self):
        self.board = self.game.Board()
        for i in range(self.board_size):
            for j in range(self.board_size):
                val = self.board[i][j]
                if val == EMPTY_TILE:
                    self.board_grid_cells[i][j].config(text="", bg=_get_colour(EMPTY_TILE))
                else:
                    self.board_grid_cells[i][j].config(text=str(val), bg=_get_colour(val))

        self.score = self.game.Score()
        self.score_grid_cells[0].config(text="Score: " + str(self.score))

        self.update_idletasks()
        self.update()

    def _draw_board(self):
        background = Frame(self, bg=_get_colour(None), width=WINDOW_SIZE, height=WINDOW_SIZE)
        background.grid()
        board_frame = Frame(background, bg=_get_colour(None), width=BOARD_DISPLAY_SIZE, height=BOARD_DISPLAY_SIZE)
        board_frame.grid()
        for i in range(self.board_size):
            grid_row = []
            for j in range(self.board_size):
                cell = Frame(board_frame, bg=_get_colour(EMPTY_TILE), width=BOARD_DISPLAY_SIZE / self.board_size, height=BOARD_DISPLAY_SIZE / self.board_size)
                cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                t = Label(master=cell, text="", bg=_get_colour(EMPTY_TILE), justify=CENTER, font=FONT, width=4, height=2)
                t.grid()
                grid_row.append(t)

            self.board_grid_cells.append(grid_row)
        board_frame.pack()

    def _draw_score(self):
        score_frame_size = 50
        score_frame = Frame(self, bg=_get_colour(None), width=score_frame_size / 2, height=score_frame_size)
        score_frame.grid()
        score_text = Label(master=score_frame, text="Score: " + str(self.score), bg=_get_colour(None), justify=CENTER, font=("Verdana", 10, "bold"))
        self.score_grid_cells.append(score_text)
        score_text.grid()
        self.update()


# Coverts (r, g, b) to hex #rrggbb
def _get_colour(num):
    return '#%02x%02x%02x' % utils.get_colour(num)
