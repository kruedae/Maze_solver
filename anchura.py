import numpy as np
import queue
import time
from funciones import *

class node:
    """
    position
    list of previous actions
    """
    def __init__(self, position, actions=[]):
        self.position = position
        self.actions = actions

import queue

def main_anchura(maze):
    # get the start time
    st = time.time()
    S = node(initial_position(maze))
    frontier= queue.Queue()
    frontier.put(S)
    current_node = frontier.get()

    while not verify_end(current_node, maze):
        for action in availabe_actions(current_node.position, maze):
            new_actions = [x for x in current_node.actions]
            new_actions.append(action)
            new_node = node(apply_action(current_node.position, action), new_actions)
            frontier.put(new_node)
        if not frontier.empty():
            current_node = frontier.get()
    et = time.time()
    # get the execution time
    elapsed_time = et - st
    #print('Execution time:', elapsed_time, 'seconds')
    #print(frontier.qsize(), current_node.position, [transform_actions(x) for x in current_node.actions])
    animate_solution(maze, current_node.actions, 'anchura')
    return elapsed_time
