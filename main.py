from neuroevolution import *

"""
This section is for evolving neural networks to play the game of tic tac toe.
"""
#evolve_a_champion("save_trained_models_here/network_one_champion.pickle", 1, opponent="individuals")
#evolve_a_champion("save_trained_models_here/network_two_champion.pickle", 1, opponent="random")
#evolve_a_champion("save_trained_models_here/network_three_champion.pickle", 1, opponent="minimax")

"""
This section is for playing a human player against the evolved champions.
-- This can be commented out if you don't want to play against the champions.
"""
#human_play_against_champion("save_trained_models_here/network_one_champion.pickle")
#human_play_against_champion("save_trained_models_here/network_two_champion.pickle")
#human_play_against_champion("save_trained_models_here/network_three_champion.pickle")


"""
This section is for testing the evolved champions up against the opponent algorithms, which is the minimax algorithm and the random move algorithm.
-- This can be commented out if you don't want to test the champions.
"""
#test_fifty_games_against_opponent("save_trained_models_here/network_one_champion.pickle", "random")
#test_fifty_games_against_opponent("save_trained_models_here/network_two_champion.pickle", "random")
#test_fifty_games_against_opponent("save_trained_models_here/network_three_champion.pickle", "random")

#test_fifty_games_against_opponent("save_trained_models_here/network_one_champion.pickle", "minimax")
#test_fifty_games_against_opponent("save_trained_models_here/network_two_champion.pickle", "minimax")
#test_fifty_games_against_opponent("save_trained_models_here/network_three_champion.pickle", "minimax")


