"""
This implements the Hand class, which consists of 4 tiles.
"""

import hanabi
import numpy as np
from tile import Tile
from typing import List, Iterable

class Hand:
    def __init__(self, tiles: List[Tile]=None) -> None:
        if tiles is None:
            self.tiles = [ Tile(), Tile(), Tile(), Tile() ]
        else:
            assert len(tiles)==4
            self.tiles = tiles

    def __eq__(self, other) -> bool:
        return self.tiles == other.tiles

    def __iter__(self) -> Iterable[Tile]:
        return self.tiles.__iter__()

    def __str__(self) -> str:
        output=""
        for tile in self.tiles:
            output+=f"{str(tile)}\n\n"
        return output

    def __repr__(self) -> str:
        return ('Hand(\n' +
                '[\n' +
                '\n'.join('    ' + repr(tile) + ',' for tile in self.tiles) +
                '\n])'
                )

    def __getitem__(self, position) -> Tile:
        return self.tiles[position]

    def add_info(self, positions:List[int], info:str) -> None:
        """
        positions is a list of ints for which the attribute "info" applies.
        """
        assert info in hanabi.colors or info in hanabi.numbers
        for i, tile in enumerate(self.tiles):
            if i in positions:
                if info in hanabi.colors:
                    n = hanabi.colors.index(info)
                    tile.colors = [ int(j == n) for j in range(5) ]
                if info in hanabi.numbers:
                    n = hanabi.numbers.index(info)
                    tile.numbers = [ int(j == n) for j in range(5) ]
            else:
                if info in hanabi.colors:
                    n = hanabi.colors.index(info)
                    tile.colors[n]=0
                if info in hanabi.numbers:
                    n = hanabi.numbers.index(info)
                    tile.numbers[n]=0

    def drop_tile(self, n=None) -> None:
        assert n is not None
        self.tiles[n] = Tile()

    def probs(self, seen) -> None:
        for i, tile in enumerate(self.tiles):
            print(f"Tile {i}")
            prep = tile.prob_matrix(seen).replace(0, np.nan).dropna(how='all', axis=0).dropna(how='all', axis=1).replace(np.nan, 0)
            print(prep)
            print()
