class Node:
    def __init__(self, val=None):
        self.value = val
        self.next = None


class Stack:
    # Constructor to initialize the stack object with a top node and its value as null
    def __init__(self) -> None:
        self.top = None
        self.height = 0

    # Function to push an element onto the top of the stack
    def push(self, val):
        # Create a newNode instance for pushing into the stack
        newNode = Node(val)
        if (self.height == 0):
            self.top = newNode    # If there is no existing nodes in the list then set this
        else:
            newNode.next = self.top     # Set next pointer of newnode to point at current
            self.top = newNode          # Move the previous first node on top to second position
        self.height += 1

    # Print the Stack
    def print_stack(self):
        current = self.top
        while (current != None):
            print("\t" + str(current.value) + " -> ", end="")
            current = current.next
        print("None")

    # Print the Stack by top
    def print_stack_head(self, top):
        while (top != None):
            print(str(top.value) + " -> ", end="")
            top = top.next

    # Function to pop an element onto the top of the stack
    def pop(self):
        if self.height == 0:
            return None

        tempNode = self.top   # Store reference to head before deleting it
        self.top = tempNode.next
        tempNode.next = None
        self.height -= 1
        return tempNode


my_stack = Stack()
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(99)
my_stack.push(300)
my_stack.print_stack()

print('='*10)
my_stack.pop()
my_stack.print_stack()
