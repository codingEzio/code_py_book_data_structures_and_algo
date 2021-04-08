import sys

if len(sys.argv) == 2:
    if sys.argv[1] == 'debug':
        DEBUG = True
    else:
        DEBUG = False
else:
    DEBUG = False


class BinarySearchTree:

    class __Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

        def get_value(self):
            return self.value

        def get_left(self):
            return self.left

        def get_right(self):
            return self.right

        def set_value(self, new_value):
            self.value = new_value

        def set_left(self, new_left):
            self.left = new_left

        def set_right(self, new_right):
            self.right = new_right

        def __iter__(self):
            """
            In-order traversal (from the bottom)
            """
            if self.left is not None:
                for elem in self.left:
                    yield elem
            else:
                if DEBUG:
                    yield f"\nI'm None here! #LEFT\t(at {str(self)[44:-2]})"

            yield self.value

            if self.right is not None:
                for elem in self.right:
                    yield elem
            else:
                if DEBUG:
                    yield f"I'm None here! #RIGHT\t(at {str(self)[44:-2]}) \n"

    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        O(logN) all the way (insert, delete, lookup)

        It cannot guarantee the O(logN), keyword: more-space, balanced, sorted
        If the values are to inserted were already sorted, it
        - insert n items became O(N^2) in the worse case
        - the tree being built will become a "long stick" (~= linked list)
        """

        def __insert(root, value):

            # relation with recursion
            # - outside: initialize the first element as the root node
            # - inside : tranform any received vals into a `__Node` object
            if root is None:
                return BinarySearchTree.__Node(value)

            # fmt: off
            # relation with recursion
            # - outside: compare between `root` and inserted (level 1 and 2)
            # - inside : replace with the subtree's root (via `get_left/right`)
            if value < root.get_value():

                # get the `__Node` instance for L/R via the recursion inside
                root.set_left(
                    __insert(
                        # enter the subtrees via replacing the `root` in recur
                        root.get_left(), value
                    )
                )

            else:

                # get the `__Node` instance for L/R via the recursion inside
                root.set_right(
                    __insert(
                        # enter the subtrees via replacing the `root` in recur
                        root.get_right(), value
                    )
                )

            return root

        # call nested function
        self.root = __insert(self.root, value)

    def __iter__(self):
        """
        Nothing fancy here, all the fancy stuff are inside the `__Node` class
        """

        # call the `__iter__` inside the BST, or return `[]` if it's empty
        if self.root is not None:
            return self.root.__iter__()
        else:
            return [].__iter__()


def main():
    tree = BinarySearchTree()
    lst = [5, 8, 2, 1, 4, 9, 6, 7]

    for elem in lst:
        tree.insert(elem)

    # see 'bst_inorder.log' if you wanna know how the `__iter__` works :)

    if DEBUG is True:
        for elem in tree:
            print(elem)
    else:
        assert [elem for elem in tree] == [1, 2, 4, 5, 6, 7, 8, 9]
        print("Assertion passed.")


if "__main__" == __name__:
    main()
