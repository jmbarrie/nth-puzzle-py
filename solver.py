from itertools import chain
from node import Node
from puzzle import Puzzle
from heapq import heappush, heappop

class Solver:
    def __init__(self, algorithm, puzzle):
        if not isinstance(puzzle, Puzzle):
            raise TypeError('puzzle must be an instance of the Puzzle class.')
        self.puzzle = puzzle
        self.algorithm = algorithm
        self.heuristic = None
        self.goal_state = None
        self.set_heuristic()

    def set_heuristic(self):
        """
        Sets the heuristic based on the user's chosen algorithm.
        """
        # If Uniform Cost Search or A* with Manhattan Distance heuristic
        if self.algorithm == '1' or self.algorithm == '3':
            self.heuristic = 'uniform'
        # Else if A* with Misplaced Tile Heuristic
        elif self.algorithm == '2':
            self.heuristic = 'misplaced_tiles'

    def general_search(self):
        """
        Generalized graph search using the priority queue.
        Returns success or failure of search for goal state.
        """
        self.generate_goal_state()

        if self.puzzle.get_puzzle() == self.goal_state:
            return 'Solved'

        # Stores puzzles that have already been expanded
        visited = []
        queue = []
        max_queue_size, nodes_explored = 0, 0
        parent_node = Node(self.puzzle, self.puzzle, 0, self.heuristic)
        heappush(queue, (0, parent_node))

        while queue:
            max_queue_size = max(len(queue), max_queue_size)
            lowest_cost = heappop(queue)
            current_node = lowest_cost[1]
            nodes_explored += 1

            if not current_node.get_puzzle() in visited:
                visited.append(current_node.get_puzzle())
                if current_node.get_puzzle() == self.goal_state:
                    current_node.print_puzzle()
                    print('Goal!!!')
                    print(f'To solve this problem the search algorithm expanded a total of %s nodes.' % nodes_explored)
                    print(f'The maximum number of nodes in the queue at any one time was %s.' % len(queue))
                    print(f'The depth of the goal node was %s.' % current_node.get_g_cost())
                    return 1

                if nodes_explored == 1:
                    print('Expanding state')
                    current_node.print_puzzle()
                else:
                    print(f'The best state to expand with a g(n) = %s and h(n) = %s' % (current_node.get_g_cost(), current_node.get_h_cost()))
                    current_node.print_puzzle()
                    print('Expanding this node...')

                moves = current_node.generate_legal_moves()
                for puzzle in moves:
                    next_node = Node(puzzle, current_node, current_node.get_g_cost(), self.heuristic)
                    heappush(queue, (current_node.f_cost, next_node))
        return 0
    
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

    def get_goal_state(self):
        return self.goal_state
