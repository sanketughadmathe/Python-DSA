class Node:
    def __init__(self, val=None):
        self.value = val
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    # Constructor for creating a new BST object with root node as the given value
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
            return True
        current = self.root
        while (True):
            if newNode.value == current.value:
                return False
            if newNode.value < current.value:
                if current.left_child == None:
                    current.left_child = newNode
                    return True
                current = current.left_child
            else:
                if current.right_child == None:
                    current.right_child = newNode
                    return True
                current = current.right_child

    def contains(self, value):
        current = self.root
        while (current != None):
            if value < current.value:
                current = current.left_child
            elif value > current.value:
                current = current.right_child
            else:  # found it!
                return True
        return False


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)


print('Root:', my_tree.root.value)
print('Root -> Left:', my_tree.root.left_child.value)
print('Root -> Right', my_tree.root.right_child.value)
