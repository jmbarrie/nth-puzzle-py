class Puzzle:
    def __init__(self):
        puzzle = None

    def get_puzzle(self):
        """
        Returns the current puzzle.
        """
        return self.puzzle

    def set_puzzle(self, puzzle_index1, puzzle_index2, new_puzzle_value):
        """
        Sets the value of the puzzle

        Args:
            puzzle_index1 (int): First index of the puzzle tuple
            puzzle_index2 (int): Second index of the puzzle tuple
            new_puzzle_value (int): Value to update 
        """

        self.puzzle[puzzle_index1][puzzle_index2] = new_puzzle_value

    def print_puzzle(self):
        """
        Outputs the current puzzle.
        """
        for row in self.puzzle:
            print(*row, sep=', ')

    def create_default_puzzle(self):
        """
        Selection 1: Generates a default puzzle for the user.
        """
        self.puzzle = [[1, 3, 4],
                       [8, 6, 2],
                       [7, 0, 5]
                       ]

    def get_index_value(self, puzzle_index1, puzzle_index2):
        """
        Returns the contents at tuple index.

        Args:
            puzzle_index1 (int): First index of the puzzle tuple
            puzzle_index2 (int): Second index of the puzzle tuple
        """
        return self.puzzle[puzzle_index1][puzzle_index2]

    def shift_value_up(self, puzzle_index1, puzzle_index2):
        """
        Shifts the contents at tuple index up.

        Args:
            puzzle_index1 (int): First index of the puzzle tuple
            puzzle_index2 (int): Second index of the puzzle tuple
        """
        if(puzzle_index1 - 1 >= 0):
            temp_value = self.get_index_value(puzzle_index1 - 1, puzzle_index2)
            self.set_puzzle(puzzle_index1 - 1, puzzle_index2, 0)
            self.set_puzzle(puzzle_index1, puzzle_index2, temp_value)

    def shift_value_down(self, puzzle_index1, puzzle_index2):
        """
        Shifts the contents at tuple index down.

        Args:
            puzzle_index1 (int): First index of the puzzle tuple
            puzzle_index2 (int): Second index of the puzzle tuple
        """
        if(puzzle_index1 + 1 <= len(self.puzzle)):
            temp_value = self.get_index_value(puzzle_index1 + 1, puzzle_index2)
            self.set_puzzle(puzzle_index1 + 1, puzzle_index2, 0)
            self.set_puzzle(puzzle_index1, puzzle_index2, temp_value)

    def shift_value_right(self, puzzle_index1, puzzle_index2):
        """
        Shifts the contents at tuple index right.

        Args:
            puzzle_index1 (int): First index of the puzzle tuple
            puzzle_index2 (int): Second index of the puzzle tuple
        """
        if(puzzle_index2 + 1 <= len(self.puzzle)):
            temp_value = self.get_index_value(puzzle_index1, puzzle_index2 + 1)
            self.set_puzzle(puzzle_index1, puzzle_index2 + 1, 0)
            self.set_puzzle(puzzle_index1, puzzle_index2, temp_value)

    def shift_value_left(self, puzzle_index1, puzzle_index2):
        """
        Shifts the contents at tuple index left.

        Args:
            puzzle_index1 (int): First index of the puzzle tuple
            puzzle_index2 (int): Second index of the puzzle tuple
        """
        if(puzzle_index2 - 1 >= 0):
            temp_value = self.get_index_value(puzzle_index1, puzzle_index2 - 1)
            self.set_puzzle(puzzle_index1, puzzle_index2 - 1, 0)
            self.set_puzzle(puzzle_index1, puzzle_index2, temp_value)