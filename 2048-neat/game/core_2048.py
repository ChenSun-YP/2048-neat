from game.utils import Direction
# from game.ub4c106207f7d7ae4d7fb268df44519d4e1e
# from game.utils import Key
from game.utils import State
from random import randint

EMPTY_TILE = 0

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
        # One pass to merge, one pass to shift
        made_move = False

        rotations = 0
        back_rotations = 0
        if direction == Direction.UP:
            rotations = 2
            back_rotations = 2
        elif direction == Direction.DOWN:
            rotations = 0
            back_rotations = 0
        elif direction == Direction.LEFT:
            rotations = 3
            back_rotations = 1
        elif direction == Direction.RIGHT:
            rotations = 1
            back_rotations = 3

        self.board = rotate_clockwise(self.board, rotations)

        # Merge then shift through empty space

        self.board = rotate_clockwise(self.board, back_rotations)




def fresh_board(size):
    return [[0 for i in range(0, size)] for j in range(0, size)]


# Randomly spawns a tile of value 2 or 4
# P(x = 2) = 90%, P(x = 4) = 10%
def spawn_tile(board):
    spawned = False
    num_empty_tiles = count_value(board, EMPTY_TILE)
    if num_empty_tiles == 0:
        return spawned

    probability = randint(1, 100)
    tile_value = 2 if probability <= 90 else 4

    kth_selected_tile = randint(0, num_empty_tiles - 1)
    current_empty_tile = 0
    for i, i_val in enumerate(board):
        for j, j_val in enumerate(board):
            if j_val == EMPTY_TILE:
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


# 2D array
def rotate_clockwise(arr, iteration):
    if iteration <= 0:
        return

    l = len(arr)
    for i in range(0, iteration):
        for s in range(0, int(l / 2)):
            for j in range(0, l - (2 * s) - 1):
                temp = arr[s][s + j]
                arr[s][s + j] = arr[l - s - j - 1][s]
                arr[l - s - j - 1][s] = arr[l - s - 1][l - s - j - 1]
                arr[l - s - 1][l - s - j - 1] = arr[s + j][l - s - 1]
                arr[s + j][l - s - 1] = temp

    return arr
