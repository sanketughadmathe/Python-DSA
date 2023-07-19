class Node():
    def __init__(self, val) -> None:
        self.value = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    # Print List
    def printList(self):
        """
        Prints the elements of the doubly linked list from head to tail.
        """
        temp_node = self.head
        while temp_node is not None:
            print(str(temp_node.value) + " <-> ", end="")
            temp_node = temp_node.next

    # Print List via head
    def print_ll_head(self, head):
        """
        Prints the elements of the doubly linked list given a specific head node.
        """
        while head is not None:
            print(str(head.value) + " -> ", end="")
            head = head.next

    # Append
    def append(self, value):
        """
        Appends a new node with the given value to the end of the doubly linked list.
        """
        newNode = Node(value)
        if not self.head and not self.tail:  # Empty list
            self.head = newNode
            self.tail = newNode
        else:
            currentTailNode = self.tail
            currentTailNode.next = newNode
            newNode.prev = currentTailNode
            self.tail = newNode
        self.length += 1

    # Pop
    def pop(self):
        """
        Removes the last node from the doubly linked list.
        """
        currentNodeToRemove = self.tail
        if self.length == 0:  # Empty list
            return None
        if self.length == 1:  # Only one node in the list
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            currentNodeToRemove.prev = None
        self.length -= 1

    # Prepend
    def prepend(self, value):
        """
        Prepends a new node with the given value to the beginning of the doubly linked list.
        """
        newNode = Node(value)
        if self.length == 0:  # Empty list
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    # Pop first
    def popFirst(self):
        """
        Removes the first node from the doubly linked list.
        """
        if self.length == 0:  # Empty list
            return None
        if self.length == 1:  # Only one node in the list
            self.head = None
            self.tail = None
        else:
            tempNode = self.head
            self.head = self.head.next
            self.head.prev = None
            tempNode.next = None
        self.length -= 1

    # Get
    def get(self, index):
        """
        Retrieves the node at the given index in the doubly linked list.
        """
        if 0 < index >= self.length:
            raise IndexError("Index out of range")
            return None
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node

    # Set
    def set(self, index, newValue):
        """
        Sets the value of the node at the given index in the doubly linked list.
        """
        nodeToChange = self.get(index)
        if nodeToChange:
            nodeToChange.value = newValue
            return True
        return False

    # Insert
    def insert(self, index, newValue):
        """
        Inserts a new node with the given value at the specified index in the doubly linked list.
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(newValue)
        if index == self.length:
            return self.append(newValue)
        newNode = Node(newValue)
        temp = self.get(index-1)
        newNode.next = temp.next
        newNode.prev = temp
        temp.next = newNode
        self.length += 1

    # Remove by index
    def remove(self, index):
        """
        Removes the node at the specified index from the doubly linked list.
        """
        if 0 < index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop()
        currentNodeToRemove = self.get(index)
        prevNode = currentNodeToRemove.prev
        nextNode = currentNodeToRemove.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        currentNodeToRemove.prev = None
        currentNodeToRemove.next = None
        self.length -= 1
