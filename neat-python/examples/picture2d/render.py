import pickle
import pygame

import evolve_2048
from neat import nn, visualize

evolve_2048.W = 1000
evolve_2048.H = 1000

pb = evolve_2048.PictureBreeder(128, 128, 1500, 1500, 1280, 1024, 'color', 4)

with open("genome-20219-701.bin", "rb") as f:
    g = pickle.load(f)
    print g
    node_names = {0: 'x', 1: 'y', 2: 'gray'}
    visualize.draw_net(g, view=True, filename="picture-net.gv",
                       show_disabled=False, prune_unused=True, node_names=node_names)

    net = nn.create_feed_forward_phenotype(g)
    pb.make_high_resolution(g)
