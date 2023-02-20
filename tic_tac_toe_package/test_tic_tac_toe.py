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
        self.assertTrue(game.check_win(1))

        game.board = [0, 0, 0, 2, 2, 2, 0, 0, 0]
        self.assertTrue(game.check_win(2))

        game.board = [0, 0, 0, 0, 0, 0, 2, 2, 2]
        self.assertTrue(game.check_win(2))

        game.board = [1, 0, 0, 0, 1, 0, 0, 0, 1]
        self.assertTrue(game.check_win(1))

        game.board = [0, 0, 2, 0, 2, 0, 2, 0, 0]
        self.assertTrue(game.check_win(2))

        game.board = [0, 2, 0, 2, 0, 0, 2, 0, 0]
        self.assertFalse(game.check_win(2))

        game.board = [1, 0, 0, 0, 1, 0, 0, 0, 0]
        self.assertFalse(game.check_win(1))

    def test_check_tie(self):
        game = TicTacToe(3)
        game.board = [1, 2, 1, 1, 1, 2, 2, 1, 2]
        self.assertTrue(game.check_tie())

        game.board = [1, 2, 1, 1, 1, 2, 2, 0, 2]
        self.assertFalse(game.check_tie())

    def test_encode_to_NN(self):
        game = TicTacToe(3)
        game.board = [1, 2, 1, 1, 1, 2, 2, 0, 2]
        encoded_to_NN = game.encode_to_NN()
        self.assertEqual(encoded_to_NN, [1, 2, 1, 1, 1, 2, 2, 0, 2, 1])

if __name__ == '__main__':
    unittest.main()