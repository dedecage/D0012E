def MaxHeapify(A, heapSize, i):
    
    left = 2*i+1
    right = 2*i+2
    largest = i
    
    if left < heapSize and A[left] > A[largest]:
        largest = left
        
    if right < heapSize and A[right] > A[largest]:
        largest = right
        
    if i != largest:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A, heapSize, largest)
        

def BuildHeap(A):
    
    heapSize = len(A)
    
    for i in range (int(heapSize/2)-1, -1, -1):
        MaxHeapify(A, heapSize, i)
        

def HeapSort(A):
    
    heapSize = len(A)
    BuildHeap(A)
    
    for i in range(heapSize-1, 0, -1):
        
        A[0], A[i] = A[i], A[0]
        heapSize -= 1
        MaxHeapify(A, heapSize, 0)
        

A = [2, 8, 1, 4, 14, 7, 16, 10, 9, 3]
HeapSort(A)
print(A)

# Algorithm is in-place (no added subarrays)
# Algorithm is unstable (no maintenance during heapify)
# Best case running time: O(nlogn)
# Worst case running time: O(nlogn)
# Average case running time: O(nlogn)

# https://brilliant.org/wiki/heap-sort/
