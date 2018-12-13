class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None;
    def get_data(node):
        return node.data
    

list1 = LinkedList()
list1.head = Node(3)
node1 = Node(4)
node2 = Node(5)
node3 = Node(6)

list1.head.next = node1
node1.next = node2
node2.next = node3

list1.get_data(node1)
