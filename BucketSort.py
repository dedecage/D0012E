from InsertionSort import*

def BucketSort(A):

    bucket = []

    # Create as many buckets as there are elements
    for i in range(len(A)):
        bucket.append([])

    # Put into buckets
    for j in A:
        bucketIndex = int(10*j)
        bucket[bucketIndex].append(j)

    # Sort buckets
    for k in range(len(A)):
        InsertionSort(bucket[k])

    # Merge buckets
    k=0
    for i in range(len(A)):
        for j in range(len(bucket[i])):
            A[k] = bucket[i][j]
            k+=1
            

A = [.42, .32, .33, .52, .37, .47, .51]
BucketSort(A)
print(A)

# Algorithm is not in-place (buckets consume extra space)
# Algorithm is stable (since insertion sort is stable)
# Best case running time: O(n+k) (k = amount of buckets)
# Worst case running time: O(n^2) (all elements in one bucket, i.e regular insertion sort)
# Average case running time: O(n+k)
