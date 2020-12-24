# Exercise 2.3-5

# Best case: O(1), worst case: O(logn)

def BinarySearch(A, v, low, high):

    if low > high:
        return None

    mid = (low + high) // 2

    if A[mid] == v:
        return mid
    
    elif A[mid] < v:
        return BinarySearch(A, v, low, mid-1)
    
    return BinarySearch(A, v, mid+1, high)


A = [1, 2, 3, 4, 5, 6]
print(BinarySearch(A, 3, 0, 5))
print(BinarySearch(A, 7, 0, 5))
