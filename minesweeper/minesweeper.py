import random

# board object to represent mineseeper game
# can be used for create board obj, dig here, render display
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #create board
        self.board = self.make_new_board()
        self.assign_values_to_board()


        # init set to keep track of already dug locations
        self.dug = set()

    #helper function
    def make_new_board(self):

        # using list of lists for 2-D board representation
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*': 
                continue

            board[row][col] = '*'
            bombs_planted += 1

    # assigns value (0-8) for all empty spaces
    # these represent how many locations far the neighboring bombs are.
    def assign_values_to_board(self):
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if self.board[row][col] == '*':
                    continue

                self.board[row][col] = self.get_number_of_neighboring_bombs(row, col)

    # iterate through all 8 neighbors and count bombs
    def get_number_of_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def dig(self, row, col):
        # dig at the location
        #  return true if success, flase if bomb dug
        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False 
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return True

    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        string_rep = ''
        
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )
        
        indices = [i for i in range(self.dim_size)]
        indices_row = '  '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            indices_row += ' |'.join(cells)
            indices_row += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep 

# play game
def play(dim_size=10, num_bombs=10):
    #1. create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    #2. display board to the user, ask for input (x,y)
    #3. a. if (x,y) is a bomb, display game over!
    #3. b. if (x,y) is not a bomb, dig recursively until each square is
    #      at least next to a bomb.
    #4. repeat step 2 and 3a/b until no more candidate locations to dig,
    #   display user is Winner!
    pass