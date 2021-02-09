from itertools import chain
from puzzle import Puzzle
import heapq

class Solver:
    def __init__(self, algorithm, puzzle):
        if not isinstance(puzzle, Puzzle):
            raise TypeError('puzzle must be an instance of the Puzzle class.')
        self.puzzle = puzzle
        self.algorithm = algorithm
        self.heuristic = self.get_heuristic()
        self.goal_state = self.generate_goal_state()

    def get_heuristic(self):
        """
        Sets the heuristic based on the user's chosen algorithm.
        """
        # If Uniform Cost Search or A* with Manhattan Distance heuristic
        if self.algorithm == '1' or self.algorithm == '3':
            self.heuristic = 'eucledian'
        # Else if A* with Misplaced Tile Heuristic
        elif self.algorithm == '2':
            self.heuristic = 'misplaced_tiles'

    def general_search(self):
        if self.puzzle.get_puzzle() == self.goal_state:
            return 'Solved'
    
    def generate_goal_state(self):
        """
        Sets the goal state during initialization of Solver class.
        """
        flat_list = list(chain.from_iterable(self.puzzle.get_puzzle()))
        flat_list = \
            sorted(flat_list, key = lambda x: x if x > 0 else float('Inf'))
        
        list_size = len(self.puzzle.get_puzzle()[0])
        puzzle_size = len(self.puzzle.get_puzzle())

        goal_state = []
        k = 0

        for i in range(0, puzzle_size):
            idx = []
            for j in range(0, list_size):
                idx.append(flat_list[k])
                k += 1
                
            goal_state.append(idx)

        self.goal_state = goal_state