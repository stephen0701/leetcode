# Longest consecutive ones in a matrix
from typing import List

"""
Depth first search on 4 directions(up, down, right, left) to find if there is any consecutive 1.
Add the visited position into a set so that it won't be counted repeatedly and reduce consumed time.
"""
def longestOnes(matrix: List[List[int]]) -> int:

	visited = set()
	def dfs(x, y):
	
		# Check whether the position is out of bound
		if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[x]):
			return 0
		# Check the value of the position
		elif matrix[x][y]==0:
			return 0
		# Check whether the value has been visited
		elif (x, y) in visited:
			return 0
		else:
			visited.add((x,y))
			return 1+dfs(x-1, y)+dfs(x, y-1)+dfs(x, y+1)+dfs(x+1, y)
		
	result = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):	
			result = max(result, dfs(i, j))
	return result


matrix = [[0, 0, 1, 1, 0, 1],
		  [0, 0, 1, 0, 0, 1],
		  [1, 0, 1, 0, 0, 1],
		  [0, 1, 1, 1, 0, 1],
		  [0, 0, 0, 1, 0, 1],
		  [1, 0, 1, 0, 0, 1]]
print(longestOnes(matrix))

matrix = [[1, 1, 1, 1],
		  [1, 1, 1, 1],
		  [1, 1, 1, 1],
		  [1, 1, 1, 1]]
print(longestOnes(matrix))

matrix = [[0, 0, 0, 0],
		  [0, 0, 0, 0],
		  [0, 0, 0, 0],
		  [0, 0, 0, 0]]
print(longestOnes(matrix))

matrix = [[1, 1, 0, 1, 1],
		  [1, 0, 0, 1],
		  [1, 0, 0, 1],
		  [1, 1, 1, 1]]
print(longestOnes(matrix))