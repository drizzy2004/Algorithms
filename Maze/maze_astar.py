import numpy as np
from heapq import heappush, heappop
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


class Maze():
    
    def __init__(self, map, start_state, goal_state, map_index):
        self.start_state = start_state
        self.goal_state = goal_state
        self.map = map
        self.visited = [] # state
        self.m, self.n = map.shape 
        self.map_index = map_index


    def draw(self, node):
        path=[]
        while node.parent:
            path.append(node.state)
            node = node.parent
        path.append(self.start_state)
    
        draw(self.map, path[::-1], self.map_index)

    def check_visited(self, state):
        for previous_visited in self.visited:
            if np.array_equal(state, previous_visited):
                return True

        return False


    def goal_test(self, current_state):
        if current_state == self.goal_state:
            return True

        return False


    def get_cost(self, current_state, next_state):
        return 1


    def get_successors(self, state):
        successors = []
        change_1 = [0, 0, -1, 1]
        change_2 = [-1, 1, 0, 0]
        row = state[0]
        col = state[1]

        for i in range(4):
            new_row = row + change_1[i]
            new_col = col + change_2[i]
            if self.map[new_row, new_col] != 0.0:
                successors.append((state[0] + change_1[i], state[1] + change_2[i]))

        return successors


    # heuristics function
    def heuristics(self, state):
        difference = abs(state[0] - self.goal_state[0]) + abs(state[1] - self.goal_state[1])
        return difference


    # priority of node 
    def priority(self, node):
        return self.heuristics(node.state) + node.cost_from_start

    
    # solve it
    def solve(self):
        node = Node(self.start_state, 0, None)
        self.visited.append(self.start_state)
        count = 0
        priority_q = [(self.priority(node), count, node)]

        # Check if game is already solved
        if self.goal_test(self.start_state):
            return

        while priority_q:
            current_node = heappop(priority_q)[2]
            successors = self.get_successors(current_node.state)

            for next_state in successors:
                if not self.check_visited(next_state):
                    self.visited.append(next_state)
                    next_node = Node(next_state, current_node.cost_from_start + self.get_cost(current_node.state, next_state), current_node)

                    if self.goal_test(next_state) is True:
                        self.draw(next_node)
                        return

                    count += 1
                    heappush(priority_q, (self.priority(next_node), count, next_node))

            
    
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='maze')
    parser.add_argument('-index', dest='index', required = True, type = int)
    index = parser.parse_args().index

    # Example:
    # Run this in the terminal solving map 1
    #     python maze_astar.py -index 1
    
    data = np.load('map_'+str(index)+'.npz')
    map, start_state, goal_state = data['map'], tuple(data['start']), tuple(data['goal'])

    game = Maze(map, start_state, goal_state, index)
    game.solve()
    