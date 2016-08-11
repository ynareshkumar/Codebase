#Function which takes a number as input and returns the individual digits as output. Eg: 12 -> [1,2],  4 -> [4]
def splitassingledigits(num):
	outarr = []
	while ((int)(num/10) != 0):
		outarr.append(num%10)
	#	print('Outarr is ',outarr)
		num = (int)(num/10)
	outarr.append(num)	
	return reversed(outarr)

#Function that takes input 2 arrays and returns the sum of element of arrays as single digits
#Given two integer arrays, add their elements into third array by satisfying following constraints –
#
#1. Addition should be done starting from 0th index of both arrays.
#2. Split the sum if it is a not a single digit number and store the digits in adjacent locations in output array.
#3. Output array should accommodate any remaining digits of larger input array.
#http://www.geeksforgeeks.org/add-elements-given-arrays-given-constraints/
def sumtwoarrays(a,b):
	m = len(a)
	n = len(b)
	out = []
	m1=0
	n1=0
	#print('entering')
	for i in a:
		if (n1 < n):
			out.extend(splitassingledigits(i+b[n1]))
			#print('Tempoutput is ',out)
			n1+=1
		else:
			out.append(i)
		m1+=1

	while (n1 < n):
		out.extend(splitassingledigits(b[n1]))
		n1+=1
	return out
	
a = [9, 2, 3, 7, 9, 6, 6, 9]
b = [3, 1, 4, 7, 8, 7, 100, 200]
out = sumtwoarrays(a,b)
print(out)