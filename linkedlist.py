class LinkedNode():
    prev = None
    index = None
    data = None
    next = None
    def __init__(self, data):
        self.data = data

class LinkedList(LinkedNode):
    
    head = None
    tail = None
    size = 0
    def __init__(self, node):
        if self.head == None:
            self.head = node
            self.head.index = 0
            if self.head.next != None:
                self.setTail()
            else:
                self.tail = node
                self.tail.index = 0
                self.size = 1

    def setTail(self):
        current = self.head
        while current:
            if current.next == None:
                self.tail = current
                break
    
    def printList(self):

        current = self.head
        
        while current:
            print("Node data:", current.data)
            # print("Node index:",current.index)
            # if current.prev != None:
            #     print("Previous Node index:", current.prev.index) 
            # else:
            #     print("Current Head")
            current = current.next

    def append(self, node):

        prevBuffer = self.tail
        indexbuffer = self.tail.index
        self.tail.next = node

        self.tail = node
        self.tail.index = indexbuffer + 1
        self.tail.prev = prevBuffer

    def prepend(self, node):
        
        self.head.prev = node
        nextBuffer = self.head
        self.head = node
        self.head.next = nextBuffer
        self.head.index = 0
        self.updateIndices()
        
    def updateIndices(self):

        current = self.head.next

        while current: 
            current.index = current.prev.index + 1
            # print("Updated Data:", current.data)
            # print("Updated Index:", current.index)
            current = current.next
        # print("=============")    
            
    def insert(self,index, node):
        current = self.head
        while current:

            if current.index == index:

                node.prev = current.prev
                node.next = current
                node.index = current.index

                node.prev.next = node
                current.prev = node
                current.index = node.index + 1

                self.updateIndices()
                break
            else:
                current = current.next
                
    def updateNodeData(self, index, data):

        current = self.head

        while current:

            if current.index == index:
                current.data = data
                break
            else:
                current = current.next

    def removeHead(self):
      self.head.next.prev = None
      self.head = self.head.next
      self.head.index = 0
      self.updateIndices()

    def removeTail(self):
        self.tail = self.tail.prev
        self.tail.next = None

    def getSize(self):
        self.size = self.tail.index + 1
        return print(self.size)
    
    def removeNode(self,index):

        if index == self.head.index or index == self.tail.index:
            print("use the appropriate function to remove head or tail")
            raise IndexError
        else:
            current = self.head.next

            while current:
                if current.index == index:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.updateIndices()
                    break
                else:
                    current = current.next

node = LinkedNode("head")

ll = LinkedList(node)

ll.append(LinkedNode("one"))
ll.append(LinkedNode("bad word"))
ll.prepend(LinkedNode("newHead"))
ll.updateNodeData(1,"old head")
ll.insert(2, LinkedNode("inserted here"))
ll.removeHead()
ll.removeTail()
ll.removeNode(1)
ll.printList()
ll.getSize()