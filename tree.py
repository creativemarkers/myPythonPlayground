class TreeNode():
    name = None
    data = None
    parent = None
    children = []
    def __init__(self, name) -> None:
        self.name = name
        pass


#basic tree structure for practice
class Tree():
    root = None
    maxDepth = 0
    current = None

    def __init__(self, treeNode:object) -> None:
        if self.root == None:
            self.root = treeNode
            self.current = self.root

    def printCurrentChildren(self):
        for child in self.current.children:
            print(child.name)

    def addChildToCurrent(self, leaf:object) -> None:
        leaf.parent = self.current
        self.current.children = leaf


    def findNode(self, nodeName) -> object:
        #make sure to change current to desired node to start search
        #my recursion is fucked
        while len(self.current.children) != 0:
            if self.current.name == nodeName:
                print("Found:", nodeName)
                return self.current.name
            else:
                if len(self.current.children) == 0:
                    return None
                else:
                    for child in self.current.children:
                        self.current = child
                        self.findNode(nodeName)
            re

    def insertNode(self, child, parentName = None):

        if parentName == None:
            parentName = self.root.name

        self.findNode(parentName)

        self.addChildToCurrent(child)

    def traverseTree(self):

        if len(self.current.children) == 0:
            return self.current
        else:
            for child in self.current.children:
                self.current = child
                self.traverseTree()

    def printTree(self):        

        print(self.current.name)
        if len(self.current.children) == 0:
            return None
        else:
            for child in self.current.children:
                self.current = child
                self.printTree()
        

        

    


def main():

    tree = Tree(TreeNode("base"))
    child1Name = "Depth:1,Child:1"
    tree.addChildToCurrent(TreeNode(child1Name))
    #tree.printCurrentChildren()
    tree.current = tree.root

    tree.insertNode(TreeNode("Depth:2,Child:1"),child1Name)
    tree.findNode("Depth:2,Child:1")
    #tree.printTree()


if __name__ == "__main__":
    main()