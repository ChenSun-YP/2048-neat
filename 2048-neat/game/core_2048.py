# from game.utils import Direction
# from game.utils import Key
from game.utils import State
from random import randint


class GameCore:
    def __init__(self, game_size=4):
        self.game_size = game_size
        self.board = fresh_board(game_size)
        self.score = 0
        self.State = State.MENU

    def score(self):
        return self.score

    def board(self):
        return self.board

    def game_size(self):
        return self.game_size

    def restart_game(self, game_size=4):
        self.game_size = game_size
        self.score = 0
        self.board = fresh_board(game_size)

        # Spawn two tiles randomly on the board
        spawn_tile(self.board)
        spawn_tile(self.board)

    def try_move(self, direction):
        pass


def fresh_board(size):
    return [[0 for i in range(0, size)] for j in range(0, size)]


# Randomly spawns a tile of value 2 or 4
# P(x = 2) = 90%, P(x = 4) = 10%
def spawn_tile(board):
    spawned = False
    num_empty_tiles = count_value(board, 0)
    if num_empty_tiles == 0:
        return spawned

    probability = randint(1, 100)
    tile_value = 2 if probability <= 90 else 4

    kth_selected_tile = randint(0, num_empty_tiles - 1)
    current_empty_tile = 0
    for i, i_val in enumerate(board):
        for j, j_val in enumerate(board):
            if j_val == 0:
                current_empty_tile = current_empty_tile + 1
                if current_empty_tile == kth_selected_tile:
                    board[i][j] = tile_value
                    spawned = True
                    break

        if spawned:
            break

    return spawned


# 2D array
def count_value(arr, value):
    count = 0
    for i in arr:
        for j in i:
            if j == value:
                count = count + 1

    return count

print(fresh_board(4))