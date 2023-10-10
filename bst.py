class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self._size = 0   # <-- Variable is now named "_size"

    def size(self):    # <-- Method keeps the name "size"
        return self._size


    def is_empty(self):
        return self._size == 0

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def add(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            self._add(item, self.root)
        self._size += 1

    def _add(self, item, node):
        if item < node.data:
            if node.left is None:
                node.left = Node(item)
            else:
                self._add(item, node.left)
        else:
            if node.right is None:
                node.right = Node(item)
            else:
                self._add(item, node.right)

    def remove(self, item):
        if self.root is None:
            return
        self.root = self._remove(item, self.root)
        self._size -= 1

    def _remove(self, item, node):
        if node is None:
            return node
        if item < node.data:
            node.left = self._remove(item, node.left)
        elif item > node.data:
            node.right = self._remove(item, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.data = self._find_min(node.right)
                node.right = self._remove(node.data, node.right)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node.data

    def find(self, item):
        return self._find(item, self.root)

    def _find(self, item, node):
        if node is None:
            raise ValueError("Item not found")
        if item == node.data:
            return node.data
        elif item < node.data:
            return self._find(item, node.left)
        else:
            return self._find(item, node.right)

    def inorder(self):
        items = []
        self._inorder(self.root, items)
        return items

    def _inorder(self, node, items):
        if node is not None:
            self._inorder(node.left, items)
            items.append(node.data)
            self._inorder(node.right, items)

    def preorder(self):
        items = []
        self._preorder(self.root, items)
        return items

    def _preorder(self, node, items):
        if node is not None:
            items.append(node.data)
            self._preorder(node.left, items)
            self._preorder(node.right, items)

    def postorder(self):
        items = []
        self._postorder(self.root, items)
        return items

    def _postorder(self, node, items):
        if node is not None:
            self._postorder(node.left, items)
            self._postorder(node.right, items)
            items.append(node.data)

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(node.data)
            self._print_tree(node.right)