import numpy as np
import queue
import time
import os, psutil
from funciones import *

class node(object):
    """
    position
    list of previous actions
    """
    def __init__(self, position, actions=[], count=0):
        self.position = position
        self.actions = actions
        self.count = count
    def increase_count(self):
        self.count = self.count+1
    def get_count(self):
        return self.count
    def __gt__(self, other):
        return self.count > other.count
    def __lt__(self, other):
        return self.count < other.count
import queue

def main_uniform(maze):
    # get the start time
    st = time.time()
    S = node(initial_position(maze))
    frontier= queue.PriorityQueue()
    frontier.put(S)
    current_node = frontier.get()
    while not verify_end(current_node, maze):
        for action in availabe_actions(current_node.position, maze):
            new_actions = [x for x in current_node.actions]
            new_actions.append(action)
            new_node = node(apply_action(current_node.position, action), new_actions, current_node.get_count()+1)
            frontier.put(new_node)
        current_node = frontier.get()
    #print(frontier.qsize(), current_node.position, [transform_actions(x) for x in current_node.actions])
    # get the end time
    et = time.time()
    # get the execution time
    elapsed_time = et - st

    process = psutil.Process(os.getpid())
    memory = process.memory_info().rss/(1024**2)
    animate_solution(maze, current_node.actions, 'uniform')
    return elapsed_time, memory
