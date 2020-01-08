# Ref: https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/


class BinarySearchTree:
    """
    Here's a simple illustration:
        4
      2  6      # the left  side is always "TOP > BOTTOM" (applies to all lvl)
    1 3  5 7    # the right side is always "TOP < BOTTOM" (applies to all lvl)
    """

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def find_node(self, value) -> bool:
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)

        if value > self.value and self.right_child:
            return self.right_child.find_node(value)

        return value == self.value

    def insert_node(self, value) -> None:
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)

    def remove_node(self, value, parent) -> bool:
        """
        Different scenarios (cuz ya might need to re-organize after deletion)

        [#1 a node without children]
           10                         10
          8  12     (DELETE 11)     8   12
        7 9 11 13                  7 9 👻 13
                                       (simply remove the leaf node)

        [#2 a node with one child]
           10                         10
          8  12     (DELETE 13)      8  12
        7 9 11 13                  7 9 11 14(👻)
                 14                    (now the child became the parent)

        [#3 a node with two children]
           10                         10
          8  12     (DELETE 12)      8  13(👻)
        7 9 11 13                  7 9 11 MOVED
                                       (maintain the left(TOP>BOT), move node)
        """
        if value < self.value and self.left_child:
            return self.left_child.remove_node(value, self)

        elif value < self.value:
            return False

        elif value > self.value and self.right_child:
            return self.right_child.remove_node(value, self)

        elif value > self.value:
            return False

        else:

            if (
                self.left_child is None
                and self.right_child is None
                and self == parent.left_child
            ):
                parent.left_child = None
                self.helper_clear_node()

            elif (
                self.left_child is None
                and self.right_child is None
                and self == parent.right_child
            ):
                parent.right_child = None
                self.helper_clear_node()

            elif (
                self.left_child
                and self.right_child is None
                and self == parent.left_child
            ):
                parent.left_child = self.left_child
                self.helper_clear_node()

            elif (
                self.left_child
                and self.right_child is None
                and self == parent.right_child
            ):
                parent.right_child = self.left_child
                self.helper_clear_node()

            elif (
                self.right_child
                and self.left_child is None
                and self == parent.left_child
            ):
                parent.left_child = self.right_child
                self.helper_clear_node()

            elif (
                self.right_child
                and self.left_child is None
                and self == parent.right_child
            ):
                parent.right_child = self.right_child
                self.helper_clear_node()

            else:
                self.value = self.right_child.helper_find_min_value()
                self.right_child.remove_node(self.value, self)

        return True

    def helper_clear_node(self) -> None:
        self.value = None
        self.left_child = None
        self.right_child = None

    def helper_find_min_value(self):
        if self.left_child:
            return self.left_child.helper_find_min_value()
        else:
            return self.value


def main() -> None:
    # Expected result for testing:
    #    10
    #   8  12
    # 7 9 11 13
    #         14
    root_node = BinarySearchTree(10)

    root_node.insert_node(8)  # root-left
    root_node.insert_node(7)  # root-left-left (also leaf-node)
    root_node.insert_node(9)  # root-left-right (also leaf-node)

    root_node.insert_node(12)  # root-right
    root_node.insert_node(11)  # root-right-left (also leaf-node)
    root_node.insert_node(13)  # root-right-right

    # purely added for demonstrating 'a node with one child' scenario
    root_node.insert_node(14)  # root-right-right-right (also leaf-node)

    assert root_node.find_node(10) is True
    assert root_node.find_node(7) is True
    assert root_node.find_node(13) is True
    assert root_node.find_node(20) is False

    """ a node without child """
    # before
    assert root_node.left_child.left_child is not None
    # after
    root_node.remove_node(7, None)
    assert root_node.left_child.left_child is None
    assert root_node.left_child.right_child.value == 9

    """ a node with one child """
    # before
    assert root_node.right_child.right_child.right_child is not None
    assert root_node.right_child.right_child.right_child.value == 14
    # after
    root_node.remove_node(13, None)
    assert root_node.right_child.right_child.right_child is None
    assert root_node.right_child.right_child.value == 14

    """ a node with two children """
    # before
    assert root_node.right_child.value == 12
    assert root_node.right_child.right_child is not None
    # after
    root_node.remove_node(12, None)
    assert root_node.right_child.value == 14
    assert root_node.right_child.right_child is None


if "__main__" == __name__:
    main()
