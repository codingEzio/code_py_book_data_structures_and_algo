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

    def insert_node(self, value) -> None:
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)

    def find_node(self, value) -> bool:
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)

        if value > self.value and self.right_child:
            return self.right_child.find_node(value)

        return value == self.value


def main() -> None:
    # Expected result for testing:
    #    10
    #   8  12
    # 7 9 11 13
    root_node = BinarySearchTree(10)

    root_node.insert_node(8)  # root-left
    root_node.insert_node(7)  # root-left-left
    root_node.insert_node(9)  # root-left-right
    root_node.insert_node(9)  # root-left-right-LEFTorLEAF

    root_node.insert_node(12)  # root-right
    root_node.insert_node(11)  # root-right-left
    root_node.insert_node(13)  # root-right-right

    assert root_node.find_node(10) is True
    assert root_node.find_node(7) is True
    assert root_node.find_node(13) is True
    assert root_node.find_node(20) is False


if "__main__" == __name__:
    main()
