from LinkedList import Node, Linkedlist


def find_middle_node(self):
    slow = self.head
    fast = self.head
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
    return slow


my_linked_list = Linkedlist()
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(7)

my_linked_list.print_list()
print("\n")
print("="*50)
middle_node = find_middle_node(my_linked_list)
my_linked_list.print_ll_head(middle_node)
