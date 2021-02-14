from copy import deepcopy

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
        self.puzzle = [[1, 2, 3],
                       [4, 0, 6],
                       [7, 5, 8]
                       ]

    def create_custom_puzzle(self):
        """
        Selection 2: Allows user to define a custom puzzle.
        """
        custom_puzzle = []
        print('Enter your puzzle, use a zero to represent the blank, and exit to'
              + 'complete your custom puzzle')
        while True:
            user_selection = \
                input('Enter the row, use space or tabs between numbers\t')

            if user_selection == 'exit':
                break
            else:
                row_list = user_selection.split(" ")
                row_list = [int(i) for i in row_list]
                custom_puzzle.append(row_list)
                continue

        self.puzzle = custom_puzzle
        print(self.puzzle)

    def get_index_value(self, puzzle_index1, puzzle_index2):
        """
        Returns the contents at tuple index.

        Args:
            puzzle_index1 (int): First index of the puzzle tuple
            puzzle_index2 (int): Second index of the puzzle tuple
        """
        return self.puzzle[puzzle_index1][puzzle_index2]

    def get_blank_space_index(self):
        """
        Finds and returns the index of the blank space.
        """
        blank_space_indices = []
        for index, list in enumerate(self.puzzle):
            if 0 in list:
                blank_space_indices.extend((index, list.index(0)))
        
        return blank_space_indices

    def get_puzzle_array_size(self):
        """
        Returns the size of the puzzle indices, and the length of each list.
        """
        list_size = len(self.get_puzzle()[0])
        puzzle_size = len(self.get_puzzle())

        return [puzzle_size, list_size]