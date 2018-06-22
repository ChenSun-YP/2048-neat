import os

import neat
import interface_2048 as game
import visualize
from game.utils import Direction

# To adapt for different game size, change this and change num_inputs in the config
game_size = 4

neurons_in = []

for i in range(0, game_size-1):
    new = []
    [new.append(0) for j in range(0, game_size - 1) ]
    neurons_in.append(new)


# up, left, down, right
neurons_out = [0, 0, 0, 0]


def map_neuron_to_move(pos):
    if pos == 0:
        return Direction.UP
    elif pos == 1:
        return Direction.LEFT
    elif pos == 2:
        return Direction.DOWN
    elif pos == 3:
        return Direction.RIGHT


def eval_genomes(genomes, config):
    game.initialize()
    for genome_id, genome in genomes:
        eval_genome(genome_id, genome, config)


def eval_genome(genome_id, genome, config):
    genome.fitness = 0.0
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    game.restart_game(game_size)

    # Play game till game over, then evaluate fitness
    game_over = False
    score = 0
    while not game_over:
        # Squash the n by n board into 1 by (n * n)
        board = game.status['board']
        in_neurons = [j for i in board for j in i]
        output = net.activate(in_neurons)

        # Use the 'most activated' output neuron as the intended direction
        max_i = 0
        max_out = 0
        for out_i, out in enumerate(output):
            if out > max_out:
                max_i = out_i
                max_out = out

        # Play the game with the intended direction
        game.make_move(map_neuron_to_move(max_i))
        status = game.status
        game_state = game.state
        if game_state == game.State.GAMEOVER:
            game_over = True
            score = status['score']

    genome.fitness = score


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
    p.add_reporter(neat.Checkpointer(5))

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

    node_names = {-1:'A', -2: 'B', 0:'A XOR B'}
    visualize.draw_net(config, winner, True, node_names=node_names)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)

    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
    p.run(eval_genomes, 10)


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-2048')
    run(config_path)