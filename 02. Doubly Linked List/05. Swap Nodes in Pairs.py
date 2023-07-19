from DoublyLinkedList import doublyLinkedlist, Node

my_doulby_linked_list = doublyLinkedlist()

my_doulby_linked_list = doublyLinkedlist()

my_doulby_linked_list.append(8)
my_doulby_linked_list.append(9)
my_doulby_linked_list.append(10)
my_doulby_linked_list.append(11)
my_doulby_linked_list.append(12)
my_doulby_linked_list.append(11)
my_doulby_linked_list.append(13)
my_doulby_linked_list.append(11)
my_doulby_linked_list.append(14)
my_doulby_linked_list.append(11)

print('\n')
my_doulby_linked_list.printList()
print('\n')


def swap_pairs(self):
    # Create a dummy node as the previous node of the head
    dummy = Node(0)
    dummy.next = self.head
    prev = dummy

    # Iterate through the linked list in pairs
    while self.head is not None and self.head.next is not None:
        # Get the two nodes to be swapped
        firstNode = self.head
        secondNode = self.head.next

        # Swap the nodes by adjusting the next pointers
        prev.next = secondNode
        firstNode.next = secondNode.next
        secondNode.next = firstNode

        # Adjust the prev and next pointers for the swapped nodes
        secondNode.prev = prev
        firstNode.prev = secondNode

        # Update the prev pointer to the first node of the next pair
        if firstNode.next is None:
            firstNode.next.prev = firstNode

        # Move the head pointer to the next pair
        self.head = firstNode.next
        prev = firstNode

    # Update the head pointer of the linked list
    self.head = dummy.next


swap_pairs(my_doulby_linked_list)
my_doulby_linked_list.printList()
print('\n')
