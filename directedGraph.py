class GraphNode():
    
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.data = None

    def __repr__(self) -> str:
        return f"Object: {self.name}"
    
    def addNeighbor(self,node,distance):
        print(f"adding {node}, to {self.name}")
        self.neighbors[node] = distance

class Graph():

    nodes = []
    current = None
    shortestPath = None
    memo = []

    def __init__(self):
        
        # self.current = node
        # self.nodes.append[node]
        pass

    def connectNewNeighbors(self, node1, node2, distance):

        if node1 not in self.nodes:
            self.nodes.append(node1)
        if node2 not in self.nodes:
            self.nodes.append(node2)

        node1.addNeighbor(node2, distance)
        node2.addNeighbor(node1, distance)

    def changeCurrent(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

        self.current = node

    def shortestPathFromCurrent(self, end):
        tempShortestNode = None
        tempShortestDist = None
        for node, dist in self.current.neighbors.items():
            print(i, j)
            if tempShortestDist == None or dist < 
            
def main():
    graph = Graph()
    nodeA = GraphNode("node A")
    nodeB = GraphNode("node B")
    nodeC = GraphNode("node C")
    nodeD = GraphNode("node D")
    graph.connectNewNeighbors(nodeA,nodeB,5)
    graph.connectNewNeighbors(nodeB,nodeC,7)
    graph.connectNewNeighbors(nodeC,nodeA,2)
    graph.connectNewNeighbors(nodeB,nodeD,4)
    graph.connectNewNeighbors(nodeC,nodeD,3)
    graph.changeCurrent(nodeA)
    graph.shortestPathFromCurrent(nodeD)



if __name__ == "__main__":
    main()
