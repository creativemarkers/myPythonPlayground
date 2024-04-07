class GraphNode():
    def __init__(self,name) -> None:
        self.name = name
        self.data = None

    def __repr__(self) -> str:
        return f"{self.name}"
    
class DirectedGraph():

    def __init__(self):
        self.adjacencyList = {}

    def addNode(self,node):
        if node not in self.adjacencyList:
            print(f"adding {node}, to adjancy list keys...")
            self.adjacencyList[node] = []
        else:
            print(f"{node}, already in graph")

    def addEdge(self,parentNode:object, edgeList:list):
        if parentNode in self.adjacencyList:
            for node in edgeList:
                if node not in self.adjacencyList[parentNode]:
                    print(f"adding {node} to {parentNode}'s edges")
                    self.adjacencyList[parentNode].append(node)
                else:
                    print(f"{node}, already in {parentNode} adjacency list.")
        else:
            print(f"{parentNode} not in graph, please add it to graph first.")

    def depthFirstTraversal(self, startNode):
        #use a stack
        visited = set()
        stack = [startNode]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                neighbors = self.adjacencyList[current]
            print(current)
            for edge in reversed(neighbors):
                if edge not in visited:
                    stack.append(edge)
        return None


def main():

    dGraph = DirectedGraph()

    alphabet = ["a","b","c","d","e","f"]
    nodeList = []
    
    for letter in alphabet:
        node = GraphNode(name=letter)
        nodeList.append(node)

    for node in nodeList:
        dGraph.addNode(node)

    aEdges = [nodeList[1],nodeList[2]]
    bEdges = [nodeList[3]]
    cEdges = [nodeList[4]]
    eEdges = [nodeList[1]]
    fEdges = [nodeList[3]]
    #adding edges to a
    dGraph.addEdge(nodeList[0],aEdges)
    #adding edge to b
    dGraph.addEdge(nodeList[1],bEdges)
    #adding edge to c
    dGraph.addEdge(nodeList[2],cEdges)
    #adding edge to e
    dGraph.addEdge(nodeList[4],eEdges)
    #adding edge to f
    dGraph.addEdge(nodeList[5],fEdges)

    #dGraph.depthFirstTraversal(nodeList[0])


    print(dGraph.adjacencyList)







if __name__ == "__main__":
    main()