from LinkedList import Linkedlist


def remove_duplicates(self):
    """Remove duplicates from the linked list."""
    values = set()
    # keep track of last node with unique value seen so far.
    previoius = None
    current = self.head   # start at head of LinkedList
    while current:
        if current.value in values:
            previoius.next = current.next  # skip over duplicate nodes
        else:
            values.add(current.value)   # add new, non-duplicate value to set
            previoius = current         # update previous pointer for next iteration
        current = current.next        # move on to next node


my_linked_list = Linkedlist()
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(7)
my_linked_list.append(6)
my_linked_list.append(9)

my_linked_list.print_list()
print("\n")
print("="*50)
middle_node = remove_duplicates(my_linked_list)
my_linked_list.print_list()
