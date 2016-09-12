#Direction at last square block
#Given a R x C (1 <= R, C <= 1000000000) grid and initial position as top left corner and direction as east. Now we start running in forward direction and cross each square blocks of matrix. Whenever we find dead end or reach a cell that is already visited, we take right because we can not cross the visited square blocks again. Tell the direction when we will be at last square block.

#For example : Consider the case with R = 3, C = 3. The path followed will be (0,0) — (0,1) — (0,2) — (1,2) — (2,2) — (2,1) — (2,0) — (1,0) — (1,1). At this point, all squares have been visited, and is facing right.

#http://www.geeksforgeeks.org/direction-last-square-block/


def matrixspiral(R,C):
	if R < 0 or C < 0:
		return None
	a = [[None] * C for i in range(R)]
	i = 0
	j = 0
	a[i][j] = 1
	curdirection = "Right"
	while (True):
		print(a)
		if (j+1) < C and a[i][j+1] == None:
			j += 1
			a[i][j] = 1
			curdirection = "Right"
		elif (i+1) < R and a[i+1][j] == None:
			i += 1
			a[i][j] =1
			curdirection = "Down"
		elif (j-1) >= 0 and a[i][j-1] == None:
			j -= 1
			a[i][j] = 1
			curdirection = "Left"
		elif (i-1) >= 0 and a[i-1][j] == None:
			i -= 1
			a[i][j] = 1
			curdirection = "Up"
		else:
			return curdirection
	
	print ("Matrix is currently ",a)	
	
print ("Final direction is ",matrixspiral(3,1))
	


