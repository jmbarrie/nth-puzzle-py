from solver import Solver
from puzzle import Puzzle
import pytest

@pytest.fixture
def default_solver_uc():
    default_puzzle = Puzzle()
    default_puzzle.create_default_puzzle()
    return Solver("1", default_puzzle)

def test_generate_goal_state(default_solver_uc):
    expected = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]]
    
    default_solver_uc.generate_goal_state()
    print(default_solver_uc.goal_state)
    assert expected == default_solver_uc.get_goal_state()