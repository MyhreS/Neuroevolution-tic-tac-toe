from neuroevolution import *

train_network_one("save_trained_models_here/network_one_champion.pickle", 1)
train_network_two("save_trained_models_here/network_two_champion.pickle", 1)
train_network_three("save_trained_models_here/network_three_champion.pickle", 1)


"""
local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'config.txt')

config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     config_path)


#run_population_with_neat(config)
test_best_network(config)
"""