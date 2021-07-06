import numpy as np
import random
import copy

temp = []
for i in range(1000):
    r = random.randint(0, 24)
    if r not in temp: temp.append(r)
    if len(temp) > 25: break
mat = []
t = []
for i, j in enumerate(temp):
    if (i + 1) % 5 is not 0:
        t.append(j)
    else:
        t.append(j)
        mat.append(t)
        t = []

final_mat = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]


# mat1 = [[1, 6, 2, 3, 4], [5, 0, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]

# print(mat)


class Node():

    def __init__(self, mat, pr, d):
        self.state = mat

        self.center = None

        if self.state is not None:
            for y, t1 in enumerate(self.state):
                for x, t2 in enumerate(t1):
                    # print(x, y, t2)
                    if t2 == 0:
                        # print(x, y)
                        self.center = (x, y)
                        break
                if self.center is not None:
                    break

        self.parent = pr

        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None
        self.depth = d

    def extend(self):
        x, y = self.center[0], self.center[1]
        if self.center[0] - 1 != -1:
            temp = copy.deepcopy(self.state)
            temp[y][x], temp[y][x - 1] = temp[y][x - 1], temp[y][x]
            self.child1 = Node(temp, self, self.depth + 1)

        if self.center[1] - 1 != -1:
            temp = copy.deepcopy(self.state)
            temp[y][x], temp[y - 1][x] = temp[y - 1][x], temp[y][x]
            self.child2 = Node(temp, self, self.depth + 1)

        if self.center[0] + 1 != 5:
            temp = copy.deepcopy(self.state)
            temp[y][x], temp[y][x + 1] = temp[y][x + 1], temp[y][x]
            self.child3 = Node(temp, self, self.depth + 1)

        if self.center[1] + 1 != 5:
            temp = copy.deepcopy(self.state)
            temp[y][x], temp[y + 1][x] = temp[y + 1][x], temp[y][x]
            self.child4 = Node(temp, self, self.depth + 1)



########## aval sath ##########
def first(start):
    st = []
    ans = None
    rear = 0
    st.append(start)
    while rear is not len(st):
        temp = copy.deepcopy(st[rear])

        if temp.state == final_mat:
            ans = temp
            while temp.parent is not None:
                print(temp.state)
                temp = temp.parent
            print(temp.state)

            break
        temp.extend()

        if temp.child4 is not None:
            st.append(temp.child4)
        if temp.child3 is not None:
            st.append(temp.child3)
        if temp.child2 is not None:
            st.append(temp.child2)
        if temp.child1 is not None:
            st.append(temp.child1)
        rear += 1



start = Node(mat, None, 0)
first_depth(start)
