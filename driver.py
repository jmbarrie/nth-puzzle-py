from puzzle import Puzzle
from solver import Solver
from itertools import chain

def solve(algorithm_selection, puzzle):
    solver = Solver(algorithm_selection, puzzle)
    solver.general_search()

def main():
    puzzle = Puzzle()
    print("Welcome to Juan's N-th puzzle solver.")

    while True:
        user_selection = input('"1" for default 8 puzzle, or "2" for a custom puzzle\n')

        if user_selection == '1':
            print('Creating default puzzle\n')
            puzzle.create_default_puzzle()
            break
        elif user_selection == '2':
            print('Creating custom puzzle\n')
            puzzle.create_custom_puzzle()
            break
        else:
            print('Please enter "1" or "2".')
            continue

    while True:
        algorithm_selection = input('Enter your choice of algorithm\n'
                                     '\t1. Uniform Cost Search\n' 
                                     '\t2. A* with the Misplaced Tile Heuristic\n' 
                                     '\t3. A* with the Manhattan Distance Heuristic\n')
        if algorithm_selection == "1":
            print('Uniform Cost Search selected')
            break
        elif algorithm_selection == "2":
            print('A* with Misplaced Tile Heuristic selected')
            break
        elif algorithm_selection == "3":
            print('A* with Manhattan Distance Heuristic Selected')
            break
        else:
            print('Sorry, please choose a valid algorithm')
            continue

    solve(algorithm_selection, puzzle)

if __name__ == "__main__":
    main()