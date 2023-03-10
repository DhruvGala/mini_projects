import time
from player import HumanPlayer, GeniusComputerPlayer

class TickTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]    # we will use a single list to rep 3x3 board
        self.current_winner = None  # keep track of the winner

    def print_board(self):
        # this is just getting rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' |'.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc tells us what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' |'.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
    
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_square(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if a valid move, then assign the letter to the said square
        # return true, else just return false.
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        else:
            return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere, row, col or diag
        # let's check row first
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        #check col next
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]   # lef diag
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right diag
            if all([spot == letter for spot in diagonal2]):
                return True
    
        return False




def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'    # starting letter
    # iterate while the game still has empty squares.
    while game.empty_squares():
        # get the move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

        # pause for asthetics
        time.sleep(0.9)

    if print_game:
        print('Its a tie!')
        

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TickTacToe()

    play(t, x_player, o_player, print_game=True)