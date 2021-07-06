

# --- GENERAL -------------------------------------------------------
from random import randint
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4, width=120)
EMPTY = 0


def possible_moves(matrix):
    """
    description: Possible moves of empty tile based on it's position
    input      : Puzzle (matrix 5*5)
    output     : A list of all possible moves (list)
    """
    result = []
    m = eval(matrix)

    # Finding row and column of empty tile
    row = 0
    while EMPTY not in m[row]: row += 1
    column = m[row].index(EMPTY)

    # Finding possible moves of empty tile
    if row > 0:                                                     # up
        m[row][column], m[row-1][column] = m[row-1][column], m[row][column]
        result.append(str(m))
        m[row][column], m[row-1][column] = m[row-1][column], m[row][column]

    if row < 2:                                                     # down
        m[row][column], m[row+1][column] = m[row+1][column], m[row][column]
        result.append(str(m))
        m[row][column], m[row+1][column] = m[row+1][column], m[row][column]

    if column > 0:                                                  # left
        m[row][column], m[row][column-1] = m[row][column-1], m[row][column]
        result.append(str(m))
        m[row][column], m[row][column-1] = m[row][column-1], m[row][column]

    if column < 2:                                                  # right
        m[row][column], m[row][column+1] = m[row][column+1], m[row][column]
        result.append(str(m))
        m[row][column], m[row][column+1] = m[row][column+1], m[row][column]

    return result


# --- A* ALGORITHM --------------------------------------------------
def heuristic_1(puzzle):
    """
    description: Misplaced tiles
    input      : Puzzle (matrix 5*5)
    output     : The number of misplaced tiles (int)
    """
    misplaced = 0
    tile = EMPTY
    m = eval(puzzle)
    for row in range(3):
        for column in range(3):
            if m[row][column] != tile:
                misplaced += 1
            tile += 1
    return misplaced


def heuristic_2(puzzle):
    """
    description: Manhattan distance
    input      : Puzzle (matrix 5*5)
    output     : Manhattan distance (integer)
    """
    distance = 0
    m = eval(puzzle)
    for row in range(3):
        for column in range(3):
            if m[row][column] == EMPTY: continue 
            distance += int(abs(row - (m[row][column] / 3)) + abs(column - (m[row][column] % 3)))
    return distance


def puzzle_astar(initial, goal):
    """
    description: A* algorithm
    input      : Initial state, Goal state
    output     : -
    """
    fringe = [{
        'heuristic': heuristic_2(initial),
        'state'    : initial
    }]

    expanded = []
    expanded_nodes = 0

    print("> Solution:")
    while fringe:
        # finding minimum heuristic node in fringe set.
        min_node = fringe[0]
        for node in fringe:
            if node['heuristic'] < min_node['heuristic']:
                min_node = node

        # illustrating path to user
        pp.pprint(min_node)
        print()

        # check and return this node if one were goal node
        if min_node['state'] == goal:
            expanded.append(min_node['state'])
            break

        # check and skip this node if one were expanded before
        if min_node['state'] in expanded:
            continue

        # select this node to expand and remove it from fringe set
        fringe.remove(min_node)

        # finding non-repetitive nodes as descendants of selected node
        for move in possible_moves(min_node['state']):
            if move in expanded: continue
            # adding descendants to fringe set
            fringe.append({
                'heuristic': min_node['heuristic'] + heuristic_2(move) - heuristic_2(min_node['state']),
                'state'    : move
            })
            # adding selected node to expanded node set to prevent loop
            expanded.append(min_node['state'])
        # recording number of expended nodes
        expanded_nodes += 1

    # showing number of expanded nodes
    print("\n> Expanded nodes:", expanded_nodes)


# --- BREADTH FIRST ALGORITHM ---------------------------------------
def puzzle_breadth_first(initial, goal):
    """
    description: Breadth First algorithm
    input      : Initial state, Goal state
    output     : -
    """
    fringe = [initial]
    expanded = []
    expanded_nodes = 0

    print("> Solution:")
    while fringe:
        # selecting first node of fringe set.
        selected_node = fringe[0]

        # illustrating path to user
        pp.pprint(selected_node)
        print('')

        # check and return this node if one were goal node
        if selected_node == goal: break

        # select this node to expand and remove it from fringe set
        fringe = fringe[1:]

        # adding selected node to expanded node set to prevent loop
        expanded.append(selected_node)

        # finding non-repetitive nodes as descendants of selected node
        for move in possible_moves(selected_node):
            if move in expanded: continue
            # adding descendants to fringe set
            fringe.append(move)

        # recording number of expended nodes
        expanded_nodes += 1

    # showing number of expanded nodes
    print("\n> Expanded nodes:", expanded_nodes)


# --- DFS ALGORITHM ---------------------------------------
def puzzle_backtracking(current, goal, level, count=0, expended=[]):
    """
    description: Iterative deepening algorithm
    input      : Initial state, Goal state, Level limitation, Level Counter, Expended nodes
    output     : False or path nodes to the goal node
    """
    result = False

    if count < level:
        count += 1
        expended.append(current)
        # showing node level and node
        print('L', count, ': ', current)

        if current == goal: result = goal
        elif not current: result = False
        elif count:
            for move in possible_moves(current):
                if move in expended: continue
                # do DFS algorithm to first left descendant node
                result = puzzle_backtracking(move, goal, level, count, expended)
                # going to next sibling node
                if not result: continue
                return result

    return result


# --- ITERATIVE DEEPENING ALGORITHM ---------------------------------
def puzzle_iterative_deepening(initial, goal, level_limit):
    """
    description: Iterative deepening algorithm
    input      : Initial state, Goal state, Level limitation
    output     : -
    """
    print("> Solution by limiting level to", level_limit, ":\n")

    result = puzzle_backtracking(initial, goal, level_limit)
    if not result: result = '\n> not found'
    else: print('\nGOAL:')
    print(result)
def readfile():
    f=open('puzzle.txt', 'r')
    readMe= str([[int(num) for num in line.split(',')] for line in f])
    return readMe
def rand(n):
    place1=0
    place2=0
    f=[[EMPTY, 1, 2],[3, 4, 5],[6, 7, 8]]
    for i in range(1,n+1):
        place1=randint(0, 2)
        place2=randint(0, 2)
        place3 = randint(0, 2)
        place4 = randint(0, 2)
        temp=f[place1][place2]
        f[place1][place2]=f[place3][place4]
        f[place3][place4]=temp
    return str(f)

# --- MAIN ----------------------------------------------------------
if __name__ == '__main__':
    i=0
    initial_state=[[0,0,0],[0,0,0],[0,0,0]]
    print ("read from file i=1")
    print ("random i=2")
    print ("k.B i=3")
    i=input("enter i=")
    if i==1:
        initial_state=readfile()
    if i==2:
        n=input();
        initial_state=rand(n)
    if i==3:
        initial_state=str(input())
    goal_state = str([
        [EMPTY, 1 , 2  ],
        [3    , 4 , 5  ],
        [6    , 7 , 8  ],
    ])

    print ('if x=1 then bfs');
    print ("if x=2 then idfs ");
    print ("if x=3 then a*");
    x=0
    x=input("enter x=");

    if x==1:
        puzzle_breadth_first(initial_state, goal_state)
    if x==2:
        puzzle_iterative_deepening(initial_state, goal_state, 7)
    if x==3:
        puzzle_astar(initial_state, goal_state)
