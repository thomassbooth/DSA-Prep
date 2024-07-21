from collections import deque

def bfs(graph: list[list], source, searchNode):

    #havent seen anything yet
    seen = [False for i in range(len(graph))]
    previous = [-1 for i in range(len(graph))]

    seen[source] = True
    queue = deque([source])

    while len(queue) > 0:
        #grab first in the queue
        current = queue.popleft()
        
        #we found our value
        if current == searchNode: return True

        #grab our array of adjacencies (edges to other nodes)
        connectedNodes = graph[current]
        for i in range(len(connectedNodes)):
            #if theres no edge for node i (weight = 0)
            if connectedNodes[i] == 0: continue
            #if we have already seen this node
            if seen[i]: continue

            #mark this node as seen
            seen[i] = True
            #store this node as the previous
            previous[i] = current
            #add this node to the queue
            queue.append(i)

        
        current = searchNode
        path = []

        #if we have found the node
    while previous[current] != -1:
        path.append(current)
        current = previous[current]

    if len(path):
        
        return [source] + path.reverse()

    


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ]
    source = 0
    searchNode = 2
    path = bfs(graph, source, searchNode)
    print(f"Path from {source} to {searchNode}: {path}")