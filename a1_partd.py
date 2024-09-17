# copy over your a1_partd.py file here
#    Main Author(s): Anthony Sin
#    Main Reviewer(s): Siripa Purinruk, Sayeda Insha Fatima Zaidi

from a1_partc import Queue

"""
Purpose: Iterate through the grid which was passed through as a paramenter
			to find any indices that are overflowing
Parameters:
1. 2D array grid
Return Value: Collection of tuples that are overflowing
Limitations: Large amount of tuples
"""
def get_overflow_list(grid):	
	rows = len(grid)
	cols = len(grid[0])
	overflow_list = {}

	# Iterate through all indices to determine the amount of neighbours
	for x in range(rows):
		for y in range(cols):
			# Corners of the grid
			if (x == 0 or x == rows - 1) and (y == 0 or y == cols - 1):
				neighbors = 2
			# Outer edges of the grid that aren't the corner
			elif x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
				neighbors = 3
			# Inner grid
			else:
				neighbors = 4

			# Value inside the tuple more than/equal to its neighbour, consider it an overflowing
			# cell and add it to the dictionary
			cell_value = abs(grid[x][y])
			if cell_value >= neighbors:
				overflow_list[(x, y)] = True
	
	# If the above logic doesn't produce any tuples
	if not overflow_list:
		return None
	return overflow_list

"""
Purpose: Recursively modify a grid that has overflowing values and modify their neighbours, and then create
			a copy of the modified grid and pass it to the queue.
Parameters:
1. Grid (2D array of integers)
2. Instance of Queue class defined in partC
Return Value: Integer value of the number of recursive calls.
Limitations: None
"""
def overflow(grid, a_queue):
	overflow_list = get_overflow_list(grid)

	# Check grid if all values have the same sign (positive or negative)
	all_pos, all_neg = True, True
	for row in grid:
		for value in row:
			if value < 0:
				all_pos = False
			elif value > 0:
				all_neg = False
			if not all_pos and not all_neg:
				break
		
	# Base case:
	# If get_overflow_list is empty, or grid is the same sign, exit the recursion
	if overflow_list is None or all_pos or all_neg:
		return 0
	
	# Create a shallow copy of the grid so we can modify the original grid
	grid_copy = [row[:] for row in grid]
	
	# Set overflowing cells to 0
	for row, col in overflow_list:
		grid[row][col] = 0

	# Modify neighbours of overflowing cells
	for x, y in overflow_list:
		neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
		# Neighbours that are within bounds of the grid are modified
		for row, col in neighbours:
			if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
				# Increment or decrement the value of neighbours based on overflowing sign
				cell_value = abs(grid[row][col])
				if grid_copy[x][y] < 0:
					grid[row][col] = -(cell_value + 1)
				else:   
					grid[row][col] = cell_value + 1

	# Pass a copy of the newly updated grid to the queue
	a_queue.enqueue([row[:] for row in grid])

	return 1 + overflow(grid,a_queue)