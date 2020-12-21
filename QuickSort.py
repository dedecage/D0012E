def QuickSort(A, start, end):
    
    if start >= end:
        return

    p = Partition(A, start, end)
    QuickSort(A, start, p-1)
    QuickSort(A, p+1, end)
    

    
def Partition(A, start, end):
    
    pivot = A[start]
    low = start + 1
    high = end

    while True:
        while low <= high and A[high] >= pivot:
            high -= 1

        while low <= high and A[low] <= pivot:
            low += 1

        if low <= high:
            A[low], A[high] = A[high], A[low]
        else:
            break

    # Place pivot element at its correct index
    A[start], A[high] = A[high], A[start]

    return high


A = [2, 8, 5, 3, 9, 4, 1]
QuickSort(A, 0, 6)
print(A)

# Algorithm is in-place (no subarrays created as opposed to merge sort)
# Algorithm is not stable
# Best case running time: O(nlogn)
# Worst case running time: O(n^2) (consistently bad pivot elements, reverse sorted)
# Average case running time: O(nlogn)
