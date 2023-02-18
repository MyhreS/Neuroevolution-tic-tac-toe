from tic_tac_toe_package import TicTacToe

game = TicTacToe(4)
game.print_board()
game.make_move(2, 0)
game.make_move(2, 5)
game.make_move(2, 10)
game.make_move(2, 15)
game.print_board()
print(game.check_win(2))