import unittest
from tic_tac_toe_package import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def test_init(self):
        game = TicTacToe(3)
        self.assertEqual(game.board, [0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(game.player_turn, 1)
        self.assertEqual(game.board_size, 3)

    def test_make_move(self):
        game = TicTacToe(3)
        self.assertTrue(game.make_move(1, 0))
        self.assertEqual(game.board, [1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(game.player_turn, 2)

        # Test making an invalid move
        self.assertFalse(game.make_move(1, 0))

    def test_check_win(self):
        game = TicTacToe(3)
        game.board = [1, 1, 1, 0, 0, 0, 0, 0, 0]
        self.assertTrue(game.check_win_player(1))

        game.board = [0, 0, 0, 2, 2, 2, 0, 0, 0]
        self.assertTrue(game.check_win_player(2))

        game.board = [0, 0, 0, 0, 0, 0, 2, 2, 2]
        self.assertTrue(game.check_win_player(2))

        game.board = [1, 0, 0, 0, 1, 0, 0, 0, 1]
        self.assertTrue(game.check_win_player(1))

        game.board = [0, 0, 2, 0, 2, 0, 2, 0, 0]
        self.assertTrue(game.check_win_player(2))

        game.board = [0, 2, 0, 2, 0, 0, 2, 0, 0]
        self.assertFalse(game.check_win_player(2))

        game.board = [1, 0, 0, 0, 1, 0, 0, 0, 0]
        self.assertFalse(game.check_win_player(1))

    def test_check_tie(self):
        game = TicTacToe(3)
        game.board = [1, 2, 1, 1, 1, 2, 2, 1, 2]
        self.assertTrue(game.check_tie())

        game.board = [1, 2, 1, 1, 1, 2, 2, 0, 2]
        self.assertFalse(game.check_tie())

    def test_check_board_state(self):
        game = TicTacToe(3)
        game.board = [1, 1, 1, 0, 0, 0, 0, 0, 0]
        self.assertEqual(game.check_board_state(), 1) # Player 1 wins
        game.board = [0, 0, 0, 2, 2, 2, 0, 0, 0]
        self.assertEqual(game.check_board_state(), 2) # Player 2 wins
        game.board = [1,1,2,2,2,1,1,2,1]
        self.assertEqual(game.check_board_state(), 3) # Tie
        game.board = [1,2,0,0,0,0,0,0,0]
        self.assertEqual(game.check_board_state(), 0) # No winner or tie yet

    def test_encode_to_NN(self):
        game = TicTacToe(3)
        game.board = [1,1,1,1,0,2,2,2,2]
        encoded_to_NN = game.encode_to_NN()
        self.assertEqual(encoded_to_NN, [1,1,1,1,0,2,2,2,2])
        game.player_turn = 2
        encoded_to_NN = game.encode_to_NN()
        self.assertEqual(encoded_to_NN, [2,2,2,2,0,1,1,1,1])

    def test_find_possible_boards(self):
        game = TicTacToe(3)
        game.board = [1,1,1,1,0,2,2,2,2]
        possible_boards, moves = game.find_possible_boards()
        self.assertEqual(possible_boards, [[1,1,1,1,1,2,2,2,2]])
        game.player_turn = 2
        possible_boards, moves = game.find_possible_boards()
        self.assertEqual(possible_boards, [[2,2,2,2,1,1,1,1,1]])
        self.assertEqual(moves, [4])

    def test_reset_game(self):
        game = TicTacToe(3)
        game.board = [1, 2, 1, 1, 1, 2, 2, 0, 2]
        game.player_turn = 2
        game.reset_game()
        self.assertEqual(game.board, [0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(game.player_turn, 1)

if __name__ == '__main__':
    unittest.main()