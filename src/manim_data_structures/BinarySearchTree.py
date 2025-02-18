class BinarySearchTree:
    """
    Each node has at the most two children:
         The left child holds values that are less than the value of the node
         The right child holds values that are greater than the value of the node
    Any Duplicate values are ignored here
    """

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def __repr__(self):
            return f"Node({self.value})"

    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        This inserts a new value into the tree
        """
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            # To go left
            if node.left is None:
                node.left = self.Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            # To go right
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._insert_recursive(node.right, value)
        else:
            # Duplicate value, ignore insertion.
            pass

    def search(self, value):
        """
        Searches for a value in the tree
        returns a node or nothing at all
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        elif value < node.value:
            return self._search_recursive(node.left, value)
        # value > node.value
        else:  
            return self._search_recursive(node.right, value)

    def in_order_traversal(self):
        """
     in-order traversal of the tree
        returns a list after
        """
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        if node is None:
            return
        self._in_order_recursive(node.left, result)
        result.append(node.value)
        self._in_order_recursive(node.right, result)
