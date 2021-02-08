import pytest
from puzzle import Puzzle

@pytest.fixture
def default_puzzle():
    puzzle_fixture = Puzzle()
    puzzle_fixture.create_default_puzzle()
    return puzzle_fixture

def test_set_values():
    expected = [[5, 3, 4],
                [8, 6, 2],
                [7, 0, 5]
                ]
    puzzle = Puzzle()
    puzzle.create_default_puzzle()
    puzzle.set_puzzle(0, 0, 5)
    assert expected == puzzle.get_puzzle()

def test_get_puzzle(default_puzzle):
    expected = [[1, 3, 4],
                [8, 6, 2],
                [7, 0, 5]
                ] 

    assert expected == default_puzzle.get_puzzle()

def test_shift_value_up():
    expected = [[1, 3, 4],
                [8, 0, 2],
                [7, 6, 5]
                ] 

    puzzle = Puzzle()
    puzzle.create_default_puzzle()
    puzzle.shift_value_up(2, 1)

    assert expected == puzzle.get_puzzle()

def test_shift_value_down():
    expected = [[1, 6, 4],
                [8, 0, 2],
                [7, 0, 5]
                ] 

    puzzle = Puzzle()
    puzzle.create_default_puzzle()
    puzzle.set_puzzle(0, 1, 0)
    puzzle.shift_value_down(0, 1)

    assert expected == puzzle.get_puzzle()

def test_shift_value_right():
    expected = [[1, 3, 4],
                [8, 6, 2],
                [7, 5, 0]
                ]
    puzzle = Puzzle()
    puzzle.create_default_puzzle()
    puzzle.shift_value_right(2, 1)

    assert expected == puzzle.get_puzzle()

def test_shift_value_left():
    expected = [[1, 3, 4],
                [8, 6, 2],
                [0, 7, 5]
                ]
    puzzle = Puzzle()
    puzzle.create_default_puzzle()
    puzzle.shift_value_left(2, 1)

    assert expected == puzzle.get_puzzle()