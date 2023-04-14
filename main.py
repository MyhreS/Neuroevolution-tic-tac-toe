from neuroevolution import *

evolve_a_champion("save_trained_models_here/network_one_champion.pickle", 1, opponent="individuals")
evolve_a_champion("save_trained_models_here/network_two_champion.pickle", 1, opponent="random")
evolve_a_champion("save_trained_models_here/network_three_champion.pickle", 1, opponent="minimax")

#human_play_against_champion("save_trained_models_here/network_one_champion.pickle")
#human_play_against_champion("save_trained_models_here/network_two_champion.pickle")
#human_play_against_champion("save_trained_models_here/network_three_champion.pickle")
