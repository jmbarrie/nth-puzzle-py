from puzzle import Puzzle
from solver import Solver
from itertools import chain

def solve(algorithm_selection, puzzle):
    solver = Solver(algorithm_selection, puzzle)
    solver.general_search()

def main():
    puzzle = Puzzle()
    print('Nth Puzzle Solver')
    user_selection = input('"1" for default 8 Puzzle\n')

    if user_selection == '1':
        print('Creating default puzzle')
        puzzle.create_default_puzzle()

    print('Puzzle generated')

    while True:
        algorithm_selection = input('Choose algorithm: 1 - Uniform Cost Search, 2 - A* with Misplaced Tile Heuristic, 3 - A* with Manhattan Distance heuristic\n')
        if algorithm_selection == "1":
            print('Uniform Cost Search selected')
            break
        elif algorithm_selection == "2":
            print('A* with Misplaced Tile Heuristic selected')
            break
        elif algorithm_selection == "3":
            print('A* with Misplaced Tile Heuristic selected')
            break
        else:
            print('Sorry, please choose a valid algorithm')
            continue

    solve(algorithm_selection, puzzle)

if __name__ == "__main__":
    main()