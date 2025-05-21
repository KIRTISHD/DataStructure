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

    # This will print the elements present in Linked list
    def print(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

    # This will append the element at the beginning of the list
    def append_at_begin(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        newnode.next = self.head
        self.head = newnode

    # This will append the elements at a given location starting with 0(index)
    def append_at_index(self, data, index):

        if index < 0:
            raise IndexError("Invalid index")
            return

        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        
        if index == 0:
            self.append_at_begin(data)
            return
        
        counter = 0
        current = self.head
        while current is not None and counter < index-1:
            current = current.next
            counter += 1

        if current is None:
            raise IndexError("Index is greater than no of elements")
        
        newnode.next = current.next
        current.next = newnode


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(4)
    ll.append(44)
    ll.append(444)
    ll.append_at_index(43, 4)
    ll.print()