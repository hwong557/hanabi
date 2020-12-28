import hanabi
from tile import Tile
from hand import Hand
from assistant import add_new_sighting
import numpy as np
import pandas as pd

def test_prob_matrix():
    seen = np.array(
            [[1, 0, 2, 1, 0],
             [2, 1, 1, 1, 1],
             [0, 2, 1, 2, 1],
             [3, 2, 2, 1, 1],
             [3, 1, 1, 2, 1]]
             )

    tiles = [
                Tile(),
                Tile(colors=[1, 1, 1, 0, 1], numbers=[1, 0, 1, 1, 1]),
                Tile(colors=[1, 1, 0, 1, 1], numbers=[1, 1, 0, 1, 1]),
                Tile(colors=[0, 1, 1, 0, 1], numbers=[0, 1, 0, 1, 1]),
            ]

    expected = [{"one":{"red":0.1176470588,"blue":0.0588235294,"green":0.1764705882,"yellow":0.0,"white":0.0},"two":{"red":0.1176470588,"blue":0.0588235294,"green":0.0,"yellow":0.0,"white":0.0588235294},"three":{"red":0.0,"blue":0.0588235294,"green":0.0588235294,"yellow":0.0,"white":0.0588235294},"four":{"red":0.0588235294,"blue":0.0588235294,"green":0.0,"yellow":0.0588235294,"white":0.0},"five":{"red":0.0588235294,"blue":0.0,"green":0.0,"yellow":0.0,"white":0.0}},
 {"one":{"red":0.1666666667,"blue":0.0833333333,"green":0.25,"yellow":0.0,"white":0.0},"two":{"red":0.0,"blue":0.0,"green":0.0,"yellow":0.0,"white":0.0},"three":{"red":0.0,"blue":0.0833333333,"green":0.0833333333,"yellow":0.0,"white":0.0833333333},"four":{"red":0.0833333333,"blue":0.0833333333,"green":0.0,"yellow":0.0,"white":0.0},"five":{"red":0.0833333333,"blue":0.0,"green":0.0,"yellow":0.0,"white":0.0}},
 {"one":{"red":0.1818181818,"blue":0.0909090909,"green":0.0,"yellow":0.0,"white":0.0},"two":{"red":0.1818181818,"blue":0.0909090909,"green":0.0,"yellow":0.0,"white":0.0909090909},"three":{"red":0.0,"blue":0.0,"green":0.0,"yellow":0.0,"white":0.0},"four":{"red":0.0909090909,"blue":0.0909090909,"green":0.0,"yellow":0.0909090909,"white":0.0},"five":{"red":0.0909090909,"blue":0.0,"green":0.0,"yellow":0.0,"white":0.0}},
 {"one":{"red":0.0,"blue":0.0,"green":0.0,"yellow":0.0,"white":0.0},"two":{"red":0.0,"blue":0.3333333333,"green":0.0,"yellow":0.0,"white":0.3333333333},"three":{"red":0.0,"blue":0.0,"green":0.0,"yellow":0.0,"white":0.0},"four":{"red":0.0,"blue":0.3333333333,"green":0.0,"yellow":0.0,"white":0.0},"five":{"red":0.0,"blue":0.0,"green":0.0,"yellow":0.0,"white":0.0}}]
    for tile,expect in zip(tiles, expected):
        a=tile.prob_matrix(seen)
        b=pd.DataFrame(expect)
        pd.testing.assert_frame_equal(a, b)


def test_add_info():
    h = Hand()
    h.add_info(positions=[0, 3], info="one")
    assert h == Hand([Tile(colors=[1, 1, 1, 1, 1], numbers=[1, 0, 0, 0, 0]), Tile(colors=[1, 1, 1, 1, 1], numbers=[0, 1, 1, 1, 1]), Tile(colors=[1, 1, 1, 1, 1], numbers=[0, 1, 1, 1, 1]), Tile(colors=[1, 1, 1, 1, 1], numbers=[1, 0, 0, 0, 0])])

    h = Hand()
    h.add_info(positions=[0, 1], info="red")
    assert h == Hand([Tile(colors=[1, 0, 0, 0, 0], numbers=[1, 1, 1, 1, 1]), Tile(colors=[1, 0, 0, 0, 0], numbers=[1, 1, 1, 1, 1]), Tile(colors=[0, 1, 1, 1, 1], numbers=[1, 1, 1, 1, 1]), Tile(colors=[0, 1, 1, 1, 1], numbers=[1, 1, 1, 1, 1])])

def test_drop_tile():
    h = Hand([Tile(colors=[1, 0, 0, 0, 0], numbers=[1, 1, 1, 1, 1]), Tile(colors=[1, 0, 0, 0, 0], numbers=[1, 1, 1, 1, 1]), Tile(colors=[0, 1, 1, 1, 1], numbers=[1, 1, 1, 1, 1]), Tile(colors=[0, 1, 1, 1, 1], numbers=[1, 1, 1, 1, 1])])
    h.drop_tile(0)
    assert h == Hand(
        [
            Tile(colors=[1, 1, 1, 1, 1], numbers=[1, 1, 1, 1, 1]),
            Tile(colors=[1, 0, 0, 0, 0], numbers=[1, 1, 1, 1, 1]),
            Tile(colors=[0, 1, 1, 1, 1], numbers=[1, 1, 1, 1, 1]),
            Tile(colors=[0, 1, 1, 1, 1], numbers=[1, 1, 1, 1, 1]),
        ])

def test_add_new_sighting():
    seen = pd.DataFrame(
            np.array( [0]*25 ).reshape(5, 5),
            index=hanabi.colors,
            columns=hanabi.numbers,
            )

    add_new_sighting("1r", seen)
    pd.testing.assert_frame_equal(seen,
            pd.DataFrame({"one":{"red":1,"blue":0,"green":0,"yellow":0,"white":0},"two":{"red":0,"blue":0,"green":0,"yellow":0,"white":0},"three":{"red":0,"blue":0,"green":0,"yellow":0,"white":0},"four":{"red":0,"blue":0,"green":0,"yellow":0,"white":0},"five":{"red":0,"blue":0,"green":0,"yellow":0,"white":0}})
            )

    add_new_sighting("b3", seen)
    pd.testing.assert_frame_equal(seen,
            pd.DataFrame({"one":{"red":1,"blue":0,"green":0,"yellow":0,"white":0},"two":{"red":0,"blue":0,"green":0,"yellow":0,"white":0},"three":{"red":0,"blue":1,"green":0,"yellow":0,"white":0},"four":{"red":0,"blue":0,"green":0,"yellow":0,"white":0},"five":{"red":0,"blue":0,"green":0,"yellow":0,"white":0}}))

    add_new_sighting("W5", seen)
    pd.testing.assert_frame_equal(seen,
            pd.DataFrame({"one":{"red":1,"blue":0,"green":0,"yellow":0,"white":0},"two":{"red":0,"blue":0,"green":0,"yellow":0,"white":0},"three":{"red":0,"blue":1,"green":0,"yellow":0,"white":0},"four":{"red":0,"blue":0,"green":0,"yellow":0,"white":0},"five":{"red":0,"blue":0,"green":0,"yellow":0,"white":1}}))

    add_new_sighting("2Y", seen)
    pd.testing.assert_frame_equal(seen,
            pd.DataFrame({"one":{"red":1,"blue":0,"green":0,"yellow":0,"white":0},"two":{"red":0,"blue":0,"green":0,"yellow":1,"white":0},"three":{"red":0,"blue":1,"green":0,"yellow":0,"white":0},"four":{"red":0,"blue":0,"green":0,"yellow":0,"white":0},"five":{"red":0,"blue":0,"green":0,"yellow":0,"white":1}}))


def test_probs():
    h = Hand()
    seen=pd.DataFrame({"one":{"red":1,"blue":0,"green":0,"yellow":0,"white":0},"two":{"red":0,"blue":0,"green":0,"yellow":0,"white":0},"three":{"red":0,"blue":0,"green":0,"yellow":0,"white":0},"four":{"red":0,"blue":0,"green":0,"yellow":0,"white":0},"five":{"red":0,"blue":0,"green":0,"yellow":0,"white":0}})
    h.probs(seen)
