class Node:
    def __init__(self, val=None):
        self.value = val
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    # push an element to the end of queue (enqueue operation). O(1) time complexity
    def enqueue(self, value):
        newNode = Node(value)
        # if not self.is_empty():
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        return True

    # Print Queue
    def printQueue(self):
        current = self.first
        while current is not None:
            print(current.value)
            current = current.next

    # pop from front and remove first node in linked list which has been added last.(dequeue operation),O(n) worst case scenario as we need to traverse entire LinkedList for finding previousNode before removing it

    # Print the Queue by top

    def print_queue_head(self, first):
        while (first != None):
            print(str(first.value) + " -> ", end="")
            first = first.next

    def dequeue(self):
        """Remove and returns first node from Queue"""
        tempNode = self.first
        if self.length == 0:
            return None

        if self.length == 1:
            self.first = None
            self.last = None

        else:
            self.first = self.first.next
            tempNode.next = None
        self.length -= 1
        return tempNode


my_queue = Queue()
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(99)
my_queue.enqueue(300)
my_queue.printQueue()

print('='*10)
my_queue.dequeue()
my_queue.printQueue()
