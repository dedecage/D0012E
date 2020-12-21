def InsertionSort(A):
    
    for j in range(1, len(A)):
        
        key = A[j]
        i = j-1

        while i >= 0 and A[i] > key:
            
            A[i+1] = A[i]
            i-=1
            
        A[i+1] = key
    
A = [5, 2, 4, 6, 1, 3]
InsertionSort(A)
print(A)

# Algorithm is in-place
# Algorithm is stable
# Best case running time: O(n) (when already sorted)
# Worst case running time: O(n^2) (when sorted in reverse order)
# Average case running time: O(n^2)
