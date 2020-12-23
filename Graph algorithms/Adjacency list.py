import sys
from Heap import*


"""https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/ """
class Node:
    
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.next = None


class Graph:
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [None] * self.vertices

    # Method for adding an undirected edge between two nodes 
    def addEdge(self, source, destination, weight):
        if weight < 1:
            return
        # Create first node and link it to the source index
        node = Node(destination, weight)
        node.next = self.adj_list[source]
        self.adj_list[source] = node
        # Create second node and link it to the destination index
        node = Node(source, weight)
        node.next = self.adj_list[destination]
        self.adj_list[destination] = node


    # Prints the graph
    def print_graph(self):
        for i in range(self.vertices):
            print("Vertex " + str(i) + ":", end="")
            temp = self.adj_list[i]
            while temp:
                print(" -> {}".format(temp.value),
                      "( weight: {}".format(temp.weight),
                      ")", end="")
                temp = temp.next
            print(" \n")


    # Prints a minimum spanning tree
    def printMST(self, tree, edge_weights): 
        print ("Edge \tWeight")
        for i in range(1, self.vertices): 
            print (tree[i], "-", i, "\t", edge_weights[i])


    # O(ELogV), E = edges, V = vertices
    def prim(self):
        
        edge_weights = [sys.maxsize] * self.vertices
        tree = [None] * self.vertices

        # Load all vertices to the heap
        heap = Heap()
        for vertex in range(self.vertices):
            heap.add(vertex, sys.maxsize)
            
        # Initialize starter vertex
        heap.pos[0] = 0
        edge_weights[0] = 0
        heap.decreaseWeight(0, 0)
        
        while heap.isEmpty() == False: # O(V)
            current = heap.pop() # O(LOG(V))
            temp = self.adj_list[current[0]]
            while temp: # O(E)
                if heap.inHeap(temp.value) and edge_weights[temp.value] > temp.weight:
                    edge_weights[temp.value] = temp.weight
                    tree[temp.value] = current[0]
                    heap.decreaseWeight(temp.value, temp.weight) # O(LOG(V)
                temp = temp.next
        self.printMST(tree, edge_weights)
        

graph = Graph(9) 
graph.addEdge(0, 1, 4) 
graph.addEdge(0, 7, 8) 
graph.addEdge(1, 2, 8) 
graph.addEdge(1, 7, 11) 
graph.addEdge(2, 3, 7) 
graph.addEdge(2, 8, 2) 
graph.addEdge(2, 5, 4) 
graph.addEdge(3, 4, 9) 
graph.addEdge(3, 5, 14) 
graph.addEdge(4, 5, 10) 
graph.addEdge(5, 6, 2) 
graph.addEdge(6, 7, 1) 
graph.addEdge(6, 8, 6) 
graph.addEdge(7, 8, 7) 
graph.prim() 
