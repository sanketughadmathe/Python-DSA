from LinkedList import Linkedlist


def find_kth_from_end(ll, k):
    """Find the K-th element from end of a linked list"""
    fast = slow = ll.head

    for _ in range(k):
        if fast == None:
            return None
        else:
            fast = fast.next

    while fast != None:
        slow = slow.next
        fast = fast.next
    return slow


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

print('\n')

my_linked_list.print_list()
print('\n')

my_linked_list.print_ll_head(find_kth_from_end(my_linked_list, 4))
print('\n')

my_linked_list.print_ll_head(find_kth_from_end(my_linked_list, 7))
print('\n')
