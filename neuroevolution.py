import os
import pickle
import random

import numpy as np
import neat
from tic_tac_toe_package import TicTacToe

class TicTacToeGame:
    def __init__(self, board_size):
        self.game = TicTacToe(board_size)

    def get_prediction(self, net):
        # Make the network rank the possible moves. It will move to the highest ranked move.
        board_states, moves = self.game.find_possible_boards()
        predictions = []
        for board_state in board_states:
            predictions.append(net.activate(board_state))
        move = np.argmax(predictions)
        return int(move)


    def play(self, genome1, genome2, config):
        """
        Train the AI by passing two NEAT neural networks and the NEAT config object.
        These AI's will play against each other to determine their fitness.
        """

        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)
        self.genome1 = genome1
        self.genome2 = genome2

        game_over = False
        for round_number in range(2):
            while not game_over:
                # Make move
                if round_number == 1:
                    if self.game.player_turn == 1:
                        move = self.get_prediction(net1)
                    else:
                        move = self.get_prediction(net2)
                else:
                    if self.game.player_turn == 1:
                        move = self.get_prediction(net2)
                    else:
                        move = self.get_prediction(net1)
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
                    self.genome1.fitness += 0.5
                    self.genome2.fitness += 0.5
                    game_over = True
            self.game.reset_game()
            # TODO: Play the network against dumb and a smart bot and give additional fitness if the network win.





def play_genomes(genomes, config):
    """
    Make each genome play tic-tac-toe.
    """
    # 100 pr genome * 2 because of attack and defend.
    for i, (genome_id1, genome1) in enumerate(genomes):
        genome1.fitness = 0
        for genome_id2, genome2 in random.sample(genomes, len(genomes)):
            genome2.fitness = 0 if genome2.fitness is None else genome2.fitness
            game = TicTacToeGame(3)
            game.play(genome1, genome2, config)
    #for i, (genome_id1, genome1) in enumerate(genomes):
        #print("Genome ID: ", genome_id1, " Fitness: ", genome1.fitness)

def run_population_with_neat(config):
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    #p.add_reporter(neat.Checkpointer(1))

    winner = p.run(play_genomes, 300)
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)

def test_best_network(config):
    with open("best.pickle", "rb") as f:
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

