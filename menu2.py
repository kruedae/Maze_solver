import numpy as np
from astar import *

maze = np.genfromtxt('maze_10x10.csv', delimiter=',', dtype=str)
main_astar(maze)
