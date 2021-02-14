import pytest
from node import Node
from puzzle import Puzzle

@pytest.fixture
def default_node():
    default_puzzle = Puzzle()
    default_puzzle.create_default_puzzle()
    return Node(default_puzzle, default_puzzle, 0)

def test_move_up(default_node):
    expected = [[1, 0, 3],
                [4, 2, 6],
                [7, 5, 8]
                ]
    default_node.print_puzzle()
    new_node = default_node.shift_value_up()
    new_node.print_puzzle()
    assert expected == new_node.get_puzzle() 

def test_move_down(default_node):
    expected = [[1, 2, 3],
                [4, 5, 6],
                [7, 0, 8]
                ]
    default_node.print_puzzle()
    new_node = default_node.shift_value_down()
    new_node.print_puzzle()
    assert expected == new_node.get_puzzle() 

def test_move_left(default_node):
    expected = [[1, 2, 3],
                [0, 4, 6],
                [7, 5, 8]
                ]
    default_node.print_puzzle()
    new_node = default_node.shift_value_left()
    new_node.print_puzzle()
    assert expected == new_node.get_puzzle() 

def test_move_right(default_node):
    expected = [[1, 2, 3],
                [4, 6, 0],
                [7, 5, 8]
                ]
    default_node.print_puzzle()
    new_node = default_node.shift_value_right()
    new_node.print_puzzle()
    assert expected == new_node.get_puzzle() 

def test_legal_moves(default_node):
    moves = default_node.generate_legal_moves()
    expected_0 = [[1, 0, 3],
                [4, 2, 6],
                [7, 5, 8]
                ]

    expected_1 = [[1, 2, 3],
                [4, 5, 6],
                [7, 0, 8]
                ]

    expected_2 = [[1, 2, 3],
                [4, 6, 0],
                [7, 5, 8]
                ]

    expected_3 = [[1, 2, 3],
                [0, 4, 6],
                [7, 5, 8]
                ]

    assert moves[0].get_puzzle() == expected_0
    assert moves[1].get_puzzle() == expected_1
    assert moves[2].get_puzzle() == expected_2
    assert moves[3].get_puzzle() == expected_3
