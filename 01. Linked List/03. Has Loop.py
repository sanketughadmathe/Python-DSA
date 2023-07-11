from LinkedList import Linkedlist


def has_loop(self):
    """Check if the linked list contains a loop."""

    # pointer to traverse with two steps at most (slow and fast)
    slow = self.head
    fast = self.head

    while (fast != None and fast.next != None):
        slow = slow.next  # move one step forward in both pointers
        fast = fast.next.next
        # check for loops by comparing current positions of slow & fast ptrs
        if slow == fast:
            return True
    return False
