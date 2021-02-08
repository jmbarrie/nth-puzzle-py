import pytest
from puzzle import Puzzle

@pytest.fixture
def default_puzzle():
    puzzle_fixture = Puzzle()
    puzzle_fixture.create_default_puzzle()
    return puzzle_fixture

def test_set_values():
    expected = [[5, 2, 3],
                [4, 0, 6],
                [7, 5, 8]
                ]
    puzzle = Puzzle()
    puzzle.create_default_puzzle()
    puzzle.set_puzzle(0, 0, 5)
    assert expected == puzzle.get_puzzle()

def test_get_puzzle(default_puzzle):
    expected = [[1, 2, 3],
                [4, 0, 6],
                [7, 5, 8]
                ] 

    assert expected == default_puzzle.get_puzzle()

def test_shift_value_up():
    expected = [[1, 0, 3],
                [4, 2, 6],
                [7, 5, 8]
                ] 

    puzzle = Puzzle()
    puzzle.create_default_puzzle()
    puzzle.shift_value_up(1, 1)

    assert expected == puzzle.get_puzzle()

def test_shift_value_down():
    expected = [[1, 2, 3],
                [4, 5, 6],
                [7, 0, 8]
                ] 

    puzzle = Puzzle()
    puzzle.create_default_puzzle()
    puzzle.shift_value_down(1, 1)

    assert expected == puzzle.get_puzzle()

def test_shift_value_right():
    expected = [[1, 2, 3],
                [4, 6, 0],
                [7, 5, 8]
                ]
    puzzle = Puzzle()
    puzzle.create_default_puzzle()
    puzzle.shift_value_right(1, 1)

    assert expected == puzzle.get_puzzle()

def test_shift_value_left():
    expected = [[1, 2, 3],
                [0, 4, 6],
                [7, 5, 8]
                ]
    puzzle = Puzzle()
    puzzle.create_default_puzzle()
    puzzle.shift_value_left(1, 1)

    assert expected == puzzle.get_puzzle()