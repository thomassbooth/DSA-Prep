from collections import deque

class Edge:
    def __init__(self, to):
        self.to = to

def dfs(graph: list[list[Edge]], currNode: int, searchNode: int, seen: list[bool], path: list[int]) -> bool:
    # Base case: we've already visited this node
    if seen[currNode]:
        return False

    # Mark this node as seen
    seen[currNode] = True

    # Add this node to the path as we are now visiting it
    path.append(currNode)
    if currNode == searchNode:
        return True

    # Recurse
    edgeList = graph[currNode]
    for edge in edgeList:
        if dfs(graph, edge.to, searchNode, seen, path):
            return True

    # If searchNode not found, backtrack
    path.pop()

    return False

if __name__ == "__main__":
    # Example graph represented as an adjacency list with Edge objects
    graph = [
        [Edge(1), Edge(2)],  # Node 0 is connected to Node 1 and Node 2
        [Edge(0), Edge(3)],  # Node 1 is connected to Node 0 and Node 3
        [Edge(0), Edge(3)],  # Node 2 is connected to Node 0 and Node 3
        [Edge(1), Edge(2)]   # Node 3 is connected to Node 1 and Node 2
    ]
    source = 0
    searchNode = 3

    seen = [False for _ in range(len(graph))]
    path = []

    if dfs(graph, source, searchNode, seen, path):
        print(f"Path from {source} to {searchNode}: {path}")
    else:
        print(f"No path found from {source} to {searchNode}")
