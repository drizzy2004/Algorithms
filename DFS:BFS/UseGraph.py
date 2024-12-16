
import Graph

ga1 = Graph.GraphAlgorithms('graph-1.txt')
ga2 = Graph.GraphAlgorithms('graph-2.txt')
ga3 = Graph.GraphAlgorithms('graph-3.txt')
ga4 = Graph.GraphAlgorithms('graph-4.txt')

# Example
print("DFS recursive:")
print(ga1.DFS('recursive'))

print("DFS stack:")
print(ga1.DFS('stack'))

print("BFS:")
print(ga1.BFS())

print("hasCycle?")
print(ga1.hasCycle())

print("Shortest path from a to f:")
print(ga1.shortestpath('a','f'))

