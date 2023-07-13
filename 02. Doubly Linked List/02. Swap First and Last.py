from DoublyLinkedList import doublyLinkedlist

my_doulby_linked_list = doublyLinkedlist()

my_doulby_linked_list.append(8)
my_doulby_linked_list.append(9)
my_doulby_linked_list.append(10)
my_doulby_linked_list.append(11)

print('\n')
my_doulby_linked_list.printList()
print('\n')


def swap_first_last(self):
    """Swap the first and last elements of a list."""
    if (self.head == None and self.head == self.tail):
        return
    self.head.value, self.tail.value = self.tail.value, self.head.value


swap_first_last(my_doulby_linked_list)
my_doulby_linked_list.printList()
print('\n')
