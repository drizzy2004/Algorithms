from copy import deepcopy as copy
import argparse
from animation import draw

class Node():
    def __init__(self, board, jumpfrom = None, jumpover = None, jumpto = None):
        self.board = board
        self.jumpfrom = jumpfrom
        self.jumpover = jumpover
        self.jumpto = jumpto

class peg:
    def __init__(self, start_row, start_col, rule):
        self.size = 5
        self.start_row, self.start_col, self.rule = start_row, start_col, rule
        # board
        self.board = [[1 for j in range(i+1)] for i in range(self.size)]
        self.board[start_row][start_col] = 0
        self.start = Node(copy(self.board))
        # path
        self.path = []
        # Do some initialization work here if you need:
        self.path.append(Node(copy(self.board)))



    def draw(self):
        if self.success():
            draw(self.path, self.start_row, self.start_col, self.rule)
        else:
            print("No solution were found!")


    def success(self):
        total = 0
        for row in self.board:
            for piece in row:
                if piece == 1:
                    total += 1

        if total == 1:
            if self.rule == 1 and self.path[-1].jumpto != (self.start_row, self.start_col):
                return False
            return True

        return False

    def find_all_jumps(self):
        jumps = []
        change_in_rows = [-2, -2, 2, 2, 0, 0]
        change_in_cols = [0, -2, 0, 2, -2, 2]

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                for move in range(6):

                    if not (0 <= row + change_in_rows[move] < len(self.board) and 0 <= col + change_in_cols[move] < len(self.board[row + change_in_rows[move]])):
                        continue

                    jump_from = (row, col)
                    if self.board[row][col] != 1:
                        continue

                    dr, dc = change_in_rows[move], change_in_cols[move]
                    jump_over = (row + dr // 2, col + dc // 2)
                    jump_to = (row + dr, col + dc)

                    if self.board[jump_over[0]][jump_over[1]] != 1 or self.board[jump_to[0]][jump_to[1]] != 0:
                        continue

                    # Update all pieces to correct values
                    current_board = copy(self.board)
                    current_board[jump_from[0]][jump_from[1]] = 0
                    current_board[jump_over[0]][jump_over[1]] = 0
                    current_board[jump_to[0]][jump_to[1]] = 1

                    jumps.append(Node(current_board, jump_from, jump_over, jump_to))

        return jumps
        
    def solve(self):
        if self.success():
            return True

        all_jumps = self.find_all_jumps()

        for jump in all_jumps:
            current_board = copy(self.board)
            self.board = jump.board
            self.path.append(jump)

            if self.solve():
                return True

            self.board = current_board
            self.path.pop()

        return False


        
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='peg game')

    parser.add_argument('-hole', dest='position', required = True, nargs = '+', type = int, help='initial position of the hole')
    parser.add_argument('-rule', dest='rule', required = True, type = int, help='index of rule')

    args = parser.parse_args()

    start_row, start_col = args.position
    if start_row > 4:
        print("row must be less or equal than 4")
        exit()
    if start_col > start_row:
        print("column must be less or equal than row")
        exit()

    # Example: 
    # python peg.py -hole 0 0 -rule 0
    game = peg(start_row, start_col, args.rule)
    game.solve()
    game.draw()
    