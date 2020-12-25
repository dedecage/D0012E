# Exercise 4.1-5)

import sys

def FindMaximumSubarray(A):

    maxSum = Sum = -sys.maxsize
    
    for j in range(len(A)):
        
        currentHigh = j
        
        if Sum > 0:
            Sum += A[j]
        else:
            currentLow = j
            Sum = A[j]

        if Sum > maxSum:
            maxSum = Sum
            low = currentLow
            high = currentHigh
            
    return A[low:high+1]

A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(FindMaximumSubarray(A))

A = [-2, -3, 4, -1, -2, 1, 5, -3]
print(FindMaximumSubarray(A))
