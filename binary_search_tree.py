from tree_node import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.node_count = 0

    def is_empty(self) -> bool:
        return self.size()

    def size(self) -> int:
        return self.node_count

    def add(self, data) -> bool:
        if self.contains(data):
            return False

        self.root = self.__add(self.root, data)
        self.node_count += 1
        return True

    def __add(self, node: TreeNode, data):
        if not node:
            node = TreeNode(None, None, data)
        else:
            if data < node.data:
                node.left = self.__add(node.left, data)
            else:
                node.right = self.__add(node.right, data)
        return node

    def contains(self, data) -> bool:
        return self.__contains(self.root, data)

    def __contains(self, node: TreeNode, data) -> bool:
        if not node:
            return False

        if data > node.data:
            self.__contains(node.right, data)
        else:
            self.__contains(node.left, data)

        return True

    def height(self) -> int:
        return self.__height(self.root)

    def __height(self, node: TreeNode) -> int:
        if not node:
            return 0

        return max(self.__height(node.left), self.__height(node.right)) + 1

    def remove(self, data) -> bool:
        if self.contains(data):
            self.root = self.__remove(self.root, data)
            self.node_count -= 1
            return True
        return False

    def __remove(self, node: TreeNode, data):
        if not node:
            return None

        if data > node.data:
            node.right = self.__remove(node.right, data)

        elif data < node.data:
            node.left = self.__remove(node.left, data)

        else:
            if not node.left:
                return node.right

            elif not node.right:
                return node.left

            else:
                tmp = self.__find_min(node.right)
                node.data = tmp.data
                node.right = self.__remove(node.right, tmp.data)

        return node

    def __find_min(self, node: TreeNode):
        while node.left:
            node = node.left
        return node

