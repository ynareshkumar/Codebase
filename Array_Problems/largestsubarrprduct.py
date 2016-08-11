#Given an array consisting of n positive integers, and an integer k. Find the largest product subarray of size k, i.e., find maximum product of k contiguous elements in the array where k <= n. Examples:
#Input: arr[] = {1, 5, 9, 8, 2, 4,
#                1, 8, 1, 2} 
#     k = 6
#Output:   4608  
#The subarray is {9, 8, 2, 4, 1, 8}
#http://www.geeksforgeeks.org/largest-product-subarray-size-k/

def largestsubarrproduct(a, k):
    if k > len(a) or k <= 0:
        print ('Invalid argument value k')
        return []
    m = 0
    prodsofar = 1
    index = 0
    for i in a:
        m += 1
        prodsofar *= i
        if m == k:
            maxprod = prodsofar
        elif m > k:
            prodsofar = int(prodsofar / a[index])
            index += 1
            if maxprod < prodsofar:
                maxprod = prodsofar

    return maxprod


a = [1, 5, 9, 8, 2, 4, 1, 8, 1, 2]
out = largestsubarrproduct(a, 3)
print ('Output arr is ', out)