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

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left_child, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right_child, value)

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

    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left_child = self.__delete_node(
                current_node.left_child, value)
        elif value > current_node.value:
            current_node.right_child = self.__delete_node(
                current_node.right_child, value)
        else:
            if current_node.left_child == None and current_node.right_child == None:
                return None
            elif current_node.left_child == None:
                current_node = current_node.right_child
            elif current_node.right_child == None:
                current_node = current_node.left_child
            else:
                sub_tree_main = self.min_value(current_node.right_child)
                current_node.value = sub_tree_main
                current_node.right_child = self.__delete_node(
                    current_node.right_child, sub_tree_main)

        return current_node

    def delete_node(self, vaule):
        self.__delete_node(self.root, vaule)

    # def __delete_node(self, current_node, value):
    #     if current_node == None:
    #         return None
    #     if value < current_node.value:
    #         current_node.left_child = self.__delete_node(
    #             current_node.left_child, value)
    #     elif value > current_node.value:
    #         current_node.right_child = self.__delete_node(
    #             current_node.right_child, value)
    #     else:
    #         if current_node.left_child == None and current_node.right_child == None:
    #             return None
    #         elif current_node.left_child == None:
    #             current_node = current_node.right_child
    #         elif current_node.right_child == None:
    #             current_node = current_node.left_child
    #         else:
    #             sub_tree_min = self.min_value(current_node.right_child)
    #             current_node.value = sub_tree_min
    #             current_node.right_child = self.__delete_node(
    #                 current_node.right_child, sub_tree_min)
    #     return current_node

    # def delete_node(self, value):
    #     self.__delete_node(self.root, value)

    def min_value(self, current_node):
        while current_node.left_child != None:
            current_node = current_node.left_child
        return current_node.value


my_tree = BinarySearchTree()
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

my_tree.delete_node(2)

# print(my_tree.min_value(my_tree.root))
# print(my_tree.min_value(my_tree.root.left_child))
# print(my_tree.min_value(my_tree.root.right_child))


print('Root:', my_tree.root.value)
print('Root -> Left:', my_tree.root.left_child.value)
print('Root -> Right:', my_tree.root.right_child)
