def MergeSort(A):

    if len(A) == 1:
        return A

    else:
        
        mid = len(A) // 2
    
        L = A[:mid]
        R = A[mid:]

        MergeSort(L)
        MergeSort(R)

        Merge(A, L, R)

def Merge(A, L, R):

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i+=1
            k+=1
        else:
            A[k] = R[j]
            j+=1
            k+=1

    # Add leftover elements
    while i < len(L):
        A[k] = L[i]
        i+=1
        k+=1

    while j < len(R):
        A[k] = R[j]
        j+=1
        k+=1
        

A = [2, 8, 5, 3, 9, 4, 1]
MergeSort(A)
print(A)

# Algorithm is not in place (divided arrays take up extra memory)
# Algorithm is stable (no left- to right rearranging during merge step)
# Best case running time: O(nlogn)
# Worst case running time: O(nlogn)
# Average case running time: O(nlogn)
