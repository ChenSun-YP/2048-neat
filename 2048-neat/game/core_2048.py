from game.utils import Direction
from game.utils import Key
from game.utils import State


class GameCore:
    def __init__(self, game_size=4):
        self.game_size = game_size
        self.board = []
        self.score = 0
        self.State = State.MENU

    def score(self):
        return self.score

    def board(self):
        return self.board

    def game_size(self):
        return self.game_size

    def restart_game(self, game_size=4):
        pass

    def try_move(self, direction):
        pass
