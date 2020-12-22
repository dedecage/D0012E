def CountingSort(A, radix):
    
    size = len(A)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = A[i] // radix
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = A[i] // radix
        output[count[index % 10] - 1] = A[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        A[i] = output[i]
        

def RadixSort(A):
    
    maxVal = max(A)

    radix = 1
    while maxVal // radix > 0:
        CountingSort(A, radix)
        radix *= 10


A = [121, 432, 564, 23, 1, 45, 788]
RadixSort(A)
print(A)

# Algorithm is not in place
# Algorithm is stable (no left- to right rearrangements)
# Best case running time O(d(n+k)) (d = number cycle. Ex: 3 where max is 100-999)
# Worst case running time O(d(n+k))
# Average case running time O(d(n+k))

# Time complexities assume the use of counting sort
