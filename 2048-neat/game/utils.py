from enum import Enum


class State(Enum):
    MENU = "menu"
    IDLE = "idle"
    SHIFTING = "shifting"
    WIN = "win"
    LOSS = "loss"


class Key(Enum):
    UP = "W"
    DOWN = "S"
    LEFT = "A"
    RIGHT = "D"
    RESTART = "R"
    BACK = "B"
    ENTER = "Enter"


class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


BLACK = (0, 0, 0)
RED = (244, 67, 54)
PINK = (234, 30, 99)
PURPLE = (156, 39, 176)
DEEP_PURPLE = (103, 58, 183)
BLUE = (33, 150, 243)
TEAL = (0, 150, 136)
LIGHT_GREEN = (139, 195, 74)
GREEN = (60, 175, 80)
ORANGE = (255, 152, 0)
DEEP_ORANGE = (255, 87, 34)
BROWN = (121, 85, 72)
WHITE = (255, 255, 255)

alt_colors = {0: BLACK, 2: RED, 4: PINK, 8: PURPLE, 16: DEEP_PURPLE, 32: BLUE, 64: TEAL, 128: LIGHT_GREEN, 256: GREEN,
              512: ORANGE, 1024: DEEP_ORANGE, 2048: BROWN, 4096: RED, 8192: PINK, 16384: PURPLE, 32768: DEEP_PURPLE}

ZERO = (205, 193, 180)
TWO = (238, 228, 218)
FOUR = (237, 224, 200)
EIGHT = (242, 177, 121)
ONE_SIX = (245, 124, 59)
THREE_TWO = (246, 124, 95)
SIX_FOUR = (246, 94, 59)
ONE_TWO_EIGHT = (237, 207, 114)
TWO_FIVE_SIX = (237, 204, 97)
FIVE_ONE_TWO = (237, 200, 80)
ONE_ZERO_TWO_FOUR = (237, 197, 63)
TWO_ZERO_FOUR_EIGHT = (237, 194, 46)

colors = {0: ZERO, 2: TWO, 4: FOUR, 8: EIGHT, 16: ONE_SIX, 32: THREE_TWO, 64: SIX_FOUR, 128: ONE_TWO_EIGHT,
          256: TWO_FIVE_SIX, 512: FIVE_ONE_TWO, 1024: ONE_ZERO_TWO_FOUR, 2048: TWO_ZERO_FOUR_EIGHT}


def get_colour(i):
    return colors[i] if colors[i] is not None else BLACK





