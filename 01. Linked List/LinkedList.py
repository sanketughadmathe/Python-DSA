class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    # Print List
    def print_list(self):
        """
        Prints the values of all nodes in the linked list.
        """
        temp = self.head
        while temp is not None:
            # print(temp.value)
            print(str(temp.value) + " -> ", end="")
            temp = temp.next

    # Print List via head
    def print_ll_head(self, head):
        """
        Prints the values of all nodes in the linked list starting from the given head node.
        """
        while head is not None:
            print(str(head.value) + " -> ", end="")
            head = head.next

    # Append
    def append(self, value) -> None:
        """
        Appends a new node with the given value to the end of the linked list.
        """
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
        """
        Removes and returns the last node from the linked list.
        """
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
        """
        Adds a new node with the given value at the beginning of the linked list.
        """
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
        """
        Removes and returns the first node from the linked list.
        """
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
        """
        Returns the node at the specified index in the linked list.
        If the index is out of range, returns None.
        """
        if index < 0 or index >= self.length:
            # raise IndexError("Index out of range")
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    # Set
    def set_value(self, index, value):
        """
        Updates the value of the node at the specified index in the linked list.
        Returns True if the update is successful, False otherwise.
        """
        temp = self.get(index)
        # if not temp is None:
        if temp:
            temp.value = value
            return True
        return False

    # Insert
    def insert(self, index, newValue):
        """
        Inserts a new node with the given value at the specified index in the linked list.
        Returns True if the insertion is successful, False otherwise.
        """
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

    # Reverse
    def reverse(self):
        """
        Reverses the order of nodes in the linked list.
        """
        current = self.head
        self.head = self.tail
        self.tail = current

        # after = current.next
        # before = None

        for _ in range(self.length):
            after = current.next
            current.next = before
            before = current
            current = after
