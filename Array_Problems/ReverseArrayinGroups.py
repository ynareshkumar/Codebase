#http://www.geeksforgeeks.org/reverse-an-array-in-groups-of-given-size/
#Given an array, reverse every sub-array formed by consecutive k elements.

#Examples:

#Input: 
#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#k = 3
#Output:  
#[3, 2, 1, 6, 5, 4, 9, 8, 7]

def reverseArrinGroup(a,k):
	if k > len(a) or k < 2:
		return a
	j=1
	m=k*j-1
	i = 0
	while i < len(a):
		if i < m:
			tmp=a[m]
			a[m] = a[i]
			a[i] = tmp
			i = i+1
			m = m-1
		else:
			i = k*j
			j = j+1
			if k*j-1 < len(a):
				m=k*j-1
			else:
				m = len(a)-1
	return a
		

a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
k=2
print("Reverse in group ",reverseArrinGroup(a,k));
