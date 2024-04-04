from queue import Queue
import json

class TreeNode():
    name = None
    data = None
    parent = None
    
    def __init__(self, name) -> None:
        self.name = name
        self.children = []

    def toDict(self):
        if self.parent != None:
            nodeDict = {
                "name":self.name,
                "data":self.data,
                "parent":self.parent.name,
                "children":[child.toDict() for child in self.children]
            }
        else:
            nodeDict = {
                "name":self.name,
                "data":self.data,
                "parent":None,
                "children":[child.toDict() for child in self.children]
            }

        return nodeDict


#basic tree structure for practice
class Tree():
    root = None
    current = None
    depth = 0
    height = 0

    def __init__(self, treeNode:object) -> None:
        if self.root == None:
            self.root = treeNode
            self.current = self.root

    def printCurrentChildren(self):
        for child in self.current.children:
            print(child.name)

    def addChildToCurrent(self, leaf:object) -> None:
        leaf.parent = self.current
        self.current.children.append(leaf)
        # print("Appended", leaf.name, "to", self.current.name)


    def findNode(self, node, current = None) -> object:
        if self.current == node:
            return None
        
        if current == None:
            current = self.root
        if current == node:
            # print(f"{node.name}, found")
            self.current = current
            return
        elif len(current.children) == 0:
            return None
        else:
            for child in current.children:
                self.findNode(node, child)

    def findNodeDFS(self, target):
        #according to chat gpt nodes are given a visited variable instead of using an array to store the visited
        visited = []
        current = self.root

        while current:
            visited.append(current)
            if current == target:
                return current
            else:
                lastCurrent = current
                for child in current.children:
                    if child not in visited:
                        current = child
                        break
                if lastCurrent == current:
                    current = current.parent

    def gptDFS(self, target):
        #gpt suggested corrections to my dfs algorithm
        visited = set()
        stack = [self.root]

        while stack:
            current = stack.pop()
            if current.name == target.name:
                return current
            visited.add(current)
            for child in current.children:
                if child not in visited:
                    stack.append(child)
        return None
    

    def insertNode(self, parentNode: object, child:object):

        self.findNode(parentNode)

        self.addChildToCurrent(child)

    def traverseTree(self):

        if len(self.current.children) == 0:
            return self.current
        else:
            for child in self.current.children:
                self.current = child
                self.traverseTree()

    def printLevelOrderTraversal(self):        

        q = Queue()
        q.put(self.root)

        while not q.empty():
            levelSize = q.qsize()
            for _ in range(levelSize): 
                node = q.get()
                print(node.name, end = " ")
                for child in node.children:
                    q.put(child)
            print()

    def printRealFileStructure(self, desiredStart = None, indentation = 0):

        if desiredStart == None:
            start = self.root
        else:
            start = desiredStart

        if indentation == 0:
            print(start.name)
        else:
            print(" " * indentation + "└─" + start.name)

        indentation += 3

        if start.children:
            for child in start.children:
                self.printRealFileStructure(child, indentation)
        else:
            return None
        
    def deleteNode(self, desiredNode):

        self.findNode(desiredNode)

        if len(self.current.children) > 0:
            print(f"Unable to delete {desiredNode.name} since it has children")
        else:
            self.current = desiredNode.parent

            for i, child in enumerate(self.current.children):
                if child.name == desiredNode.name:
                    print("deleting child from parent")
                    self.current.children.pop(i)

    def getTreeDimensions(self, current = None):

        if current == None:
            current = self.root

        if len(current.children) == 0:
            return 1
        else:
            self.depth += 1
            for child in current.children:
                result = self.getTreeDimensions(child)
                if result != None:
                    self.height += result
        



def main():

    base = TreeNode("base")
    tree = Tree(base)
    node1 = TreeNode("node1")
    node2 = TreeNode("node2")
    node3 = TreeNode("node3")
    node4 = TreeNode("node4")
    node5 = TreeNode("node5")
    node6 = TreeNode("node6")
    node7 = TreeNode("node7")
    
    tree.insertNode(base,node1)
    tree.insertNode(base,node2)
    tree.insertNode(node1,node3)
    tree.insertNode(node1,node4)
    tree.insertNode(node2,node5)
    tree.insertNode(node2,node6)
    # tree.deleteNode(node2)
    # tree.deleteNode(node6)

    # tree.getTreeDimensions()
    # print(tree.depth)
    # print(tree.height)

    # rootDict = base.toDict()
    # print(rootDict)
    # jsonString = json.dumps(rootDict, indent=2)
    # with open("tree.json", "w") as jsonFile:
    #     jsonFile.write(jsonString)

    # result = tree.findNodeDFS(node6)
    # print(result)

    result = tree.gptDFS(node7)
    print(result)
    
    #tree.printCurrentChildren() 
    
    # tree.printLevelOrderTraversal()
    # tree.printFileStructure()
    # tree.printRealFileStructure()
    #tree.insertNode(node1,node2)
    #tree.findNode(node2)
    #tree.printTree()


if __name__ == "__main__":
    main()