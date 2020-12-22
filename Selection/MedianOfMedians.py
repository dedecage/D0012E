""" Median of medians is an algorithm that selects the k:th
    smallest element in O(n) time"""

def MedianOfMedians(A, i):

    chunks = [A[j:j+5] for j in range(0, len(A), 5)]
    medians = [sorted(chunk)[int(len(chunk)/2)] for chunk in chunks]
    
    if len(medians) <= 5:
        pivot = sorted(medians)[int(len(medians)/2)]
    else:
        pivot = MedianOfMedians(medians, len(medians)/2)

    # Partitioning step
    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)
    
    if i < k:
        return MedianOfMedians(low,i)
    elif i > k:
        return MedianOfMedians(high,i-k-1)
    else:
        return pivot


A = [1, 2, 3, 4, 5, 1000, 8, 9, 99]
print(MedianOfMedians(A, 7))

# https://brilliant.org/wiki/median-finding-algorithm/
