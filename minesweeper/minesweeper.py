import random

# board object to represent mineseeper game
# can be used for create board obj, dig here, render display
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #create board
        self.board = self.make_new_board()

        # init set to keep track of already dug locations
        self.dug = set()

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

# play game
def play(dim_size=10, num_bombs=10):
    #1. create the board and plant the bombs
    #2. display board to the user, ask for input (x,y)
    #3. a. if (x,y) is a bomb, display game over!
    #3. b. if (x,y) is not a bomb, dig recursively until each square is
    #      at least next to a bomb.
    #4. repeat step 2 and 3a/b until no more candidate locations to dig,
    #   display user is Winner!
    pass