class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Print List
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Append
    def append(self, value) -> None:
        new_node = Node(value)
        if self.head == None:  # empty list case
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # Pop
    def pop(self) -> None:
        if self.length == 0:
            return None

        pre = temp = self.head

        while (temp.next != None):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    # Prepend
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    # POP First
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if (self.length == 0):
            self.tail = None
        return temp

    # Get
    def get(self, index):
        if index < 0 or index >= self.length:
            # raise IndexError("Index out of range")
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    # Set
    def set_value(self, index, value):
        temp = self.get(index)
        # if not temp is None:
        if temp:
            temp.value = value
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
        new_node = Node(newValue)
        temp = self.get(index)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    # Reserse
    def reverse(self):
        """Function to Reverse the Linked list"""
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_linked_list = Linkedlist()
