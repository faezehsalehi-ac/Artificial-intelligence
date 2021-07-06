"""
A simple tree for AI search algorithms
"""
import random
from copy import deepcopy
from colors import bcolors
class Constants:
    """
    Project constants
    """
    PRICE = 1
    GOAL = [['1', '2', '3'], ['8', 'x', '4'], ['7', '6', '5']]
    START = [['1', '3', '4'], ['8', '6', '2'], ['7', 'x', '5']]
    HURISTIC_TYPE = 1
class Node:
    """
    Node class
    """
    def __init__(self, goal, node=None, root=None, action=None):
        self.goal = goal
        self.node = node
        self.root = root
        self.action = action
        self.children = {'up':None, 'down':None, 'right':None, 'left':None}
        self.price = 0
        self.depth = 0
        self.heuristic = 0
        self.set_heuristic(Constants.HURISTIC_TYPE)
    def extend_node(self):
        """
        Add given node to this node's children
        """
        p_m_a_p = possible_moves_and_positions(self.node)
        if p_m_a_p['p_m']['up'] is True:
            self.children['up'] = Node(self.goal, self.swap_x(\
            p_m_a_p['pos'], 'up'), self, 'up')
            self.children['up'].price = self.price + Constants.PRICE
            self.children['up'].depth = self.depth + 1
        if p_m_a_p['p_m']['down'] is True:
            self.children['down'] = Node(self.goal, self.swap_x(\
            p_m_a_p['pos'], 'down'), self, 'down')
            self.children['down'].price = self.price + Constants.PRICE
            self.children['down'].depth = self.depth + 1
        if p_m_a_p['p_m']['right'] is True:
            self.children['right'] = Node(self.goal, self.swap_x(\
            p_m_a_p['pos'], 'right'), self, 'right')
            self.children['right'].price = self.price + Constants.PRICE
            self.children['right'].depth = self.depth + 1
        if p_m_a_p['p_m']['left'] is True:
            self.children['left'] = Node(self.goal, self.swap_x(\
            p_m_a_p['pos'], 'left'), self, 'left')
            self.children['left'].price = self.price + Constants.PRICE
            self.children['left'].depth = self.depth + 1
    def print_node(self):
        """
        Print the current node
        """
        x_pos = 0
        y_pos = 0
        color = [['', '', ''], ['', '', ''], ['', '', '']]
        for i in range(3):
            for j in range(3):
                if self.node[i][j] == 'x':
                    color[i][j] = 'red'
                    x_pos = i
                    y_pos = j
        if self.action == 'up':
            color[x_pos+1][y_pos] = 'yellow'
        elif self.action == 'down':
            color[x_pos-1][y_pos] = 'yellow'
        elif self.action == 'right':
            color[x_pos][y_pos-1] = 'yellow'
        elif self.action == 'left':
            color[x_pos][y_pos+1] = 'yellow'
        for i in range(3):
            for j in range(3):
                if color[i][j] == 'red':
                    print(bcolors.BLIGHTRED, end='')
                elif color[i][j] == 'yellow':
                    print(bcolors.FLIGHTYELLOW, end='')
                print(self.node[i][j], end='')
                if color[i][j] == 'red' or color[i][j] == 'yellow':
                    print(bcolors.ENDC, end='')
                if j != 2:
                    print(', ', end='')
            print()
        print()
        print('depth: ' + str(self.depth))
        print()
    def is_this_node_goal(self):
        """
        Is current node the goal?
        """
        if self.node == self.goal:
            return True
        return False
    def swap_x(self, pos, action):
        """
        Swap empty slot
        """
        new_node = deepcopy(self.node)
        if action == 'up':
            new_node[pos['x']][pos['y']] = new_node[pos['x']-1][pos['y']]
            new_node[pos['x']-1][pos['y']] = 'x'
        elif action == 'down':
            new_node[pos['x']][pos['y']] = new_node[pos['x']+1][pos['y']]
            new_node[pos['x']+1][pos['y']] = 'x'
        elif action == 'right':
            new_node[pos['x']][pos['y']] = new_node[pos['x']][pos['y']+1]
            new_node[pos['x']][pos['y']+1] = 'x'
        elif action == 'left':
            new_node[pos['x']][pos['y']] = new_node[pos['x']][pos['y']-1]
            new_node[pos['x']][pos['y']-1] = 'x'
        return new_node
    def print_from_first(self, my_list=[], counter=1):
        """
        Printing from parent to children
        """
        if counter == 1:
            my_list = []
        my_list.insert(0, self)
        if self.root != None:
            self.root.print_from_first(my_list, 0)
        else:
            for i in my_list:
                i.print_node()
            print(bcolors.FLIGHTGREEN+'God'+bcolors.FLIGHTCYAN+\
                  ' guided us to the straight path!'+bcolors.ENDC)
    def manhattan_distance(self):
        """Calculate manhattan distance"""
        score = 0
        for i in range(3):
            for j in range(3):
                goal_x = 0
                goal_y = 0
                for search_x in range(3):
                    for search_y in range(3):
                        if self.goal[search_x][search_y] == self.node[i][j]:
                            goal_x = search_x
                            goal_y = search_y
                score += abs(goal_x - i) + abs(goal_y - j)
        return score
    def row_column(self):
        """Calcute number of slots that are not in their row and column"""
        score = 0
        row = 0
        column = 0
        for i in range(3):
            for j in range(3):
                goal_x = 0
                goal_y = 0
                for search_x in range(3):
                    for search_y in range(3):
                        if self.goal[search_x][search_y] == self.node[i][j]:
                            goal_x = search_x
                            goal_y = search_y
                if i != goal_x:
                    row += 1
                if j != goal_y:
                    column += 1
        score = row + column
        return score
    def set_heuristic(self, calc_type=1):
        """Calcute heuristic value"""
        if calc_type == 1:
            self.heuristic = self.manhattan_distance()
        elif calc_type == 2:
            self.heuristic = self.row_column()
    def get_f_value(self):
        """Get f(n) value"""
        return self.price + self.heuristic
def possible_moves_and_positions(node):
    """
    Give possible moves for empty slot
    """
    x_pos = 0
    y_pos = 0
    for i in range(3):
        for j in range(3):
            if node[i][j] == 'x':
                x_pos = i
                y_pos = j
    p_m = {'up':True, 'down':True, 'right':True, 'left':True}
    if x_pos == 0:
        p_m['up'] = False
    if x_pos == 2:
        p_m['down'] = False
    if y_pos == 0:
        p_m['left'] = False
    if y_pos == 2:
        p_m['right'] = False
    return {'p_m':p_m, 'pos':{'x': x_pos, 'y': y_pos}}
def init_start(node=deepcopy(Constants.GOAL), moves=10):
    """Init start"""
    last_move = ''
    counter = moves
    while counter != 0:
        p_m = possible_moves_and_positions(node)
        action = random.choice(['up', 'down', 'right', 'left'])
        if p_m['p_m'][action] is True and last_move != rotate(action):
            last_move = action
            pos = p_m['pos']
            if action == 'up':
                node[pos['x']][pos['y']] = node[pos['x']-1][pos['y']]
                node[pos['x']-1][pos['y']] = 'x'
            elif action == 'down':
                node[pos['x']][pos['y']] = node[pos['x']+1][pos['y']]
                node[pos['x']+1][pos['y']] = 'x'
            elif action == 'right':
                node[pos['x']][pos['y']] = node[pos['x']][pos['y']+1]
                node[pos['x']][pos['y']+1] = 'x'
            elif action == 'left':
                node[pos['x']][pos['y']] = node[pos['x']][pos['y']-1]
                node[pos['x']][pos['y']-1] = 'x'
        else:
            counter += 1
        counter -= 1
    return node
def rotate(direction):
    """Get reverse value"""
    if direction == 'up':
        return 'down'
    elif direction == 'down':
        return 'up'
    elif direction == 'right':
        return 'left'
    elif direction == 'left':
        return 'right'
