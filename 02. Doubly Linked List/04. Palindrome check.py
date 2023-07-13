from DoublyLinkedList import doublyLinkedlist

my_doulby_linked_list = doublyLinkedlist()

my_doulby_linked_list.append(8)
my_doulby_linked_list.append(9)
my_doulby_linked_list.append(10)
my_doulby_linked_list.append(11)

print('\n')
my_doulby_linked_list.printList()
print('\n')


def reverse(self):
    temp = self.head
    while temp != None:
        # swap the prev and next pointers of node points
        temp.prev, temp.next = temp.next, temp.prev

        # move to the next node
        temp = temp.prev

    # swap the head and tail pointers
    self.head, self.tail = self.tail, self.head


reverse(my_doulby_linked_list)
my_doulby_linked_list.printList()
print('\n')
