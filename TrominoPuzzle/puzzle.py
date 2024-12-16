
import argparse
import draw

# class of board
# every board is an object of the class Board 
class Board:
    def __init__(self, left, right, bottom, top):
        self.left, self.right, self.bottom, self.top = left, right, bottom, top
    
    # call this method to return four boundaries of the board 
    def get_boundary(self):
        return self.left, self.right, self.bottom, self.top

class Puzzle:
    def __init__(self, size, block):
        # size is the size of board. 
        # block is the position (x,y) of the block 
        
        # fill the initial block as black
        draw.draw_one_square(block, 'k')
        # draw the grid on the board 
        draw.grid(size)

        # create the board at full size 
        board = Board(1, size, 1, size) 
        # call solve to fill the Tromino recursively using divide and conquer 
        self.solve(block, board)
        
        # show and save the result in a picture 
        draw.save_and_show(size, block)

    def solve(self, block, board):
        # block is a position (row, column) and board is an object of Board class 
        # recursively call solve() on four small size boards with only one block on each board
        # stop the recursive call when reaching to the base case, which is board 2*2
        #  
        # call draw.draw_one_tromino(type, board) to draw one type of tromino at the center of the board. The type of the tromino is an integer 1 to 4 as explained in the instruction and the board is an object of Board class where you want to draw the tromino at its center. 
       
        left, right, bottom, top = board.get_boundary()

        column_center, row_center  = (left + right) // 2, (bottom + top) // 2

        quadrant1 = Board(column_center + 1, right, row_center + 1, top)
        quadrant2 = Board(left, column_center, row_center + 1, top)
        quadrant3 = Board(left, column_center, bottom, row_center)
        quadrant4 = Board(column_center + 1, right, bottom, row_center)

        tromino_type = self.get_tromino_type(block, board)

        draw.draw_one_tromino(tromino_type, board)

        if left == right - 1 and bottom == top -1:
            draw.draw_one_tromino(tromino_type, board)
            return board

        else:
            if block[0] > row_center and block[1] > column_center:
                self.solve(block, quadrant1)
            else:
                self.solve((row_center + 1, column_center + 1), quadrant1)

            if block[0] > row_center and block[1] <= column_center:
                self.solve(block, quadrant2)
            else:
                self.solve((row_center + 1, column_center), quadrant2)

            if block[0] <= row_center and block[1] <= column_center:
                self.solve(block, quadrant3)
            else:
                self.solve((row_center, column_center), quadrant3)

            if block[0] <= row_center and block[1] > column_center:
                self.solve(block, quadrant4)
            else:
                self.solve((row_center, column_center + 1), quadrant4)

    def get_tromino_type(self, block, board):
        # Get the boundaries of the board
        left, right, bottom, top = board.get_boundary()
        column_center, row_center = (left + right) // 2, (bottom + top) // 2

        # Dictionary for corner checks
        corners = {
            (top, right): 1,
            (top, left): 2,
            (bottom, left): 3,
            (bottom, right): 4
        }

        # Check if the block is at a corner
        if block in corners.keys():
            return corners[block]

        # Determine the tromino type based on the block's position relative to the center
        if block[0] > row_center:
            if block[1] > column_center:
                return 1  # Bottom-right
            else:
                return 2  # Bottom-left
        else:
            if block[1] > column_center:
                return 4  # Top-right
            else:
                return 3  # Top-left

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='puzzle')

    parser.add_argument('-size', dest='size', required = True, type = int, help='size of the board: 2^n')
    parser.add_argument('-block', dest='block', required = True, nargs='+', type = int, help='position of the initial block')

    args = parser.parse_args()

    # size must be a positive integer 2^n
    # block must be two integers between 1 and size 
    game = Puzzle(args.size, tuple(args.block))

    # game = puzzle(8, (1,1))
    # python puzzle.py -size 8 -block 1 1