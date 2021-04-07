from collection import deque

class Solution:
	def isLandCounter(M): # input is a matrix 
		if (M == None or M == [[]]):
			return 0
			# null case first 
		islands = 0
		c = len(M[0])
		r = len(M)

		for i in range(r):
			for j in range(c):
				if M[i][j] == 1:
					islands += 1
					FindPartsOfIsland(M, i, j, r, c)
					# BFS: define a help function to do that 

	def FindPartsOfIsland(M, i, j, c, r):
		q = deque()
		q.append([i, j])
		while(len(q) != 0):
			i = q.pop()
			x = i[0]
			y = i[1]
			if (M[x][y] == 1):
				M[x][y] = 2
				appendIF(q, r, c, x+1, y)
				appendIF(q, r, c, x, y+1)
				appendIF(q, r, c, x-1, y)
				appendIF(q, r, c, x, y-1)

	def appendIF(q, r, c, x, y):
		if (x > 0 and x < c and y > 0 and y < r):
			q.append(x, y)

