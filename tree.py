from queue import Queue

class TreeNode():
    name = None
    data = None
    parent = None
    
    def __init__(self, name) -> None:
        self.name = name
        self.children = []


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
        self.current.children.append(leaf)
        print("Appended", leaf.name, "to", self.current.name)


    def findNode(self, node, current = None) -> object:
        #make sure to change current to desired node to start search
        #my recursion is fucked
        if current == None:
            current = self.root
        if current == node:
            print(f"{node.name}, found")
            self.current = current
            return
        elif len(current.children) == 0:
            return None
        else:
            for child in current.children:
                self.findNode(node, child)

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
    
    def printFileStructure(self, desiredStart = None):

        if desiredStart != None:
            root = desiredStart
        else:
            root = self.root

        queue = Queue()
        queue.put((root, ""))  # Tuple containing node and its indentation string
        
        while not queue.empty():
            node, parent_indentation = queue.get()
            print(parent_indentation + "└─" + str(node.name))  # Add indentation and arrow
            
            # Enqueue children of the current node with incremented indentation
            for i, child in enumerate(node.children):
                child_indentation = parent_indentation + ("│  " if i < len(node.children) - 1 else "   ") + "└─"
                queue.put((child, child_indentation))

# Example usage

    


def main():

    base = TreeNode("base")
    tree = Tree(base)
    node1 = TreeNode("node1")
    node2 = TreeNode("node2")
    node3 = TreeNode("node3")
    node4 = TreeNode("node4")
    node5 = TreeNode("node5")
    node6 = TreeNode("node6")
    
    tree.insertNode(base,node1)
    tree.insertNode(base,node2)
    tree.insertNode(node1,node3)
    tree.insertNode(node1,node4)
    tree.insertNode(node2,node5)
    tree.insertNode(node2,node6)
    
    #tree.printCurrentChildren() 
    
    tree.printLevelOrderTraversal()
    tree.printFileStructure()

    #tree.insertNode(node1,node2)
    #tree.findNode(node2)
    #tree.printTree()


if __name__ == "__main__":
    main()