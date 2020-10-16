import enum

import numpy as np


class BoardSection(enum.Enum):
    EMPTY = 0,
    WHITE = 1,
    BLACK = 2


def create_board():
    return np.full((6, 6), BoardSection.EMPTY.value, dtype=BoardSection)

