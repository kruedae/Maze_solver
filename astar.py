import numpy as np
import queue
import time
from funciones import *

class node(object):
    """
    position
    list of previous actions
    """
    def __init__(self, position, actions, count, final_position):
        self.position = position
        self.actions = actions
        self.count = count
        self.final_position = final_position
    def increase_count(self):
        self.count = self.count+1
    def get_count(self):
        return self.count
    def __gt__(self, other):
        distance_heuristic = np.sqrt((self.position[0]-self.final_position[0])**2.+(self.position[1]-self.final_position[1])**2.)
        other_distance_heuristic = np.sqrt((other.position[0]-other.final_position[0])**2.+(other.position[1]-other.final_position[1])**2.)
        return self.count + distance_heuristic > other.count + other_distance_heuristic
    def __lt__(self, other):
        distance_heuristic = np.sqrt((self.position[0]-self.final_position[0])**2.+(self.position[1]-self.final_position[1])**2.)
        other_distance_heuristic = np.sqrt((other.position[0]-other.final_position[0])**2.+(other.position[1]-other.final_position[1])**2.)
        return self.count + distance_heuristic < other.count + other_distance_heuristic

def main_astar(maze):
    # get the start time
    st = time.time()
    S = node(initial_position(maze), actions=[], count=0, final_position=[maze.shape[0]-1, maze.shape[1]-2])
    print(S.position)
    frontier= queue.PriorityQueue()
    frontier.put(S)
    current_node = frontier.get()
    while not (verify_end(current_node, maze)):
        for action in availabe_actions(current_node.position, maze):
            new_actions = [x for x in current_node.actions]
            new_actions.append(action)
            new_node = node(apply_action(current_node.position, action), new_actions, current_node.get_count()+1, [maze.shape[0]-1, maze.shape[1]-2])
            frontier.put(new_node)
        current_node = frontier.get()
    # get the end time
    et = time.time()
    # get the execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
    print(frontier.qsize(), current_node.position, [transform_actions(x) for x in current_node.actions])
    animate_solution(maze, current_node.actions, 'astar')
    return elapsed_time
