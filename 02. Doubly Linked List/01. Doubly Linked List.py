class Node():
    def __init__(self, val) -> None:
        self.value = val
        self.next = None
        self.prev = None


class doublyLinkedlist:
    def __init__(self) -> None:
        # new_node = Node(value)
        self.head = None
        self.tail = None
        self.length = 0

    # Print List
    def printList(self):
        temp_node = self.head
        while (temp_node != None):
            # print ("% d" %temp_node.value)
            print(str(temp_node.value) + " <-> ", end="")
            temp_node = temp_node.next

    # Print List via head
    def print_ll_head(self, head):
        while head is not None:
            print(str(head.value) + " -> ", end="")
            head = head.next

    # Append
    def append(self, value):
        newNode = Node(value)
        if not self.head and not self.tail:
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

        currentNodeToRemove = self.tail
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            currentNodeToRemove.prev = None
            # removedValue = currentNodeToRemove.value
            # del currentNodeToRemove
            # print("Removed Value:", removedValue)

        self.length -= 1

    # Prepend
    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return True

    # Pop first
    def popFirst(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            tempNode = self.head
            self.head = self.head.next
            self.head.prev = None
            tempNode.next = None
            # deletedValue = tempNode.value
            # del tempNode
            # print('Deleted:',deletedValue )
        self.length -= 1

    # Get
    def get(self, index):
        # if index < 0 or index >= self.length:
        if 0 < index >= self.length:
            raise IndexError("Index out of range")
            return None
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        # print(current_node.value)
        return current_node

    # Set
    def set(self, index, newValue):
        nodeToChange = self.get(index)
        if nodeToChange:
            nodeToChange.value = newValue
            # print (f"Old value at {index} is: {oldValue}, New Value is : {newValue}")
            return True
        return False

    # Insert
    def insert(self, index, newValue):
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

        # temp = self.tail
        # newNode.nex

    # Remove by index
    def remove(self, index):
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
        # del currentNodeToRemove
        currentNodeToRemove.prev = None
        currentNodeToRemove.next = None
        self.length -= 1


l = doublyLinkedlist()
l.append(8)
l.append(9)
l.append(10)
l.append(11)

l.printList()
