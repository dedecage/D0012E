import collections
import sys

class Graph:
    
    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for i in range(size)] for j in range(size)] 


    def BFS(self): 
        visited = [False] * self.size
        queue = [0] 
        visited[0] = True
        while queue:
            vis = queue[0] 
            print("Breadth first search visiting: ", vis) 
            queue.pop(0) 
            for i in range(self.size): 
                if (self.matrix[vis][i] > 0 and 
                      (not visited[i])): 
                    queue.append(i) 
                    visited[i] = True


    def DFS(self):
        visited = [False] * self.size
        self.recDFS(0, visited)
        

    def recDFS(self, current, visited):
        print("Depth first search visiting: ", current) 
        visited[current] = True
        for i in range(self.size): 
            if (self.matrix[current][i] > 0 and
                    (not visited[i])): 
                self.recDFS(i, visited)
        


    def printMST(self, tree): 
        print ("Edge \tWeight")
        for i in range(1, self.size):
            print (tree[i], "-", i, "\t", self.matrix[i][ tree[i] ])


    def minWeight(self, edge_weights, mstSet):
        min = sys.maxsize
        for vertex in range(self.size):
            # If the edge_weight is the lowest one, and the vertex
            # has not been picked
            if edge_weights[vertex] < min and not mstSet[vertex]:
                min = edge_weights[vertex]
                min_index = vertex
        return min_index


    # O(n^2)
    def prim(self):
        edge_weights = [sys.maxsize] * self.size
        edge_weights[0] = 0
        mstSet = [False] * self.size # Picked vertices in the graph
        tree = [None] * self.size # Element is v1, index is connected v2    
        for iteration in range(self.size):
            # Get vertex with lowest edge weight
            next_v = self.minWeight(edge_weights, mstSet)
            # Put vertex with lowest edge weight in mstSet
            mstSet[next_v] = True 
            for i in range(self.size):
                edge = self.matrix[next_v][i]
                if edge > 0 and not mstSet[i] and edge_weights[i] > edge:
                    edge_weights[i] = edge
                    tree[i] = next_v
        self.printMST(tree)


g = Graph(5)

g.matrix = [[0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 
  
g.prim()
g.BFS()
g.DFS()

# https://www.geeksforgeeks.org/
