# Ref: https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        """
        Either create a new one
        or     replace the old one with the new one (& new one as its child XD)
        """
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        """
        Either create a new one
        or     replace the old one with the new one (& new one as its child XD)
        """
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node


def main() -> None:
    bi = BinaryTree("A")
    assert bi.value == "A"
    assert bi.left_child is None
    assert bi.right_child is None

    bi.insert_left("B")  # A -> B
    bi.insert_left("C")  # A -> C -> B
    assert bi.left_child.value == "C"
    assert bi.left_child.left_child.value == "B"

    bi.insert_right("D")  # A -> D
    bi.insert_right("E")  # A -> E -> D
    assert bi.right_child.value == "E"
    assert bi.right_child.right_child.value == "D"


if "__main__" == __name__:
    main()
