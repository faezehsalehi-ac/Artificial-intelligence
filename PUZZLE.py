#CODE BY:
	#AMIR ARANI
	#9621176201
	#for AI project in UoK


#DUTY:
	# 1. get a puzzle
	# 2. solve it with BFS or DFS or IDS algorithm...
	# 3. Print solution


#NAMES:

	# puzzle2 = getting puzzle
	# solved = solved puzzle example

	# followings are explained in NOTES
		# stack
		# queue

	# getting_r = printing row counter (related to puzzle getting section)      
	# getting_c = printing row counter

	#this following flags are for control stacking procces in DFS
		#down_flag 
		#up_flag
		#left_flag
		#right_flag


	#this following names are temporary lists that made when we change a puzzle and after we check different cases we stack or queue them
		#right_puzzle
		#down_puzzle
		#left_puzzle
		#up_puzzle


	#puzzle_counter is just a counter for check how mane puzzles are made... it saves in puzzle [4][0]

	#max_step is a controller for steps in DFS and BFS algoritm... the STEP COUNTER is saves in puzzle [4][2]

	# free_r : is raw number of free cell (00)
	# free_c : is Column number of free cell 

	# search_method: selecting search algorithm >>> 1 for DFS 	2 for BFS

	# solve_flag: explained in MAPPING explanations in NOTES section

	#following names are explained in MAPPING explanations in NOTES section
		# map_up
		# map_down
		# map_left
		# map_right


#NOTES:
   # 00 is puzzle free space

   # we have:
		# one stack for dfs algorithm
		# two queues:
			# bfs algorithm queue (main queue)
			# mapping queue


   # 6th member of puzzle: 
		#1= puzzle index      
		#2= step index      
		#3= last move (up, down, left, right) for crawling section
		#4= last move for mapping section (u, d, l, r)


   #MAPPING:
		# for mapping we have a queue in 6th member of puzzle... it means puzzle[5][3] is a queue
		# if we have a up action we add 'map_up' to this queue... if we have a down action we add 'map_down'.........
		# in the end of the program we will check if the puzzle is solved then we simulating the solving progress with popleft the queue
		# so we have another flag... solve_flag
		# names:
			# map_up		# map_down		# map_left		# map_right
		# mapping queue is in puzzle[5][3]

	#IMPORTANT NODE:
		# THESE ALGORITHMS ARE AVOIDING FROM REPEATED NODES



#__________________________________________________________________________________________________________________________________________________________________________________________________________



#for Deepcopy
import copy
#for Queue 
from collections import deque
#for stopping program
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



#selecting search algorithm
search_method = input ("select search algorithm \n  1 >>> DFS \n  2 >>> BFS\n  3 >>> IDS\n  ")

max_step = int (input ("How many steps could we crawl the tree?\n"))
print ('\n\n\n')

#check the search_method number is correct or not
if (search_method != '1') and (search_method != '2') and (search_method != '3'):

	print ("\n\n\n=================================\n    WRONG SELECTION!!!!!!!!!!!!\n=================================\n\n\n")
	sys.exit()


getting_r = 1
getting_c = 1


puzzle2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20] ,[21, 22, 23, 24, 00],[0,0,'',[]]]


#make MAPPING queue
puzzle2[5][3] = deque()



#getting puzzle numbers
for i in range( 0, 5 ) :
   
	for j in range ( 0, 5 ) :
		print ( "Enter Cell -> Row", getting_r, " Column", getting_c, ": " )
		getting_c = getting_c+1
		puzzle2[i][j] = int( input() )
	   
		if puzzle2[i][j] > 24 :
			print ("\n\n\n=================================\n    LARGE NUMBER ERROR !!!!!!!!!!!!!!\n=================================\n\n\n")
			sys.exit()
													  
	getting_r = getting_r+1
	getting_c = 1
	print ("________________________________")



print ("\n\n\n=================================\n      THINKING!!!!!!!!!!!!!!\n=================================\n\n\n")



solved = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20] ,[21, 22, 23, 24, 00],[0,0,'',[]]]



#__________________________________________________________________________________________________________________________________________________________________________________________________________

############### START DFS
if (search_method == '1'):

	
	stack.append (puzzle2)

	while 1:

		#print ("\n\n\nStack -> ",stack)
	
		#load new puzzle from stack
		puzzle = stack.pop()


		#check it is solved or not
		if (puzzle[0:5] == solved[0:5]):
			print ("\n\n\n=================================\n      SOLVED!!!!!!!!!!!!!!\n=================================\n\n\n")

			#set solve flag to 1 for print map 
			solve_flag = 1

			#we append 'finish' to map queue to find out when we dont have any other move
			puzzle[5][3].append('finish')

			break
	

		#finding free cell coords
		for i in range (0,5):
			for j in range (0,5):
				if puzzle[i][j] == 00:
					free_r = i
					free_c = j

	

		#check we reached to max depth or not
		if (puzzle[5][1]<max_step):


			#BUILDING NEW NODES

			##UP
			#check for first row. in first row you cant up
			if free_r != 0 :
				#check for last move. if last move was down you cant up
				if puzzle[5][2] != 'down' :
					#making a deep copy from puzzle to change that
					up_puzzle = copy.deepcopy(puzzle)	

					#changing puzzle
					up_puzzle[ free_r ][ free_c] = up_puzzle[ free_r-1 ][ free_c ]
					up_puzzle[ free_r -1 ][ free_c ] = 00


					#increase puzzle counter and save that
					puzzle_counter = puzzle_counter+1
					up_puzzle[5][0] = puzzle_counter	

					#saving increased step
					up_puzzle[5][1] = up_puzzle[5][1]+1	

					#saving last move
					up_puzzle[5][2] = 'up'

					#turn on up flag. it will be checked when this puzzle should be stacked...
					#we stack puzzle later. (explained)
					up_flag = 1

					#append map_up to the map queue 
					up_puzzle[5][3].append('map_up')
				



			##LEFT
			#check for first column. in first column you cant left
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





			##DOWN
			#check for last raw. in last raw you cant down
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
				


			##RIGHT
			#check for last column. in last column you cant right
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


		#STACKING NEW NODES
		#we stack puzzles in reverse... 
		#for example we made them in this order U L D R...
		#but we stack them in this order R D L U...
		#this is related to BTS algorithm.

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
######### end of  DFS

#__________________________________________________________________________________________________________________________________________________________________________________________________________

############### START BFS
elif (search_method == '2'):

	#make a queue for bfs algorithm
	queue = deque()
	queue.append (puzzle2)

	while 1:
	
		#load new puzzle from stack
		puzzle = queue.popleft()


		#check it is soled or not
		if (puzzle[0:5] == solved[0:5]):
			print ("\n\n\n=================================\n      SOLVED!!!!!!!!!!!!!!\n=================================\n\n\n")

			solve_flag = 1

			#we append 'finish' to map queue to find out when we dont have any other move
			puzzle[5][3].append('finish')

			break
	

		#finding free cell coords
		for i in range (0,5):
			for j in range (0,5):
				if puzzle[i][j] == 00:
					free_r = i
					free_c = j

	

		#check we reached to max depth or not
		if (puzzle[5][1]<max_step):


			#BUILDING NEW NODES

			##UP
			#check for first row. in first row you cant up
			if free_r != 0 :
				#check for last move. if last move was down you cant up
				if puzzle[5][2] != 'down' :
					#making a deep copy from puzzle to change that
					up_puzzle = copy.deepcopy(puzzle)	

					#changing puzzle
					up_puzzle[ free_r ][ free_c] = up_puzzle[ free_r-1 ][ free_c ]
					up_puzzle[ free_r -1 ][ free_c ] = 00


					#increase puzzle counter and save that
					puzzle_counter = puzzle_counter+1
					up_puzzle[5][0] = puzzle_counter	

					#saving increased step
					up_puzzle[5][1] = up_puzzle[5][1]+1	

					#saving last move
					up_puzzle[5][2] = 'up'

					#append up_puzzle to the bfs queue
					queue.append (up_puzzle)

					#append map_up to the map queue 
					up_puzzle[5][3].append('map_up')
				
					



			##LEFT
			#check for first column. in first column you cant left
			if free_c != 0 :
				if puzzle[5][2] != 'right':
					left_puzzle = copy.deepcopy(puzzle)
					left_puzzle[free_r][free_c] = left_puzzle[free_r][free_c-1]
					left_puzzle[free_r][free_c-1] = 00	

					puzzle_counter = puzzle_counter+1
					left_puzzle[5][0] = puzzle_counter
					left_puzzle[5][1] = left_puzzle[5][1]+1
					left_puzzle[5][2] = 'left'


					queue.append (left_puzzle)

					left_puzzle[5][3].append('map_left')





			##DOWN
			#check for last raw. in last raw you cant down
			if free_r != 4:
				if puzzle[5][2] != 'up':
					down_puzzle = copy.deepcopy(puzzle)
					down_puzzle[ free_r ][ free_c] = down_puzzle[ free_r+1 ][ free_c ]
					down_puzzle[ free_r +1 ][ free_c ] =  00	

					puzzle_counter = puzzle_counter+1
					down_puzzle[5][0] = puzzle_counter
					down_puzzle[5][1] = down_puzzle[5][1]+1
					down_puzzle[5][2] = 'down'
					

					queue.append (down_puzzle)

					down_puzzle[5][3].append('map_down')
	
				

			##RIGHT
			#check for last column. in last column you cant right
			if free_c != 4 :
				if puzzle[5][2] != 'left':
					right_puzzle = copy.deepcopy(puzzle)
					right_puzzle[free_r][free_c] = right_puzzle[free_r][free_c+1]
					right_puzzle[free_r][free_c+1] = 00

					puzzle_counter = puzzle_counter+1
					right_puzzle[5][0] = puzzle_counter
					right_puzzle[5][1] = right_puzzle[5][1]+1
					right_puzzle[5][2] = 'right'


					queue.append (right_puzzle)

					right_puzzle[5][3].append('map_right')
######### end of  BFS

#__________________________________________________________________________________________________________________________________________________________________________________________________________

############### START IDS
if (search_method == '3'):
	
	stack.append (puzzle2)

	while 1:

		#print ("\nStack -> ",stack)

		#we need this if because we should start over when stack is empty and we dont find any answers yet.
		# so first we check stack if it is empty increse temp_limit and push our question to stack and start over
		if len(stack) == 0:
			temp_limit = temp_limit+1
			print("TEMP LIMIT INCREASED !!!!!!!!! = ",temp_limit)
			stack.append (puzzle2)
			continue
	
		#load new puzzle from stack
		puzzle = stack.pop()


		#check it is solved or not
		if (puzzle[0:5] == solved[0:5]):
			print ("\n\n\n=================================\n      SOLVED!!!!!!!!!!!!!!\n=================================\n\n\n")

			#set solve flag to 1 for print map 
			solve_flag = 1

			#we append 'finish' to map queue to find out when we dont have any other move
			puzzle[5][3].append('finish')

			break

		# we should stop appending puzzles that have steps more than temp_limit.
		# so we can dont puzzles that their mother have steps one less than limit.
		# for example if temp_limit is 5 and mother puzzle have 5 steps its children will have 6 step and we shouldnt add them. 
		if puzzle[5][1] >= temp_limit:
			continue
	

		#finding free cell coords
		for i in range (0,5):
			for j in range (0,5):
				if puzzle[i][j] == 00:
					free_r = i
					free_c = j

				
		#check we reached to max depth or not
		if (puzzle[5][1]<max_step):


			#BUILDING NEW NODES

			##UP
			#check for first row. in first row you cant up
			if free_r != 0 :
				#check for last move. if last move was down you cant up
				if puzzle[5][2] != 'down' :
					#making a deep copy from puzzle to change that
					up_puzzle = copy.deepcopy(puzzle)	

					#changing puzzle
					up_puzzle[ free_r ][ free_c] = up_puzzle[ free_r-1 ][ free_c ]
					up_puzzle[ free_r -1 ][ free_c ] = 00


					#increase puzzle counter and save that
					puzzle_counter = puzzle_counter+1
					up_puzzle[5][0] = puzzle_counter	

					#saving increased step
					up_puzzle[5][1] = up_puzzle[5][1]+1	

					#saving last move
					up_puzzle[5][2] = 'up'

					#turn on up flag. it will be checked when this puzzle should be stacked...
					#we stack puzzle later. (explained)
					up_flag = 1

					#append map_up to the map queue 
					up_puzzle[5][3].append('map_up')
				



			##LEFT
			#check for first column. in first column you cant left
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





			##DOWN
			#check for last raw. in last raw you cant down
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
				


			##RIGHT
			#check for last column. in last column you cant right
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


		#STACKING NEW NODES


		#we stack puzzles in reverse... 
		#for example we made them in this order U L D R...
		#but we stack them in this order R D L U...
		#this is related to BTS algorithm.
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
######### end of  IDS

#__________________________________________________________________________________________________________________________________________________________________________________________________________


############ start of  MAPPING
		
map_counter = -1

if solve_flag == 1:
	while 1:

		#send next map to move        
		move = puzzle[5][3].popleft()
		map_counter = map_counter + 1 
		

		#print it
		print ("=====================")
		print (puzzle2[0])
		print (puzzle2[1])
		print (puzzle2[2])
		print (puzzle2[3])
		print (puzzle2[4])
		print ("=====================")

		#finding free cell
		for i in range (0,5):
			for j in range (0,5):
				if puzzle2[i][j] == 00:
					free_r = i
					free_c = j


		if move == 'map_right':
			print ("\n\n\nMOVE RIGHT")
			puzzle2[free_r][free_c] = puzzle2[free_r][free_c+1]
			puzzle2[free_r][free_c+1] = 00

		if move == 'map_up':
			print ("\n\n\nMOVE UP")
			puzzle2[ free_r ][ free_c] = puzzle2[ free_r-1 ][ free_c ]
			puzzle2[ free_r -1 ][ free_c ] = 00

		if move == 'map_down':
			print ("\n\n\nMOVE DOWN")
			puzzle2[ free_r ][ free_c] = puzzle2[ free_r+1 ][ free_c ]
			puzzle2[ free_r +1 ][ free_c ] =  00

		if move == 'map_left':
			print ("\n\n\nMOVE LEFT")
			puzzle2[free_r][free_c] = puzzle2[free_r][free_c-1]
			puzzle2[free_r][free_c-1] = 00	

		if move == 'finish':
			print ("FINAL\n\n\n=================================\n        THIS IS IT :))\n=================================")
			print("=================================\n      IN JUST ",map_counter," MOVES!!!\n=================================\n\n\n")
			while 1:
				pass
			break


