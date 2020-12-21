def SelectionSort(A):

    for j in range(0, len(A)):

        Min = j

        for i in range(j, len(A)):

            if A[i] < A[Min]:
                Min = i

        if Min != j:
            A[j], A[Min] = A[Min], A[j]


A = [2, 8, 5, 3, 9, 4, 1]
SelectionSort(A)
print(A)

# Algorithm is in-place
# Algorithm is not stable due to unregulated swap, but can be made stable
# Best case running time: O(n^2)
# Worst case running time: O(n^2)
# Average case running time: O(n^2)
