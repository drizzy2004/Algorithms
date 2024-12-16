import numpy as np
from animation import draw
import argparse

class Node():
    """
    cost_from_start - the cost of reaching this node from the starting node
    state - the state (row,col)
    parent - the parent node of this node, default as None
    """
    def __init__(self, state, cost_from_start, parent = None):
        self.state = state
        self.parent = parent
        self.cost_from_start = cost_from_start


class EightPuzzle():
    
    def __init__(self, start_state, goal_state, algorithm, array_index):
        self.start_state = start_state
        self.goal_state = goal_state
        self.visited = [] # state
        self.algorithm = algorithm
        self.m, self.n = start_state.shape 
        self.array_index = array_index

    # goal test function
    def goal_test(self, current_state):
        for i, row in enumerate(current_state):
            for j, element in enumerate(row):
                if element != self.goal_state[i][j]:
                    return False
        return True


    # get cost function
    def get_cost(self, current_state, next_state):
        return 1


    # get successor function
    def get_successors(self, state):
        successors = []
        blank_space = ()

        # your code goes here:
        for i, row in enumerate(state):
            for j, element in enumerate(row):
                if element == 0:
                    blank_space = (i, j)
                    break

        change_1 = [-1, 1, 0, 0]
        change_2 = [0, 0, 1, -1]

        for i in range(4):
            new_child = state.copy()

            if blank_space[0] + change_1[i] > 2 or blank_space[0] + change_1[i] < 0 or blank_space[1] + change_2[i] < 0 or blank_space[1] + change_2[i] > 2:
                continue

            new_child[blank_space[0], blank_space[1]] = state[blank_space[0] + change_1[i], blank_space[1] + change_2[i]]
            new_child[blank_space[0] + change_1[i], blank_space[1] + change_2[i]] = 0
            successors.append(new_child)

        return successors
    
    # draw 
    def draw(self, node):
        path=[]
        while node.parent:
            path.append(node.state)
            node = node.parent
        path.append(self.start_state)
        draw(path[::-1], self.array_index, self.algorithm)


    def check_visited(self, state):
        for previous_visited in self.visited:
            if np.array_equal(state, previous_visited):
                return True

        return False

    # solve it
    def solve(self):
        fringe = [] # node
        state = self.start_state.copy() # use copy() to copy value instead of reference 
        node = Node(state, 0, None)
        self.visited.append(state)

        # Check if game is already solved
        if self.goal_test(self.start_state):
            return

        fringe.append(node)

        while fringe:
            current_node = fringe.pop()

            if self.algorithm == "Depth-Limited-DFS" and current_node.cost_from_start > 15:
                continue

            successors = self.get_successors(current_node.state)

            for next_state in successors:
                if not self.check_visited(next_state):
                    next_cost = current_node.cost_from_start + self.get_cost(node.state, next_state)
                    next_node = Node(next_state, next_cost, current_node)

                    if self.goal_test(next_state) is True:
                        self.draw(next_node)
                        return

                    if self.algorithm == 'Depth-Limited-DFS':
                        fringe.append(next_node)

                    elif self.algorithm == 'BFS':
                        fringe.insert(0, next_node)
            
    
if __name__ == "__main__":
    
    goal = np.array([[1,2,3],[4,5,6],[7,8,0]])
    start_arrays = [np.array([[0,1,3],[4,2,5],[7,8,6]]), # easy one. use this in lab
                    np.array([[0,2,3],[1,4,6],[7,5,8]])] # medium one.

    algorithms = ['Depth-Limited-DFS', 'BFS']
    
    parser = argparse.ArgumentParser(description='eight puzzle')

    parser.add_argument('-array', dest='array_index', required = True, type = int, help='index of array')
    parser.add_argument('-algorithm', dest='algorithm_index', required = True, type = int, help='index of algorithm')

    args = parser.parse_args()

    # run this in the terminal using array 0, algorithm BFS
    # python eight_puzzle_uninform.py -array 0 -algorithm 1
    game = EightPuzzle(start_arrays[args.array_index], goal, algorithms[args.algorithm_index], args.array_index)
    game.solve()