import math
import os
import pickle
import random

import numpy as np
import neat
from tic_tac_toe_package import TicTacToe

class TicTacToeGame:
    def __init__(self, board_size):
        self.game = TicTacToe(board_size)

    def network(self, net):
        # Make the network rank the possible moves. It will move to the highest ranked move.
        board_states, moves = self.game.find_possible_boards()
        predictions = []
        for board_state in board_states:
            predictions.append(net.activate(board_state))
        move = np.argmax(predictions)
        return int(move)

    def dumb_bot(self):
        move = random.randint(0, self.game.board_size ** 2 - 1)
        return move

    def smart_network(self):
        # This function returns the best possible move for the minimax player
        def minimax(board, depth, is_maximizing):
            def check_winner(board):
                # Check for horizontal wins
                for i in range(0, 9, 3):
                    if board[i] == board[i + 1] and board[i + 1] == board[i + 2] and board[i] != 0:
                        return board[i]

                # Check for vertical wins
                for i in range(3):
                    if board[i] == board[i + 3] and board[i + 3] == board[i + 6] and board[i] != 0:
                        return board[i]

                # If there are no winners yet
                return 0

            # Check if the game is over
            result = check_winner(board)
            if result != 0:
                return result

            # If the minimax player is maximizing
            if is_maximizing:
                best_score = -float("inf")
                for i in range(9):
                    if board[i] == 0:
                        board[i] = 2
                        score = minimax(board, depth + 1, False)
                        board[i] = 0
                        best_score = max(score, best_score)
                return best_score

            # If the minimax player is minimizing
            else:
                best_score = float("inf")
                for i in range(9):
                    if board[i] == 0:
                        board[i] = 1
                        score = minimax(board, depth + 1, True)
                        board[i] = 0
                        best_score = min(score, best_score)
                return best_score

        board = self.game.board.copy()
        # This function returns the index of the best possible move for the minimax player
        best_score = -float("inf")
        best_move = -1
        for i in range(9):
            if board[i] == 0:
                board[i] = 2
                score = minimax(board, 0, False)
                board[i] = 0
                if score > best_score:
                    best_score = score
                    best_move = i
            return best_move

    def play_genome(self, genome1, genome2, config):
        """
        Train the AI by passing two NEAT neural networks and the NEAT config object.
        These AI's will play against each other to determine their fitness.
        """

        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)
        self.genome1 = genome1
        self.genome2 = genome2

        for round_number in range(2):
            game_over = False
            while not game_over:
                # Make move
                if round_number == 1:
                    if self.game.player_turn == 1:
                        move = self.network(net1)
                    else:
                        move = self.network(net2)
                else:
                    if self.game.player_turn == 1:
                        move = self.network(net2)
                    else:
                        move = self.network(net1)
                self.game.make_move(move)

                # Find out if the game is over
                board_state = self.game.check_board_state()
                if board_state == 1:
                    self.genome1.fitness += 1
                    game_over = True
                elif board_state == 2:
                    self.genome2.fitness += 1
                    game_over = True
                elif board_state == 3:
                    self.genome1.fitness += 0.2
                    self.genome2.fitness += 0.2
                    game_over = True
            self.game.reset_game()
            # TODO: Play the network against dumb and a smart bot and give additional fitness if the network win.

    def play_dumb_bot(self, genome1, config):
        """
        The network will play a dumb bot 5 times that does random moves,
        """
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        self.genome1 = genome1
        for i in range(50):
            game_over = False
            while not game_over:
                # Make move
                if self.game.player_turn == 1:
                    move = self.network(net1)
                else:
                    move = self.dumb_bot()
                self.game.make_move(move)

                # Find out if the game is over
                board_state = self.game.check_board_state()
                if board_state == 1:
                    self.genome1.fitness += 1
                    game_over = True
                elif board_state == 2:
                    game_over = True
                elif board_state == 3:
                    self.genome1.fitness += 0.2
                    game_over = True
            self.game.reset_game()

    def play_smart_bot(self, genome1, config):
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        self.genome1 = genome1

        game = TicTacToe(3)
        for i in range(50):
            game_over = False
            while not game_over:
                if game.check_player_turn(2):
                    move = self.network(net1)
                else:
                    move = self.smart_network()
                game.make_move(move)

                # Find out if the game is over
                board_state = game.check_board_state()
                if board_state == 1:
                    #print("Player 1 won")
                    self.genome1.fitness += 1
                    game_over = True
                elif board_state == 2:
                    #print("Player 2 won")
                    game_over = True
                elif board_state == 3:
                    self.genome1.fitness += 0.2
                    #print("Tie")
                    game_over = True
            game.reset_game()



# TODO: Make the net not gain fitness by tieing.
def play_genomes(genomes, config):
    """
    Make each genome play tic-tac-toe.
    """

    # 100 pr genome * 2 because of attack and defend.
    """
    for i, (genome_id1, genome1) in enumerate(genomes):
        genome1.fitness = 0
        for genome_id2, genome2 in random.sample(genomes, len(genomes)):
            game = TicTacToeGame(3)
            genome2.fitness = 0 if genome2.fitness is None else genome2.fitness
            game.play_genome(genome1, genome2, config)
    """
    
    """
    for i, (genome_id1, genome1) in enumerate(genomes):
        genome1.fitness = 0
        game = TicTacToeGame(3)
        game.play_dumb_bot(genome1, config)
    """
    for i, (genome_id1, genome1) in enumerate(genomes):
        genome1.fitness = 0
        game = TicTacToeGame(3)
        game.play_smart_bot(genome1, config)

def run_population_with_neat(config):
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    #p.add_reporter(neat.Checkpointer(1))

    winner = p.run(play_genomes, 500)
    with open("best_against_smart_bot.pickle", "wb") as f:
        pickle.dump(winner, f)

def test_best_network(config):
    with open("best_against_smart_bot.pickle", "rb") as f:
        winner = pickle.load(f)
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

    game = TicTacToe(3)
    game_over = False
    game.print_board()
    while not game_over:
        if game.check_player_turn(1):
            board_states, moves = game.find_possible_boards()
            predictions = []
            for board_state in board_states:
                predictions.append(winner_net.activate(board_state))
            move = np.argmax(predictions)
        else:
            # Human player, input int between 1 and 9
            output_move = int(input("Enter move 1-9: "))
            move = output_move - 1
        game.make_move(int(move))

        game.print_board()

        # Find out if the game is over
        board_state = game.check_board_state()
        if board_state == 1:
            print("Player 1 won")
            game_over = True
        elif board_state == 2:
            print("Player 2 won")
            game_over = True
        elif board_state == 3:
            print("Tie")
            game_over = True
    game.reset_game()


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)


    run_population_with_neat(config)
    #test_best_network(config)

