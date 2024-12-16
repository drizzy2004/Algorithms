
'''
Demonstration of some simple graph algorithms.
    
@author: Jingsai Liang
'''

import sys

class GraphAlgorithms:
    
    '''
    Reads in the specified input file containing
    adjacent edges in a graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''
    def __init__(self, fileName): 
    
        graphFile = open(fileName)

        '''
        create an initially empty dictionary representing
        an adjacency list of the graph
        '''
        self.adjacencyList = { }
    
        '''
        collection of vertices in the graph (there may be duplicates)
        '''
        self.vertices = [ ]

        for line in graphFile:
            '''
            Get the two vertices
        
            Python lets us assign two variables with one
            assignment statement.
            '''
            (firstVertex, secondVertex) = line.split()
        
            '''
            Add the two vertices to the list of vertices
            At this point, duplicates are ok as later
            operations will retrieve the set of vertices.
            '''
            self.vertices.append(firstVertex)
            self.vertices.append(secondVertex)

            '''
            Check if the first vertex is in the adjacency list.
            If not, add it to the adjacency list.
            '''
            if firstVertex not in self.adjacencyList:
                self.adjacencyList[firstVertex] = [ ]

            '''
            Add the second vertex to the adjacency list of the first vertex.
            '''
            self.adjacencyList[firstVertex].append(secondVertex)
        
        # creates and sort a set of vertices (removes duplicates)
        self.vertices = list(set(self.vertices))
        self.vertices.sort()

        # sort adjacency list for each vertex
        for vertex in self.adjacencyList:
            self.adjacencyList[vertex].sort()

    '''
    Begins the DFS algorithm.
    '''
    def DFSInit(self):
        # initially all vertices are considered unknown
        self.unVisitedVertices = list(set(self.vertices))
        # initialize path as an empty string
        self.path = ""

    '''
    depth-first traversal of specified graph
    '''
    def DFS(self, method):
        self.DFSInit()
        if method == 'recursive':
            # Your code goes here:
            for vertex in self.vertices:
                if vertex not in self.path:
                    self.DFS_recur(vertex)

            return self.path
        elif method == 'stack':
            # Your code goes here:
            for vertex in self.vertices:
                if vertex not in self.path:
                    self.DFS_stack(vertex)

            return self.path


    def DFS_recur(self,vertex):
        # Your code goes here:
        self.path = self.path + vertex

        for v in self.adjacencyList[vertex]:
            if v not in self.path:
                self.DFS_recur(v)

            
                
    def DFS_stack(self, vertex):
        stack=[]
        stack.append(vertex)
        while stack:
            vertex = stack.pop()
            if vertex not in self.path:
                self.path += vertex
                for v in self.adjacencyList[vertex]:
                    if v not in self.path:
                        stack.append(v)



    def BFSInit(self):
        # initially all vertices are considered unknown
        self.unVisitedVertices = list(set(self.vertices))
        # initialize path as an empty string
        self.path = ""
        

    def BFS(self):
        self.BFSInit()

        for vertex in self.vertices:
            if vertex not in self.path:
                self.BFS_queue(vertex)

        return self.path


    def BFS_queue(self, vertex):
        queue = []

        self.path += vertex
        queue.append(vertex)
        while queue:
            vertex = queue.pop(0)
            for v in self.adjacencyList[vertex]:
                if v not in self.path:
                    self.path += v
                    queue.append(v)


    def hasCycle(self):

        immediateParent = {}
        stack = []
        visited = set()

        for vertex in self.vertices:
            if vertex not in visited:
                stack.append([vertex, None])

            while stack:
                vertex, parent = stack.pop()
                if vertex in visited:
                    if immediateParent[vertex] != parent:
                        return True

                else:
                    visited.add(vertex)
                    immediateParent[vertex] = parent


                    for v in self.adjacencyList[vertex]:
                        if v != parent:
                            stack.append([v, vertex])
        return False


                    
    # Work on this function for at most 10 extra points
    def shortestpath(self, p, q):
        if p not in self.adjacencyList or q not in self.adjacencyList:
            return None

        # I decided to use BFS since it is the most optimal, it checks per level
        queue = [[p]]
        visited = set()
        level = {p: 0}

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node == q:
                return len(path) - 1

            if node not in visited:
                visited.add(node)

                for vertex in self.adjacencyList[node]:
                    if vertex not in visited and vertex not in level:
                        new_path = path + [vertex]
                        queue.append(new_path)
                        level[vertex] = level[node] + 1

        return None


  
                
        

        

