"""
This implements the Tile class.
A Tile should be the data of what numbers and colors the tile possibly is.
"""

import numpy as np
import pandas as pd
import hanabi
from typing import List

class Tile:
    def __init__(self, colors:List[int] = None, numbers:List[int] = None) -> None:
        # The two arrays indicate the given hints.
        # 1 means the tile can be the number/color, and 0 means the tile is not.
        if colors is not None:
            assert len(colors)==5
            self.colors=colors
        else:
            self.colors = [1]*5
        if numbers is not None:
            assert len(numbers)==5
            self.numbers=numbers
        else:
            self.numbers = [1]*5

    def __repr__(self) -> str:
        return f"Tile(colors={self.colors}, numbers={self.numbers})"

    def __str__(self) -> str:
        return f"""
        Colors: {self.colors}.
        Numbers: {self.numbers}."""
        # return self.possible_colors.__repr__()

    def __eq__(self, other) -> bool:
        return self.numbers == other.numbers and self.colors == other.colors

    def prob_matrix(self, seen:pd.DataFrame) -> pd.DataFrame:
        assert seen.shape == (5, 5)
        total_num_tiles = pd.DataFrame(
                np.array( [3, 2, 2, 2, 1]*5 ).reshape(5, 5),
                index=hanabi.colors,
                columns=hanabi.numbers,
                )
        # This is a 5 by 5 matrix of 0 and 1, indicating possible titles.
        a=np.array(self.colors).reshape(5, 1)
        b=np.array(self.numbers)
        # total_num_tiles-seen is a df of the counts of remaining tiles.
        # Multiply by the above matrix to see which tile this possibly is.
        num_possible = (total_num_tiles - seen) * (a*b)
        return num_possible/(num_possible.sum().sum())
