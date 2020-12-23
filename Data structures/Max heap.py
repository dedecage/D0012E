""" Insertion: O(logn), Delete min: O(logn), Build heap: O(n). """

class MaxHeap: 
     
    def __init__(self, A=[]):
        
        self.size = len(A)
        self.heap = A

        # Build heap if array is passed to contstructor
        for i in range(int(self.size//2), -1, -1):
            self.maxHeapify(i)

  
    def parent(self, pos): 
        return pos//2
  

    def left(self, pos): 
        return 2 * pos 
  

    def right(self, pos): 
        return (2 * pos) + 1
  

    def isLeaf(self, pos):
        
        if pos >= (self.size//2) and pos <= self.size: 
            return True
        
        else:
            return False
  

    def swap(self, a, b): 
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a] 
  

    def maxHeapify(self, pos):
        
        if not self.isLeaf(pos):
            if (self.heap[pos] < self.heap[self.left(pos)] or 
               self.heap[pos] < self.heap[self.right(pos)]): 
  
                if self.heap[self.left(pos)] > self.heap[self.right(pos)]: 
                    self.swap(pos, self.left(pos)) 
                    self.maxHeapify(self.left(pos))
                else: 
                    self.swap(pos, self.right(pos)) 
                    self.maxHeapify(self.right(pos)) 
  
 
    def insert(self, element):

        self.heap.append(element)
        self.size+= 1
        current = self.size - 1 
  
        while self.heap[current] > self.heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current)
  

    def remove(self):

        if self.size == 0:
            return
        
        popped = self.heap[0] 
        self.heap[0] = self.heap[self.size-1] 
        self.size-= 1
        self.maxHeapify(0) 
        return popped 
  


maxHeap = MaxHeap()

maxHeap.insert(84) 
maxHeap.insert(5) 
maxHeap.insert(3) 
maxHeap.insert(17) 
maxHeap.insert(10) 
maxHeap.insert(19) 
maxHeap.insert(6) 
maxHeap.insert(22) 
maxHeap.insert(9)

for i in range(0, 9):
    print(maxHeap.remove())

A = [84, 5, 3, 17, 10, 19, 6, 22, 9]
maxHeap2 = MaxHeap(A)

for i in range(0, 9):
    print(maxHeap2.remove())
