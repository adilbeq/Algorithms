class Node:
        def __init__(self, data = None):
                self.data = data
                self.next = None
class LinkedList:
        def __init__(self):
                self.head = None

        def printL(self):
                p = self.head
                while p is not None:
                        print(p.data)
                        p = p.next
        def reverse(head):
                new_head = None
                while head:
                        head.next, head, new_head = new_head, head.next, head
                return new_head


list1 = LinkedList()
list1.head = Node(3)
o2 = Node(4)
o3 = Node(5)
o4 = Node(6)
o5 = Node(7)
list1.head.next = o2
o2.next = o3
o3.next = o4
o4.next = o5

list1.reverse()

list1.printL()
