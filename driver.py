from puzzle import Puzzle

def main():
    test = Puzzle()
    print('Nth Puzzle Solver')
    user_selection = input('"1" for default 8 Puzzle\n')

    if user_selection == '1':
        print('Creating default puzzle')
        test.create_default_puzzle()

    print('Puzzle generated')
    test.print_puzzle()

if __name__ == "__main__":
    main()