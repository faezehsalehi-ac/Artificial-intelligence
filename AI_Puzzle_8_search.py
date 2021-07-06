#!/usr/bin/env python3
"""
AI searches
"""
import heapq
import time
import turtle
from tree import *
class Search:
    """
    Search class
    """
    def __init__(self):
        self.start = Constants.START
        self.goal = Constants.GOAL
        self.start_node = Node(self.goal, self.start)
        self.heuristic = 1
    def the_big_boss(self):
        """
        THE BIG BOSS!!!
        """
        choice = '1'
        print('Welcome to '+bcolors.FLIGHTGREEN+'Seyed'+bcolors.ENDC+'\'s '+\
               bcolors.BLIGHTRED+bcolors.FLIGHTYELLOW+'Puzzle-8'+bcolors.ENDC+\
               ' Solver!!!', end='\n\n')
        while choice != '0':
            self.start_node.children = {'up':None, 'down':None, 'right':None, 'left':None}
            print('Please choose a option:', end='\n\n')
            print('\t'+bcolors.FLIGHTBLUE+'1. Solve with A* Algorithm'+bcolors.ENDC)
            print('\t'+bcolors.FLIGHTGREEN+'2'\
                  '. Solve with Greedy-best-first Algorithm'+bcolors.ENDC)
            print('\t'+bcolors.FLIGHTRED+'3. Solve with BFS Algorithm'+bcolors.ENDC)
            print('\t'+bcolors.FLIGHTCYAN+'4. Solve with DFS Algorithm'+bcolors.ENDC)
            print('\t'+bcolors.FLIGHTMAGENTA+'5. Solve with DLS Algorithm'+bcolors.ENDC)
            print('\t'+bcolors.FLIGHTGRAY+'6. Solve with IDDFS Algorithm'+bcolors.ENDC)
            print('\t'+bcolors.FLIGHTYELLOW+'9. Setting'+bcolors.ENDC)
            print('\t'+bcolors.BLIGHTRED+'0.'+\
                  bcolors.ENDC+' '+bcolors.BLIGHTRED+'Exit'+bcolors.ENDC)
            choice = input(bcolors.FCYAN+'> '+bcolors.ENDC)
            if choice == '1':
                try:
                    self.astars(self.heuristic)
                except KeyboardInterrupt:
                    print('\n'+bcolors.FWHITE+bcolors.BBLACK+'Process terminated Sir!'+bcolors.ENDC)
            elif choice == '2':
                try:
                    self.gbfs(self.heuristic)
                except KeyboardInterrupt:
                    print('\n'+bcolors.FWHITE+bcolors.BBLACK+'Process terminated Sir!'+bcolors.ENDC)
            elif choice == '3':
                try:
                    self.bfs()
                except KeyboardInterrupt:
                    print('\n'+bcolors.FWHITE+bcolors.BBLACK+'Process terminated Sir!'+bcolors.ENDC)
            elif choice == '4':
                try:
                    self.dfs()
                except KeyboardInterrupt:
                    print('\n'+bcolors.FWHITE+bcolors.BBLACK+'Process terminated Sir!'+bcolors.ENDC)
            elif choice == '5':
                try:
                    temp = int(input(bcolors.FCYAN+'depth >'+bcolors.ENDC))
                    self.dls(temp)
                except KeyboardInterrupt:
                    print('\n'+bcolors.FWHITE+bcolors.BBLACK+'Process terminated Sir!'+bcolors.ENDC)
                except ValueError:
                    print(bcolors.FLIGHTRED+'That\'s not a number!'+bcolors.ENDC)
            elif choice == '6':
                try:
                    self.iddfs()
                except KeyboardInterrupt:
                    print('\n'+bcolors.FWHITE+bcolors.BBLACK+'Process terminated Sir!'+bcolors.ENDC)
            elif choice == '9':
                choice2 = '1'
                while choice2 != '0':
                    print('Please choose a option:')
                    print('\t'+bcolors.FLIGHTBLUE+'1. Easy'+bcolors.ENDC)
                    print('\t'+bcolors.FLIGHTGREEN+'2. Medium'+bcolors.ENDC)
                    print('\t'+bcolors.FLIGHTYELLOW+'3. Hard'+bcolors.ENDC)
                    print('\t'+bcolors.FLIGHTRED+'4. Extremely Hard'+bcolors.ENDC)
                    print('\t'+bcolors.BLIGHTRED+'5.'+\
                          bcolors.ENDC+' '+bcolors.BLIGHTRED+\
                          'The'+bcolors.ENDC+' '+bcolors.BRED+'HELL'+bcolors.ENDC)
                    print('\t'+bcolors.FLIGHTYELLOW+'6. Set Start Node'+bcolors.ENDC)
                    print('\t'+bcolors.FLIGHTMAGENTA+'7. Set Goal Node'+bcolors.ENDC)
                    print('\t'+bcolors.FLIGHTGRAY+'8. Set Heuristic'+bcolors.ENDC)
                    print('\t'+bcolors.FDARKGRAY+'9. Random Start'+bcolors.ENDC)
                    print('\t'+bcolors.FLIGHTCYAN+'0. Back'+bcolors.ENDC)
                    choice2 = input(bcolors.FCYAN+'> '+bcolors.ENDC)
                    if choice2 == '1' or choice2 == '2' or\
                       choice2 == '3' or choice2 == '4' or choice2 == '5':
                        self.goal = [['1', '2', '3'], ['8', 'x', '4'], ['7', '6', '5']]
                    if choice2 == '1':
                        self.start = [['1', '3', '4'], ['8', '6', '2'], ['7', 'x', '5']]
                    elif choice2 == '2':
                        self.start = [['2', '8', '1'], ['x', '4', '3'], ['7', '6', '5']]
                    elif choice2 == '3':
                        self.start = [['2', '8', '1'], ['4', '6', '3'], ['x', '7', '5']]
                    elif choice2 == '4':
                        self.start = [['5', '6', '7'], ['4', 'x', '8'], ['3', '2', '1']]
                    elif choice2 == '5':
                        self.start = [['2', '4', '3'], ['1', '8', '6'], ['x', '7', '5']]
                    elif choice2 == '6':
                        self.start = get_node()
                    elif choice2 == '7':
                        self.goal = get_node()
                    elif choice2 == '8':
                        temp = '0'
                        while temp != '1' and temp != '2':
                            temp = input(bcolors.FCYAN+'Heuristic > '+bcolors.ENDC)
                        if temp == '1':
                            self.heuristic = 1
                        elif temp == '2':
                            self.heuristic = 2
                    elif choice2 == '9':
                        self.start = init_start()
                        self.goal = Constants.GOAL
                        print(self.start)
                        print(self.goal)
                    elif choice2 == '0':
                        pass
                    else:
                        print(bcolors.BRED+'WRONG CHOICE!!!'+bcolors.ENDC)
                    self.start_node = Node(self.goal, self.start)
            elif choice == '0':
                pass
            else:
                print(bcolors.BRED+'WRONG CHOICE!!!'+bcolors.ENDC)
        print(bcolors.FCYAN+'Bye Bye!!!'+bcolors.ENDC)
    def bfs(self):
        """
        Breadth-fisrt search
        """
        node_counter = 0
        start_time = time.time()
        queue = []
        queue = [self.start_node]
        while queue[0].is_this_node_goal() is False:
            queue[0].extend_node()
            if queue[0].children['up'] != None:
                queue.append(queue[0].children['up'])
                node_counter += 1
            if queue[0].children['down'] != None:
                queue.append(queue[0].children['down'])
                node_counter += 1
            if queue[0].children['right'] != None:
                queue.append(queue[0].children['right'])
                node_counter += 1
            if queue[0].children['left'] != None:
                queue.append(queue[0].children['left'])
                node_counter += 1
            queue.pop(0)
        queue[0].print_from_first()
        end_time = time.time()
        print(bcolors.FLIGHTMAGENTA+'Time: ' + str(end_time - start_time) + bcolors.ENDC)
        print(bcolors.FLIGHTYELLOW+'Nodes: ' + str(node_counter) + bcolors.ENDC)
        print()
    def dfs(self):
        """
        Depth-first search
        """
        node_counter = 0
        start_time = time.time()
        queue = []
        queue = [self.start_node]
        while queue[0].is_this_node_goal() is False:
            queue[0].extend_node()
            temp = queue[0]
            queue.pop(0)
            if temp.children['left'] != None:
                queue.insert(0, temp.children['left'])
            if temp.children['right'] != None:
                queue.insert(0, temp.children['right'])
            if temp.children['down'] != None:
                queue.insert(0, temp.children['down'])
            if temp.children['up'] != None:
                queue.insert(0, temp.children['up'])
        queue[0].print_from_first()
        end_time = time.time()
        print(bcolors.FLIGHTMAGENTA+'Time: ' + str(end_time - start_time) + bcolors.ENDC)
        print(bcolors.FLIGHTYELLOW+'Nodes: ' + str(node_counter) + bcolors.ENDC)
        print()
    def dls(self, limit_line=5):
        """
        Depth-limited search
        """
        node_counter = 0
        start_time = time.time()
        play = True
        queue = [self.start_node]
        while queue != [] and play is True:
            if queue[0].is_this_node_goal() is False:
                queue[0].extend_node()
                temp = queue[0]
                queue.pop(0)
                if temp.depth < limit_line:
                    if temp.children['left'] != None:
                        queue.insert(0, temp.children['left'])
                    if temp.children['right'] != None:
                        queue.insert(0, temp.children['right'])
                    if temp.children['down'] != None:
                        queue.insert(0, temp.children['down'])
                    if temp.children['up'] != None:
                        queue.insert(0, temp.children['up'])
            else:
                play = False
                queue[0].print_from_first()
                end_time = time.time()
                print(bcolors.FLIGHTMAGENTA+'Time: ' + str(end_time - start_time) + bcolors.ENDC)
                print(bcolors.FLIGHTYELLOW+'Nodes: ' + str(node_counter) + bcolors.ENDC)
                print()
    def iddfs(self):
        """
        Iterative deeping depth-first search
        """
        node_counter = 0
        start_time = time.time()
        play = True
        limit_line = 0
        while True:
            queue = [self.start_node]
            while queue != [] and play is True:
                if queue[0].is_this_node_goal() is False:
                    queue[0].extend_node()
                    temp = queue[0]
                    queue.pop(0)
                    if temp.depth < limit_line:
                        if temp.children['left'] != None:
                            queue.insert(0, temp.children['left'])
                        if temp.children['right'] != None:
                            queue.insert(0, temp.children['right'])
                        if temp.children['down'] != None:
                            queue.insert(0, temp.children['down'])
                        if temp.children['up'] != None:
                            queue.insert(0, temp.children['up'])
                else:
                    play = False
                    queue[0].print_from_first()
                    end_time = time.time()
                    print(bcolors.FLIGHTMAGENTA+'Time: ' + str(end_time - start_time) + bcolors.ENDC)
                    print(bcolors.FLIGHTYELLOW+'Nodes: ' + str(node_counter) + bcolors.ENDC)
                    print()
            limit_line += 1
            if play is False:
                break
    def gbfs(self, heuristic_type=1):
        """
        Greedy best-first search
        """
        Constants.HURISTIC_TYPE = heuristic_type
        node_counter = 0
        start_time = time.time()
        heap = []
        heapq.heappush(heap, (self.start_node.heuristic, time.time(), self.start_node))
        node_counter += 1
        temp = heapq.heappop(heap)[2]
        while temp.is_this_node_goal() is False:
            temp.extend_node()
            if temp.children['left'] != None:
                heapq.heappush(heap, (temp.children['left'].heuristic,\
                               time.time(), temp.children['left']))
                node_counter += 1
            if temp.children['right'] != None:
                heapq.heappush(heap, (temp.children['right'].heuristic,\
                               time.time(), temp.children['right']))
                node_counter += 1
            if temp.children['down'] != None:
                heapq.heappush(heap, (temp.children['down'].heuristic,\
                               time.time(), temp.children['down']))
                node_counter += 1
            if temp.children['up'] != None:
                heapq.heappush(heap, (temp.children['up'].heuristic,\
                                      time.time(), temp.children['up']))
                node_counter += 1
            temp = heapq.heappop(heap)[2]
        temp.print_from_first()
        end_time = time.time()
        print(bcolors.FLIGHTMAGENTA+'Time: ' + str(end_time - start_time) + bcolors.ENDC)
        print(bcolors.FLIGHTYELLOW+'Nodes: ' + str(node_counter) + bcolors.ENDC)
        print()
    def astars(self, heuristic_type=1):
        """
        A* search
        """
        Constants.HURISTIC_TYPE = heuristic_type
        node_counter = 0
        start_time = time.time()
        heap = []
        heapq.heappush(heap, (self.start_node.get_f_value(), time.time(), self.start_node))
        node_counter += 1
        temp = heapq.heappop(heap)[2]
        while temp.is_this_node_goal() is False:
            temp.extend_node()
            if temp.children['left'] != None:
                heapq.heappush(heap, (temp.children['left'].get_f_value(),\
                                      time.time(), temp.children['left']))
                node_counter += 1
            if temp.children['right'] != None:
                heapq.heappush(heap, (temp.children['right'].get_f_value(),\
                                      time.time(), temp.children['right']))
                node_counter += 1
            if temp.children['down'] != None:
                heapq.heappush(heap, (temp.children['down'].get_f_value(),\
                                      time.time(), temp.children['down']))
                node_counter += 1
            if temp.children['up'] != None:
                heapq.heappush(heap, (temp.children['up'].get_f_value(),\
                                      time.time(), temp.children['up']))
                node_counter += 1
            temp = heapq.heappop(heap)[2]
        temp.print_from_first()
        end_time = time.time()
        print(bcolors.FLIGHTMAGENTA+'Time: ' + str(end_time - start_time) + bcolors.ENDC)
        print(bcolors.FLIGHTYELLOW+'Nodes: ' + str(node_counter) + bcolors.ENDC)
        print()
def get_node():
    """Get node from user"""
    ret_val = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
    for i in range(3):
        for j in range(3):
            temp = input('Row['+bcolors.FLIGHTYELLOW+str(i)+bcolors.ENDC+\
                         '] Col ['+bcolors.FLIGHTGREEN+str(j)+bcolors.ENDC+'] > ')
            while is_number(temp, ret_val) is False:
                temp = input('Row['+bcolors.FLIGHTYELLOW+str(i)+bcolors.ENDC+\
                             '] Col ['+bcolors.FLIGHTGREEN+str(j)+bcolors.ENDC+'] > ')
            if temp == 'x':
                ret_val[i][j] = 'x'
            else:
                ret_val[i][j] = int(temp)
    print()
    print_my_node(ret_val)
    return ret_val
def is_number(value, node):
    """Is entered value a number or 'x'"""
    try:
        if value == 'x':
            return 'x'
        val = int(value)
        if val < 1 or val > 8:
            print(bcolors.FLIGHTRED+'Number is not in range'+bcolors.ENDC)
            return False
        if val in node[0] or val in node[1] or val in node[2]:
            print(bcolors.FLIGHTRED+'Repeted number!!!'+bcolors.ENDC)
            return False
        return val
    except ValueError:
        print(bcolors.FLIGHTRED+'That\'s not a number!'+bcolors.ENDC)
        return False
def print_my_node(node):
    """Print my node"""
    for i in range(3):
        for j in range(3):
            print(node[i][j], end='')
            if j != 2:
                print(', ', end='')
        print()
if __name__ == '__main__':
    try:
        SEARCH = Search()
        SEARCH.the_big_boss()
    except:
        print('Something went wrong!')
