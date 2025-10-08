class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value, position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        index = 0
        while index < position-1:
            current = current.next
            index += 1
            if current is None:
                raise IndexError("Position out of range")
        new_node.next = current.next
        current.next = new_node

    def update(self,position,new_value):
        current = self.head
        index = 0
        while index < position:
            current = current.next
            index += 1
            if current is None:
                raise IndexError("Position out of range")
        current.data = new_value

    def remove(self,position):
        if self.head is None:
            raise IndexError("List is empty")
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        index = 0
        while index < position-1:
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
            index += 1
        current.next = current.next.next

    def display(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        print(" -> ".join(result))

ll = LinkedList()
ll.insert(10,0)
ll.insert(20,1)
ll.insert(5,1)
ll.insert(6,1)
ll.insert(7,1)
ll.insert(8,5)
ll.display()


ll.display()

ll.remove(5)
ll.display()