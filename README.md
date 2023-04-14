# Neuroevolution-tic-tac-toe
This project demonstrates a simple tic-tac-toe game that trains three AI players using neuroevolution. 
The AI is trained with the NEAT (NeuroEvolution of Augmenting Topologies) algorithm, and the game is 
implemented in Python using the neat-python library. 
The code is public at Github: https://github.com/MyhreS/Neuroevolution-tic-tac-toe

## Setup
Before running the project, ensure that the required libraries are installed. You can find the list of 
required libraries in the requirements.txt file. To install them, run:
```
pip install -r requirements.txt
```
Of course, Python is required to run the project.

## How to run
The project consists of several files:
- neuroevolution.py: Contains the code for evolving the AI to play tic-tac-toe using the NEAT algorithm.
- tic_tac_toe_package: A package containing the Tic-Tac-Toe game implementation.
- main.py: Initializes the functions in neuroevolution.py.
- config.txt: Configures the NEAT algorithm parameters, such as mutation rates, population size, etc.
- requirements.txt: Contains the list of required libraries.
- save_trained_models_here: A folder where the trained models are saved.
- README.md: This file.

To run the project, execute the main.py file:
```
python main.py
```
The code is well-commented, allowing you to easily understand and modify it (main.py). You can comment out 
sections of the code that you don't want to run. Keep in mind that training the AI can be time-consuming, 
especially when evolving against a minimax opponent, as the minimax algorithm is not very efficient. 
To reduce training time, you can decrease the number of generations or the population size used in the 
evolution process.


