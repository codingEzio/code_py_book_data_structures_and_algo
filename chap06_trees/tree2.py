# Ref: https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/

from queue import Queue


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

    def pre_order(self):
        """LEFT -> LEFT -> .. THE_REST -> RIGHT -> LEFT -> .. THE_REST"""
        print(self.value)

        if self.left_child:
            self.left_child.pre_order()

        if self.right_child:
            self.right_child.pre_order()

    def in_order(self):
        """LEFT MIDDLE RIGHT -> BACKTRACK -> LEFT MIDDLE RIGHT"""
        if self.left_child:
            self.left_child.in_order()

        print(self.value)

        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        """LEFT RIGHT MIDDLE -> BACKTRACK -> LEFT RIGHT MIDDLE"""
        if self.left_child:
            self.left_child.post_order()

        if self.right_child:
            self.right_child.post_order()

        print(self.value)

    def breadth_first_search(self):
        """
        A
        B D
        C E F   => A, B, D, C, E, F (level by level)
        """
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current_node = queue.get()
            print(current_node.value)

            if current_node.left_child:
                queue.put(current_node.left_child)

            if current_node.right_child:
                queue.put(current_node.right_child)

        return queue


def are_my_nodes_in_the_right_place(root_node) -> bool:
    """
    Expected result:
          A
        B   F
       C E  G H
      D
    """
    lvl2_b = root_node.left_child
    lvl2_f = root_node.right_child

    assert lvl2_b.value == "B"
    assert lvl2_f.value == "F"

    assert lvl2_b.left_child.value == "C"
    assert lvl2_b.right_child.value == "E"
    assert lvl2_f.left_child.value == "G"
    assert lvl2_f.right_child.value == "H"

    assert lvl2_b.left_child.left_child.value == "D"


def main() -> None:
    root = BinaryTree("A")

    # Insert lvl2 node
    root.insert_left("B")
    root.insert_right("F")

    # Insert lvl3 node
    node_lv2_b = root.left_child  # entry
    node_lv2_f = root.right_child  # entry
    node_lv2_b.insert_left("C")
    node_lv2_b.insert_right("E")
    node_lv2_f.insert_left("G")
    node_lv2_f.insert_right("H")

    # Insert lvl4 node (only a leaf-node "D")
    node_lvl3_c = node_lv2_b.left_child  # entry
    node_lvl3_c.insert_left("D")

    # Expected result
    #     A
    #   B   F
    #  C E  G H
    # D
    are_my_nodes_in_the_right_place(root)

    # root.pre_order()  # Expected: A B C D E F G H
    # root.in_order()   # Expected: D C B E A G F H
    # root.post_order() # Expected: D C E B G H F A

    root.breadth_first_search()


if "__main__" == __name__:
    main()
