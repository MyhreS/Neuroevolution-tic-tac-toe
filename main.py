from neuroevolution import *

"""
This section is for evolving neural networks to play the game of tic tac toe.
The evolved champions are saved to the directory "save_trained_models_here".
"""
evolve_a_champion("save_trained_models_here/champion_one.pickle", generations=800, opponent="individuals")
evolve_a_champion("save_trained_models_here/champion_two.pickle", generations=800, opponent="random")
evolve_a_champion("save_trained_models_here/champion_three.pickle", generations=800, opponent="minimax")

"""
This section is for playing a human player against the evolved champions.
-- This can be commented out if you don't want to play against the champions.
"""
human_play_against_champion("save_trained_models_here/champion_one.pickle")
human_play_against_champion("save_trained_models_here/champion_two.pickle")
human_play_against_champion("save_trained_models_here/champion_three.pickle")

"""
This section is for testing the evolved champions up against the opponent algorithms, which is the minimax algorithm and the random move algorithm.
-- This can be commented out if you don't want to test the champions against the opponent algorithms.
"""
print("Testing the evolved champions up against the random move algorithm opponent .")
test_fifty_games_against_opponent("save_trained_models_here/champion_one.pickle", "random")
test_fifty_games_against_opponent("save_trained_models_here/champion_two.pickle", "random")
test_fifty_games_against_opponent("save_trained_models_here/champion_three.pickle", "random")
print("Testing the evolved champions up against the minimax algorithm opponent .")
test_fifty_games_against_opponent("save_trained_models_here/champion_one.pickle", "minimax")
test_fifty_games_against_opponent("save_trained_models_here/champion_two.pickle", "minimax")
test_fifty_games_against_opponent("save_trained_models_here/champion_three.pickle", "minimax")

"""
This section is for testing the evolved champions up against each other.
-- This can be commented out if you don't want to test the champions up against each other.
"""
print("Testing the evolved champions up against each other.")
test_champions_against_each_other("save_trained_models_here/champion_one.pickle", "save_trained_models_here/champion_two.pickle")
test_champions_against_each_other("save_trained_models_here/champion_one.pickle", "save_trained_models_here/champion_three.pickle")
test_champions_against_each_other("save_trained_models_here/champion_two.pickle", "save_trained_models_here/champion_two.pickle")


