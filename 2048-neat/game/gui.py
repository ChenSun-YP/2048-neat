from time import sleep

import pygame
import game.utils as utils
from game.utils import WHITE
from game.utils import ZERO


class GameGUI:
    def __init__(self, board, score=0):
        self.board = board
        self.board_size = len(board)
        self.score = score
        self.surface = pygame.display.set_mode((600, 700))

        pygame.init()

        pygame.display.set_caption("2048")

        self.label_font = pygame.font.SysFont("monospace", 25)
        self.score_font = pygame.font.SysFont("monospace", 50)

    def repaint(self):
        self.surface.fill(ZERO)

        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                pygame.draw.rect(self.surface, _get_colour(self.board[i][j]),
                                 (i * (600 / self.board_size), j * (600 / self.board_size) + 100, 600 / self.board_size,
                                  600 / self.board_size))

                label = self.label_font.render(str(self.board[i][j]), 1, WHITE)
                label2 = self.score_font.render("Score: " + str(self.score), 1, WHITE)

                offset = 0

                if self.board[i][j] < 10:
                    offset = -10
                elif self.board[i][j] < 100:
                    offset = -15
                elif self.board[i][j] < 1000:
                    offset = -20
                else:
                    offset = -25

                if self.board[i][j] > 0:
                    self.surface.blit(label, (i * (600 / self.surface) + (300 / self.surface) + offset,
                                              j * (600 / self.surface) + 100 + 300 / self.surface - 15))
                    self.surface.blit(label2, (10, 20))


def _get_colour(num):
    return utils.get_colour(num)


while True:
    sleep(1)
    pygame.display.flip()
