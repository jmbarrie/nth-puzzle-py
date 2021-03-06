from copy import deepcopy

class Node:
    def __lt__(self, other):
        """
        Used for heapq comparison.
        """
        return self.f_cost < other.f_cost

    def __init__(self, initial_puzzle, parent_puzzle, g_cost, heuristic):
        self.initial_puzzle = initial_puzzle
        self.parent_puzzle = parent_puzzle
        self.g_cost = g_cost + 1
        self.h_cost = None
        self.f_cost = None 
        self.set_h_cost(heuristic)
        self.set_f_cost()

    def set_f_cost(self):
        """
        Sets the total f cost.
        """
        self.f_cost = self.get_g_cost() + self.get_h_cost()

    def set_h_cost(self, heuristic):
        """
        Sets the heuristic cost based on which algorithm was chosen.
        """
        if heuristic == 'uniform':
            self.h_cost = 0
        elif heuristic == 'misplaced_tiles':
            self.h_cost = self.set_misplaced_tiles()
        elif heuristic == 'manhattan':
            self.h_cost = self.set_manhattan_distance()

    def set_misplaced_tiles(self):
        expected = 1
        misplaced_tiles = 0
        # Returns the sizes of lists in our puzzle [0] puzzle size, [1] list size
        puzzle_array_sizes = self.initial_puzzle.get_puzzle_array_size()
        # Go through each item in our puzzle and count how many spaces away we are
        for i in range(puzzle_array_sizes[0]):
            for j in range(puzzle_array_sizes[1]):
                # If the last item is not 0, increment misplaced_tiles
                if i == puzzle_array_sizes[0] - 1 and j == puzzle_array_sizes[1] - 1:
                    if self.initial_puzzle.get_index_value(i, j) != 0:
                        misplaced_tiles += 1
                # Check each item, if they are not equal to their expected value, increment misplaced tiles
                elif self.initial_puzzle.get_index_value(i, j) != expected:
                    misplaced_tiles += 1 

                expected += 1

        return misplaced_tiles

    def set_manhattan_distance(self):
        distance = 0
        puzzle_array_sizes = self.initial_puzzle.get_puzzle_array_size()
        for i in range(puzzle_array_sizes[0]):
            for j in range(puzzle_array_sizes[1]):
                row, column = 0, 0
                temp = self.initial_puzzle.get_index_value(i, j)

                if temp != 0:
                    while temp > puzzle_array_sizes[0]:
                        temp -= puzzle_array_sizes[0]
                        row += 1
                    column = temp - 1
                else:
                    row = puzzle_array_sizes[0] - 1
                    column = puzzle_array_sizes[0] - 1

                distance += abs(row - i) + abs(column - j)

        return distance

    def get_g_cost(self):
        return self.g_cost

    def get_h_cost(self):
        return self.h_cost

    def get_parent(self):
        """
        Returns the parent puzzle.
        """
        return self.parent_puzzle

    def get_puzzle(self):
        """
        Returns the initial puzzle.
        """
        return self.initial_puzzle.get_puzzle()

    def get_blank_space_index(self):
        """
        Returns the location of the blank space.
        """
        return self.initial_puzzle.get_blank_space_index()

    def print_puzzle(self):
        """
        Prints the initial puzzle.
        """
        self.initial_puzzle.print_puzzle()

    def generate_legal_moves(self):
        """
        Generates the legal moves available based on the position of blank space
        and returns them.
        """
        blank_space_indices = self.initial_puzzle.get_blank_space_index()
        puzzle_array_sizes = self.initial_puzzle.get_puzzle_array_size()
        moves = []
        up, down, left, right = False, False, False, False

        # Check up and down moves
        # If the blank space is on the top row, or [0][n], can't move up
        # but, can move down
        if blank_space_indices[0] == 0:
            down = True
        # If the blank space is on the bottom row, or [2][n], can't move down
        # but, can move up
        elif blank_space_indices[0] == puzzle_array_sizes[0] - 1:
            up = True 
        # Otherwise, it can make an up or down movement
        else:
            up, down = True, True

        # Check left and right moves
        # If the blank space is on the left side, or [n][0], can't move left
        # but, can move right
        if blank_space_indices[1] == 0:
            right = True
        # If the blank space is on the right row, or [n][2], can't move right
        # but, can move left
        elif blank_space_indices[1] == puzzle_array_sizes[1] - 1:
            left = True
        # Otherwise, can move left and right
        else:
            left, right = True, True

        if up:
            moves.append(self.shift_value_up())
        if down:
            moves.append(self.shift_value_down())
        if right:
            moves.append(self.shift_value_right())
        if left:
            moves.append(self.shift_value_left())

        return moves

    def shift_value_up(self):
        """
        Shifts the contents at tuple index up.
        """
        blank_space_indices = self.initial_puzzle.get_blank_space_index()
        puzzle_copy = deepcopy(self.initial_puzzle)
        if(blank_space_indices[0] - 1 >= 0):
            temp_value = \
                self.initial_puzzle.get_index_value(blank_space_indices[0] - 1, blank_space_indices[1])
            puzzle_copy.set_puzzle(blank_space_indices[0] - 1, blank_space_indices[1], 0)
            puzzle_copy.set_puzzle(blank_space_indices[0], blank_space_indices[1], temp_value)
        
        return puzzle_copy

    def shift_value_down(self):
        """
        Shifts the contents at tuple index down.
        """
        blank_space_indices = self.initial_puzzle.get_blank_space_index()
        puzzle_copy = deepcopy(self.initial_puzzle)
        if(blank_space_indices[0] + 1 <= len(self.get_puzzle())):
            temp_value = self.initial_puzzle.get_index_value(blank_space_indices[0] + 1, blank_space_indices[1])
            puzzle_copy.set_puzzle(blank_space_indices[0] + 1, blank_space_indices[1], 0)
            puzzle_copy.set_puzzle(blank_space_indices[0], blank_space_indices[1], temp_value)
        
        return puzzle_copy

    def shift_value_right(self):
        """
        Shifts the contents at tuple index right.

        Args:
            blank_space_indices[0] (int): First index of the puzzle tuple
            blank_space_indices[1] (int): Second index of the puzzle tuple
        """
        blank_space_indices = self.initial_puzzle.get_blank_space_index()
        puzzle_copy = deepcopy(self.initial_puzzle)
        if(blank_space_indices[1] + 1 <= len(self.get_puzzle())):
            temp_value = self.initial_puzzle.get_index_value(blank_space_indices[0], blank_space_indices[1] + 1)
            puzzle_copy.set_puzzle(blank_space_indices[0], blank_space_indices[1] + 1, 0)
            puzzle_copy.set_puzzle(blank_space_indices[0], blank_space_indices[1], temp_value)

        return puzzle_copy

    def shift_value_left(self):
        """
        Shifts the contents at tuple index left.

        Args:
            blank_space_indices[0] (int): First index of the puzzle tuple
            blank_space_indices[1] (int): Second index of the puzzle tuple
        """
        blank_space_indices = self.initial_puzzle.get_blank_space_index()
        puzzle_copy = deepcopy(self.initial_puzzle)
        if(blank_space_indices[1] - 1 >= 0):
            temp_value = self.initial_puzzle.get_index_value(blank_space_indices[0], blank_space_indices[1] - 1)
            puzzle_copy.set_puzzle(blank_space_indices[0], blank_space_indices[1] - 1, 0)
            puzzle_copy.set_puzzle(blank_space_indices[0], blank_space_indices[1], temp_value)
    
        return puzzle_copy
