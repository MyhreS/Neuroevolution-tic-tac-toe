class TicTacToe:
    def __init__(self, board_size):
        """
        Initializes a new instance of the TicTacToe class.

        Parameters:
            board_size (int): The size of the game board.
        """
        self.board = [0] * (board_size**2)
        self.player_turn = 1
        self.board_size = board_size

    def print_board(self):
        """
        Prints the current state of the game board to the console.
        """
        for i in range(self.board_size):
            print(self.board[i*self.board_size:(i+1)*self.board_size])
        print()

    def board_positions(self):
        """
        Returns the total number of positions on the game board.

        Returns:
            int: The total number of positions on the game board.
        """
        return self.board_size*self.board_size

    def check_player_turn(self, player):
        """
        Checks if it is currently the specified player's turn.

        Parameters:
            player (int): The player to check (1 or 2).

        Returns:
            bool: True if it is the specified player's turn, False otherwise.
        """
        return self.player_turn == player

    def make_move(self, player, position):
        """
        Makes a move on the game board.

        Parameters:
            player (int): The player making the move (1 or 2).
            position (int): The position on the game board to make the move (0 to board_size**2-1).

        Returns:
            bool: True if the move was made successfully, False otherwise.
        """
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
        """
        Checks if the specified player has won the game.

        Parameters:
            player (int): The player to check (1 or 2).

        Returns:
            bool: True if the specified player has won, False otherwise.
        """
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
        """
        Checks if the game is tied (i.e., all positions on the game board are occupied and no player has won).

        Returns:
            bool: True if the game is tied, False otherwise.
        """
        for i in range(self.board_size**2):
            if self.board[i] == 0:
                return False
        return True

    def encode_board(self):
        """
        Encodes the current state of the game board as a single integer.

        Returns:
            int: The encoded game board as a single integer.
        """
        board_as_string = ''
        for i in self.board:
            board_as_string += str(i)
        return int(board_as_string)

