import os

import neat
import visualize
import game.tk_gui as gui
from game.utils import Direction
from game.core_2048 import GameCore
from game.utils import State

# To adapt for different game size, change this and change num_inputs in the config
GAME_SIZE = 4
NOT_MOVED_RESTART_THRESHOLD = 10

neurons_in = []
for i in range(GAME_SIZE):
    new = []
    [new.append(0) for j in range(GAME_SIZE)]
    neurons_in.append(new)

# up, down, left, right
neurons_out = [0, 0, 0, 0]

# Create GUI with fake board as placeholder
GUI = gui.GameGUI(neurons_in)


def map_neuron_to_move(pos):
    if pos == 0:
        return Direction.UP
    elif pos == 1:
        return Direction.DOWN
    elif pos == 2:
        return Direction.LEFT
    elif pos == 3:
        return Direction.RIGHT


def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        eval_genome(genome_id, genome, config)


def eval_genome(genome_id, genome, config):
    genome.fitness = 0.0
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    game = GameCore(GAME_SIZE)
    game.restart_game()
    GUI.set_board(game.Board())

    # Play game till game over, then evaluate fitness
    game_over = False
    board = game.Board()
    not_moved_count = 0
    while not game_over:
        # Squash the n by n board into 1 by (n * n)
        in_neurons = [j for i in board for j in i]
        output = net.activate(in_neurons)

        # Use the 'most activated' output neuron as the intended direction
        max_i = max(output)

        # Play the game with the intended direction
        moved = game.try_move(map_neuron_to_move(max_i))
        GUI.repaint()
        if not moved:
            not_moved_count = not_moved_count + 1

        # for i in board:
        #     print(i)

        if game.State() == State.WIN or game.State() == State.LOSS or not_moved_count == NOT_MOVED_RESTART_THRESHOLD:
            game_over = True

    genome.fitness = game.Score()


def run(config_file):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(None))

    # Run for up to 300 generations.
    winner = p.run(eval_genomes, 300)

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))

    # Show output of the most fit genome against training data.
    print('\nOutput:')
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    # for xi, xo in zip(xor_inputs, xor_outputs):
    #     output = winner_net.activate(xi)
    #     print("input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))

    node_names = {-1: 'A', -2: 'B', 0: 'A XOR B'}
    visualize.draw_net(config, winner, True, node_names=node_names)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-2048')
    run(config_path)
