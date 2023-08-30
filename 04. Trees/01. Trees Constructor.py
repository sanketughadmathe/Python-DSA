class Node:
    def __init__(self, val=None):
        self.value = val
        self.left_child = None
        self.right_child = None


class BinartSearchTree:
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

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left_child = self.__r_insert(
                current_node.left_child, value)
        if value > current_node.value:
            current_node.right_child = self.__r_insert(
                current_node.right_child, value)
        return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)


my_tree = BinartSearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

# print(my_tree.root.left_child.value)
# print(my_tree.root.right_child.value)

# print('BST Contains 17: ')
# print(my_tree.contains(17))

# print('\nBST Contains 27: ')
# print(my_tree.contains(2))


print('Root:', my_tree.root.value)
print('Root -> Left:', my_tree.root.left_child.value)
print('Root -> Right', my_tree.root.right_child.value)
