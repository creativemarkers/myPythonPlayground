def buildGraph(edges):
    graph = {}

    for edge in edges:
        a,b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph

def hasPath(graph, src, dest, visited=set()):

    if src == dest:
        return True
    if src in visited:
        return False 
    
    visited.add(src)
    
    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dest, visited) == True:
            return True
        
    return False


def undirectedPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)

    return hasPath(graph, nodeA, nodeB)

edges = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n']
]

result = undirectedPath(edges, 'j', 'm')

print(result)