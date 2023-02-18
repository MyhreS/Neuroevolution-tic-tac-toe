
class TicTacToe:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def print_board(self):
        print(self.board[0:3])
        print(self.board[3:6])
        print(self.board[6:9])
