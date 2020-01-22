# Ref: https://rosettacode.org/wiki/AVL_tree#Python

# Issues: I can't make the 'delete' feature work right now.

# This modified version would be used for debugging on pythontutor.com
# 0. notes here might not be keep in sync with the original
# 1. the 'sys.argv' part was removed due to limitations of pythontutor
# 2. the ASCII art was removed cuz pythontutor couldn't handle steps that >999
# 3. the '__str__' was replaced with simple `repr(self)` (instead of ASCII art)
from random import randrange


class AVLNode(object):
    """A node in the AVL tree.
    """

    def __init__(self, parent, key):
        """
        Creates a AVL node.

        Args:
            key:    The key of the node
            parent: The node's parent
        """
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        """
        Modified in order to work with pythontutor.com (reduce exec steps).
        For alternative solutions, go see this website for visualizations:
        ~ https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
        """
        return repr(self)

    def insert(self, node):
        """
        Inserts a node into the sub-tree rooted at this node.

        Args:
            node: The node to be inserted.
        """
        if node is None:
            return None

        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

    def delete(self):
        """
        Deletes and returns this node from the tree.
        """
        if self.left is None or self.right is None:

            if self is self.parent.left:
                self.parent.left = self.left or self.right

                if self.parent.left is not None:
                    self.parent.left.parent = self.parent

            else:
                self.parent.right = self.left or self.right

                if self.parent.right is not None:
                    self.parent.right.parent = self.parent

        else:
            s = self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()

    def next_larger(self):
        """
        Returns the node with the next larger key (the successor) in the BST.
        """
        if self.right is not None:
            return self.right.find_min()

        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent

        return current.parent

    def find(self, key):
        """
        Finds & returns the node with key from the subtree rooted at this node.

        Args:
            k: The key of the node we want to find.

        Returns:
            The node with key 'key'.
        """
        if key == self.key:
            return self
        elif key < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(key)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(key)

    def find_min(self):
        """
        Finds the node with minimum key in the sub-tree rooted at this node.

        Returns:
            The node with the minimum key.
        """
        current = self

        while current.left is not None:
            current = current.left

        return current


def height(node):
    if node is None:
        return -1
    else:
        return node.height


def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1


class AVL(object):
    """
    AVL binary search tree implementation.
    """

    def __init__(self):
        """
        Initialize an empty tree.
        """
        self.root = None

    def __str__(self):
        if self.root is None:
            return "<empty tree>"
        return str(self.root)

    def find(self, key):
        """
        Finds & returns the node with key 'key' from the sub-tree rooted at node.

        Args:
            key: The key of the node we want to find.

        Returns:
            The node with key 'key' or None if the tree is empty.
        """
        return self.root and self.root.find(key)

    def find_min(self):
        """
        Returns the minimum node of this binary search tree.
        """
        return self.root and self.root.find_min()

    def next_larger(self, key):
        """
        Returns the node that contains the next larger key (the successor) in
        the binary search tree in relation to the node with key 'key'.

        Args:
            key: The key of the node of which the successor is to be found.

        Returns:
            The successor node.
        """
        node = self.find(key)

        return node and node.next_larger()

    def insert(self, key):
        """
        Inserts a node with key 'key' into the sub-tree rooted at this node.
        This AVL version guarantees the balance property: h = O(log n)

        Args:
            key: The key of the node to be inserted.
        """
        node = AVLNode(None, key)

        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)

        self.rebalance(node)

    def delete(self, key):
        """
        Deletes & returns a node with key 'key' if it exists from the BST.
        This AVL version guarantees the balanced property: h = O(log n).

        Args:
            key: The key of the node that we want to delete.

        Returns:
            The deleted node with key 'key'.
        """
        node = self.find(key)

        if node is None:
            return None
        if node is self.root:
            pseudoroot = AVLNode(None, 0)
            pseudoroot.left = self.root
            self.root.parent = pseudoroot
            deleted = self.root.delete()
            self.root = pseudoroot.left
            if self.root is not None:
                self.root.parent = None
        else:
            deleted = node.delete()

        self.rebalance(deleted.parent)

    def rebalance(self, node):
        while node is not None:
            update_height(node)

            if height(node.left) >= (2 + height(node.right)):

                if height(node.left.left) >= height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)

            elif height(node.right) >= (2 + height(node.left)):

                if height(node.right.right) >= height(node.right.right):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)

            node = node.parent

    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent

        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y

        x.right = y.left
        if x.right is not None:
            x.right.parent = x

        y.left = x
        x.parent = y

        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent

        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y

        x.left = y.right
        if x.left is not None:
            x.left.parent = x

        y.right = x
        x.parent = y

        update_height(x)
        update_height(y)


def test(args=None):
    if type(args) is int:
        items = [randrange(0, 100) for i in range(args)]
    elif type(args) is list:
        items = [int(i) for i in args]

    print(f"----- {list(items)} -----")
    print(
        r"""
79
/\

 79
 /\
37
/\
ROTATE OPERATION!!

  72
 / \
37 79
/\ /\

   72
  / \
 37 79
 /\ /\
32
/\
ROTATE OPERATION!!

   .72
  /   \
 32   79
 / \  /\
3  37
/\ /\
ROTATE OPERATION!!

   37
  /  \
 32   72
 /\  / \
3   48 79
/\  /\ /\

   37
  /  \
 32   72
 /\  / \
3   48 79
/\  /\ /\
        88
        /\
ROTATE OPERATION!!

   .37
  /   \
 32   72
 /\  /  \
3   48   88
/\  /\  / \
       79 93
       /\ /\

    """
    )
    avl_tree = AVL()

    for item in items:
        avl_tree.insert(item)

    avl_tree.find(93)


if __name__ == "__main__":
    # test(args=8)
    test(args=[79, 37, 72, 32, 3, 48, 88, 93])
