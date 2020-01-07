# Ref: https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    pass


def main() -> None:
    bi = BinaryTree("A")
    assert bi.value == "A"
    assert bi.left_child is None
    assert bi.right_child is None


if "__main__" == __name__:
    main()
