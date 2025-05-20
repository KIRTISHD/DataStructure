## This will contain only the singly Linked list implementation

# This class will act as a Node for LL and store the data for us
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# This class will contain all the functionalities we can perform in LL
class LinkedList:
    def __init__(self):
        self.head = None

    # This will append the data at the end of LL
    def append(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode

    def print(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next


ll = LinkedList()
ll.append(4)
ll.append(44)
ll.append(444)
ll.print()