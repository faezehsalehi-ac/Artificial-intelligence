
import copy
from collections import deque
import sys


stack = []
queue = []


down_flag =0
up_flag =0
left_flag =0
right_flag =0
puzzle_counter=0
solve_flag = 0

temp_limit = 0
max_step = 0
print(' welcom to 24puzzle program , here we solve the puzzle with dfs')
max_step = int (input ("How many steps could we crawl the tree?\n"))
print ('\n\n\n')
getting_r = 1
getting_c = 1


mypuzzle = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20] ,[21, 22, 23, 24, 00],[0,0,'',[]]]

mypuzzle[5][3] = deque()



for i in range( 0, 5 ) :
   
	for j in range ( 0, 5 ) :
		print ( "Enter Cell -> Row", getting_r, " Column", getting_c, ": " )
		getting_c = getting_c+1
		mypuzzle[i][j] = int( input() )
	   
		if mypuzzle[i][j] > 24 :
			print ("\n\n\n=================================\n    LARGE NUMBER ERROR !!!!!!!!!!!!!!\n=================================\n\n\n")
			sys.exit()
													  
	getting_r = getting_r+1
	getting_c = 1
	print ("________________________________")



print ("\n\n\n=================================\n      PLeas wait\n=================================\n\n\n")



solved = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20] ,[21, 22, 23, 24, 00],[0,0,'',[]]]


############## aval omgh



stack.append (mypuzzle)

while 1:
	
		puzzle = stack.pop()

		if (puzzle[0:5] == solved[0:5]):
			print ("\n\n\n=================================\n      SOLVED!!!!!!!!!!!!!!\n=================================\n\n\n")

			solve_flag = 1
			puzzle[5][3].append('finish')

			break
	
		for i in range (0,5):
			for j in range (0,5):
				if puzzle[i][j] == 00:
					free_r = i
					free_c = j

	
		if (puzzle[5][1]<max_step):


			if free_r != 0 :
				if puzzle[5][2] != 'down' :
					up_puzzle = copy.deepcopy(puzzle)	

					up_puzzle[ free_r ][ free_c] = up_puzzle[ free_r-1 ][ free_c ]
					up_puzzle[ free_r -1 ][ free_c ] = 00

					puzzle_counter = puzzle_counter+1
					up_puzzle[5][0] = puzzle_counter	

					up_puzzle[5][1] = up_puzzle[5][1]+1	

					up_puzzle[5][2] = 'up'

					up_flag = 1 
					up_puzzle[5][3].append('map_up')
				


			if free_c != 0 :
				if puzzle[5][2] != 'right':
					left_puzzle = copy.deepcopy(puzzle)
					left_puzzle[free_r][free_c] = left_puzzle[free_r][free_c-1]
					left_puzzle[free_r][free_c-1] = 00	

					puzzle_counter = puzzle_counter+1
					left_puzzle[5][0] = puzzle_counter
					left_puzzle[5][1] = left_puzzle[5][1]+1
					left_puzzle[5][2] = 'left'

					left_flag = 1

					left_puzzle[5][3].append('map_left')



			if free_r != 4:
				if puzzle[5][2] != 'up':
					down_puzzle = copy.deepcopy(puzzle)
					down_puzzle[ free_r ][ free_c] = down_puzzle[ free_r+1 ][ free_c ]
					down_puzzle[ free_r +1 ][ free_c ] =  00	

					puzzle_counter = puzzle_counter+1
					down_puzzle[5][0] = puzzle_counter
					down_puzzle[5][1] = down_puzzle[5][1]+1
					down_puzzle[5][2] = 'down'

					down_flag = 1

					down_puzzle[5][3].append('map_down')
				

			if free_c != 4 :
				if puzzle[5][2] != 'left':
					right_puzzle = copy.deepcopy(puzzle)
					right_puzzle[free_r][free_c] = right_puzzle[free_r][free_c+1]
					right_puzzle[free_r][free_c+1] = 00

					puzzle_counter = puzzle_counter+1
					right_puzzle[5][0] = puzzle_counter
					right_puzzle[5][1] = right_puzzle[5][1]+1
					right_puzzle[5][2] = 'right'

					right_flag = 1

					right_puzzle[5][3].append('map_right')



		if right_flag == 1:
			stack.append (right_puzzle)
			right_flag = 0

		if down_flag == 1:
			stack.append (down_puzzle)
			down_flag = 0

		if left_flag == 1:
			stack.append (left_puzzle)
			left_flag = 0

		if up_flag == 1:
			stack.append (up_puzzle)
			up_flag = 0


##### start of  MAPPING
		
map_counter = -1

if solve_flag == 1:
	while 1:
        
		move = puzzle[5][3].popleft()
		map_counter = map_counter + 1 
		

		print ("=====================")
		print (mypuzzle[0])
		print (mypuzzle[1])
		print (mypuzzle[2])
		print (mypuzzle[3])
		print (mypuzzle[4])
		print ("=====================")

		for i in range (0,5):
			for j in range (0,5):
				if mypuzzle[i][j] == 00:
					free_r = i
					free_c = j


		if move == 'map_right':
			print ("\n\n\nMOVE RIGHT")
			mypuzzle[free_r][free_c] = mypuzzle[free_r][free_c+1]
			mypuzzle[free_r][free_c+1] = 00

		if move == 'map_up':
			print ("\n\n\nMOVE UP")
			mypuzzle[ free_r ][ free_c] = mypuzzle[ free_r-1 ][ free_c ]
			mypuzzle[ free_r -1 ][ free_c ] = 00

		if move == 'map_down':
			print ("\n\n\nMOVE DOWN")
			mypuzzle[ free_r ][ free_c] = mypuzzle[ free_r+1 ][ free_c ]
			mypuzzle[ free_r +1 ][ free_c ] =  00

		if move == 'map_left':
			print ("\n\n\nMOVE LEFT")
			mypuzzle[free_r][free_c] = mypuzzle[free_r][free_c-1]
			mypuzzle[free_r][free_c-1] = 00	

		if move == 'finish':
			print ("FINAL\n\n\n=================================\n  )\n=================================")
			print("=================================\n      IN JUST ",map_counter," MOVES!!!\n=================================\n\n\n")
			while 1:
				pass
			break




