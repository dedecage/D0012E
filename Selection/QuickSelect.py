""" QuickSelect is an algorithm that selects the k:th
    smallest element in expected O(n) time, and worst
    case O(n^2) """

from random import randint

def QuickSelect(A, i):

    if len(A) == 1:
        return A[0]
    
    else:
        # Pick a random pivot element
        pivot = A[randint(0, len(A)-1)]
                        
        # Partitioning step
        low = [j for j in A if j < pivot]
        high = [j for j in A if j > pivot]

        k = len(low)

        if i < k:
            return QuickSelect(low,i)
        elif i > k:
            return QuickSelect(high,i-k-1)
        else:
            return pivot


A = [1, 2, 3, 4, 5, 1000, 8, 9, 99]
print(QuickSelect(A, 6))
