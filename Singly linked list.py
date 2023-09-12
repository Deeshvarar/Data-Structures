#singly linked list
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        
class linked:
    def __init__(self):
        self.head = None
        
    def show(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
            
    def add(self,new):
        newnode = Node(new)
        newnode.next = self.head
        self.head = newnode
            
link = linked()

e1 = Node("Ironman")
link.head = e1

e2 = Node("Batman")
link.head.next = e2

e3 = Node("Superman")
e2.next = e3

e4 = Node("Thor")
e3.next = e4


link.add("Hulk")
link.add("Flash")
link.add("Black Panther")


link.show()
