def availabe_actions(position, maze):
    """
    Returns the available actions to do
    
    Parameters:
    A list with the current position and the maze in a (nxn) matrix
    Returns:
    A list with the actions to do
    """
    actions = []
    if position[0]+1<maze.shape[0]:
        if maze[position[0]+1,position[1]]!='w':
            actions.append([1,0])
    
    if position[0]-1<maze.shape[0]:
        if maze[position[0]-1,position[1]]!='w':
            actions.append([-1,0])
    
    if position[1]+1<maze.shape[1]:
        if maze[position[0],position[1]+1]!='w':
            actions.append([0,1])
    
    if position[1]-1<maze.shape[1]:
        if maze[position[0],position[1]-1]!='w':
            actions.append([0,-1])
    return actions

def apply_action(position, action):
    """
    Returns the new current position in the maze after apply an action
    
    Parameters:
    position: a list with the current position
    action: the vector action to do (ej. Down action [0,1])
    
    Returns:
    
    """
    return [position[0]+action[0], position[1]+action[1]]

def verify_end(node, maze):
    end = False
    if node.position == [maze.shape[0]-1, maze.shape[1]-2]:
        end = True
    return end

def initial_position(maze):
    i_pos = [0,1]
    for i in range(maze.shape[1]):
        if maze[0,i]=="c":
            i_pos[1] = i
            break
    return i_pos

def transform_actions(x):
    if x == [0,1]:
        return "R"
    if x == [0,-1]:
        return "L"
    if x == [1,0]:
        return "D"
    if x == [-1,0]:
        return "U"

def animate_solution(maze, actions, algorithm):
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    import numpy as np
    copy_maze = np.copy(maze)
    position_maze = initial_position(maze)
    copy_maze[position_maze[0], position_maze[1]] = '+'
    c_action = 0
    snapshots = []
    for action in actions:
        position_maze = apply_action(position_maze, action)
        copy_maze[position_maze[0], position_maze[1]] = '+'
        num_maze = np.where(copy_maze=='w',0,1) + np.where(copy_maze=='+',1,0)
        snapshots.append(num_maze)
        snapshots.append(num_maze)
        c_action += 1
        
    nSeconds = 8
    fps = int(len(snapshots)/nSeconds)
    fig = plt.figure( figsize=(8,8) )

    a = snapshots[0]
    im = plt.imshow(a, cmap='gray')

    def animate_func(i):
        if i % fps == 0:
            print( '.', end ='' )

        im.set_array(snapshots[i])
        return [im]

    anim = animation.FuncAnimation(
                                   fig, 
                                   animate_func, 
                                   frames = len(snapshots),
                                   interval = 1000 / fps, # in ms
                                   )

    anim.save(algorithm+'_result.mp4', fps=fps, extra_args=['-vcodec', 'libx264'])

    print('Done!')
