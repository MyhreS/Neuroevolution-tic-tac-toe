class TicTacToe:
    def __init__(self, board_size):
        self.board = [0] * (board_size**2)
        self.player_turn = 1
        self.board_size = board_size

    def print_board(self):
        for i in range(self.board_size):
            print(self.board[i*self.board_size:(i+1)*self.board_size])
        print()

    def board_positions(self):
        return self.board_size*self.board_size

    def check_player_turn(self, player):
        return self.player_turn == player

    def make_move(self, player, position):
        # Check if position is already taken
        if self.board[position] != 0:
            return False
        # Make the move
        self.board[position] = player

        # Change player turn
        if self.player_turn == 1:
            self.player_turn = 2
        else:
            self.player_turn = 1
        return True

    def check_win(self, player):
        # Check rows
        for i in range(self.board_size):
            row_start = i * self.board_size
            row_end = (i + 1) * self.board_size
            if all(self.board[j] == player for j in range(row_start, row_end)):
                return True

        # Check columns
        for i in range(self.board_size):
            if all(self.board[j*self.board_size+i] == player for j in range(self.board_size)):
                return True

        # Check diagonals
        if all(self.board[i*self.board_size+i] == player for i in range(self.board_size)):
            return True
        if all(self.board[i*self.board_size+(self.board_size-1-i)] == player for i in range(self.board_size)):
            return True

        # No win
        return False

    def check_tie(self):
        for i in range(self.board_size**2):
            if self.board[i] == 0:
                return False
        return True