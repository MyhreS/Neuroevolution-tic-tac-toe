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

    def get_best_move_from_network(self, net):
        # Make the network rank the possible moves. It will move to the highest ranked move.
        board_states, moves = self.game.find_possible_boards()
        predictions = [net.activate(board_state) for board_state in board_states]
        move = np.argmax(predictions)
        return int(move)

    def get_random_move(self):
        move = random.randint(0, self.game.board_size ** 2 - 1)
        return move

    def get_best_move_from_minimax(self):
        # This function returns the best possible move for the minimax player

        # Helper function to check if the game is over
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

        # The main minimax function
        def minimax(board, depth, is_maximizing):
            result = check_winner(board)
            if result != 0:
                return result

            best_score = -float("inf") if is_maximizing else float("inf")
            update_best_score = max if is_maximizing else min

            for i in range(9):
                if board[i] == 0:
                    board[i] = 2 if is_maximizing else 1
                    score = minimax(board, depth + 1, not is_maximizing)
                    board[i] = 0
                    best_score = update_best_score(score, best_score)
            return best_score

        board = self.game.board.copy()
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

    def play_individual_opponent(self, genome1, genome2, config):
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
                        move = self.get_best_move_from_network(net1)
                    else:
                        move = self.get_best_move_from_network(net2)
                else:
                    if self.game.player_turn == 1:
                        move = self.get_best_move_from_network(net2)
                    else:
                        move = self.get_best_move_from_network(net1)
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
            # TODO: Play the get_best_move_from_network against dumb and a smart bot and give additional fitness if the get_best_move_from_network win.

    def play_random_move_opponent(self, genome1, config):
        """
        The get_best_move_from_network will play a dumb bot 5 times that does random moves,
        """
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        self.genome1 = genome1
        for i in range(50):
            game_over = False
            while not game_over:
                # Make move
                if self.game.player_turn == 1:
                    move = self.get_best_move_from_network(net1)
                else:
                    move = self.get_random_move()
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

    def play_minimax_algorithm_opponent(self, genome1, config):
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        self.genome1 = genome1

        game = TicTacToe(3)
        for i in range(50):
            game_over = False
            while not game_over:
                if game.check_player_turn(2):
                    move = self.get_best_move_from_network(net1)
                else:
                    move = self.get_best_move_from_minimax()
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



def run_population_with_neat(config, save_path, generations, opponent="individuals"):
    def run(genomes, config, opponent="individuals"):
        if opponent == "minimax":
            for i, (genome_id1, genome1) in enumerate(genomes):
                genome1.fitness = 0
                game = TicTacToeGame(3)
                game.play_minimax_algorithm_opponent(genome1, config)
        elif opponent == "random":
            for i, (genome_id1, genome1) in enumerate(genomes):
                genome1.fitness = 0
                game = TicTacToeGame(3)
                game.play_random_move_opponent(genome1, config)
        elif opponent == "individuals":
            for i, (genome_id1, genome1) in enumerate(genomes):
                genome1.fitness = 0
                for genome_id2, genome2 in random.sample(genomes, len(genomes)):
                    game = TicTacToeGame(3)
                    genome2.fitness = 0 if genome2.fitness is None else genome2.fitness
                    game.play_individual_opponent(genome1, genome2, config)
        else:
            raise ValueError("Opponent must be either 'individuals', 'random' or 'minimax'")

    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(lambda genomes, config: run(genomes, config, opponent=opponent), generations)
    with open(save_path, "wb") as f:
        pickle.dump(winner, f)


"""
This is a function that test the champion against a human player.
"""
def human_play_against_champion(path_to_champion):
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    with open(path_to_champion, "rb") as f:
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


"""
This is a function that evolves network individuals using NEAT against a specified opponent. It saves the champion to a file.
"""
def evolve_a_champion(save_path, generations, opponent="individuals"):
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    run_population_with_neat(config, save_path, generations, opponent=opponent)


