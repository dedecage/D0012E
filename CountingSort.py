def CountingSort(A):
    
    size = len(A)
    output = [0] * size

    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[A[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    
    while i >= 0:
        
        # Output index will correspond to cumulative count - 1
        indexConversion = count[A[i]]-1
        
        output[indexConversion] = A[i]
        count[A[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        A[i] = output[i]


A = [4, 2, 2, 8, 3, 3, 1]
CountingSort(A)
print(A)

# Algorithm is not in place
# Algorithm is stable (no left- to right rearrangements)
# Best case running time O(n+k) (k = input range)
# Worst case running time O(n+k)
# Average case running time O(n+k)

# Counting sort is useful when the input range is small and space complexity is
# of little importance. The algorithm also has a space complexity of O(n+k)

# https://www.youtube.com/watch?v=7zuGmKfUt7s&feature=emb_logo
# Note that the video creates an output array based on cumulative count
# with off by one indexing. Here the output instead matches the size
# of the input array with standard indexing, hence indexConversion will convert
# to count[A[i]]-1 instead of places[A[i]] as would be the case in the video
