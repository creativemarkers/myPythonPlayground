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
    shortestNodes = None
    memo = []
    visited = []

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

    def shortestPathFromCurrent(self, end, current = None, nodesVisitedSofar = None, distancedTraveledSoFar = 0):
        if current == None:
            current = self.current
        print(current)
        if current == end:
            return nodesVisitedSofar, distancedTraveledSoFar
        
        if nodesVisitedSofar == None:
            print("converted")
            nodesVisitedSofar = [current]
        else:
            nodesVisitedSofar.append(current)

        for node, dist in current.neighbors.items():
            distancedTraveledSoFar += dist
            nodesVisitedSofar, distancedTraveledSoFar = self.shortestPathFromCurrent(node,nodesVisitedSofar,distancedTraveledSoFar)
            if self.shortestPath == None or distancedTraveledSoFar < self.shortestPath:
                self.shortestPath = distancedTraveledSoFar
                self.shortestNodes = nodesVisitedSofar
        
        return None, None
    
    def distanceTo(self,current,end,distanceTraveled = 0):
        print("current:", current)
        if current == end:
            return distanceTraveled
        
        self.visited.append(current)
        
        for neighbor,dist in current.neighbors.items():
            print(neighbor,dist)
            if neighbor not in self.visited:
                distanceTraveled += dist
                result = self.distanceTo(neighbor,end,distanceTraveled)

                print("result", result)
                if result != None:
                    if self.shortestPath == None:
                        self.shortestPath = result
                    elif result < self.shortestPath:
                        self.shortestPath = result
            
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
    # graph.shortestPathFromCurrent(nodeD)
    # print(graph.shortestNodes)

    #print(graph.nodes[0].neighbors[nodeB])

    graph.distanceTo(nodeA,nodeD)

    print(graph.shortestPath)



if __name__ == "__main__":
    main()
