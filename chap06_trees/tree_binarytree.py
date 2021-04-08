from queue import Queue


class BinaryTree:
    """
    All the unimaginable or unintuitive parts should be attributed to the
    call stack (e.g. inorder -> that's why you go straight to bottom left)

    Cheatsheet
    - pre_order     node L    R
    - in_order      L    node R
    - post_order    L    R    node
    """

    def __init__(self, value):
        """
        You don't have to put the left/right in the param list, since it is
        only meant for internal use only.

        Note that every node in itself is a root node. Unless there's context,
        which there isn't in the recursions, the nodes aren't "left" or "right"

        The `value` here could also be considered as (if it helps)
        - root      lv0 root, or sub-level root
        - node      node   + node's left   + node's right
        - parent    parent + parent's left + parent's right
        """
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        """
        either put the value into the slot
        or     put the value into the slot (plus new.LR = old_LR)
        """
        if self.left is None:
            self.left = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left = self.left

            self.left = new_node

    def insert_right(self, value):
        """
        either put the value into the slot
        or     put the value into the slot (plus new.LR = old_LR)
        """
        if self.right is None:
            self.right = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right = self.right

            self.right = new_node

    def dfs_preorder(self):
        print(self.value, end=" ")

        if self.left:
            self.left.dfs_preorder()

        if self.right:
            self.right.dfs_preorder()

    def dfs_inorder(self):
        if self.left:
            self.left.dfs_inorder()

        print(self.value, end=" ")

        if self.right:
            self.right.dfs_inorder()

    def dfs_postorder(self):
        if self.left:
            self.left.dfs_postorder()

        if self.right:
            self.right.dfs_postorder()

        print(self.value, end=" ")

    def bfs_levelorder(self):
        """
        The only reason we use `Queue` is because its FIFO principle, which
        eases the process of "traverse and then mark as discovered".
        """
        queue = Queue()
        queue_first_put_first_out = queue.put
        queue_access_then_delete_first_out = queue.get

        # Although you can't iterate them directly, you could know that
        # - the nodes are "sorted" (?because YOU inserted that way)
        # - the one in the foremost will be accessed first (lv0 -> lv1 ..)
        queue_first_put_first_out(self)

        # All the nodes will be "checked" (all levels in case there's subtrees)
        while not queue.empty():

            # remove/mark-as-discovered root node (lv0 -> lv1 -> lv2 ..)
            current_node = queue_access_then_delete_first_out()

            print(current_node.value, end=" ")

            # e.g. { a.L/R, b.L/R, .. h.L/R }
            if current_node.left:
                queue_first_put_first_out(current_node.left)

            # e.g. { a.L/R, b.L/R, .. h.L/R }
            if current_node.right:
                queue_first_put_first_out(current_node.right)


def main():
    # level zero
    root = BinaryTree("A")
    # level one
    root.insert_left("B")
    root.insert_right("C")
    # level two
    lv2_b_root = root.left
    lv2_b_root.insert_left("D")
    lv2_b_root.insert_right("E")
    lv2_c_root = root.right
    lv2_c_root.insert_left("F")
    lv2_c_root.insert_right("G")
    # level three
    lv3_d_root = lv2_b_root.left
    lv3_d_root.insert_left("H")

    #     A
    #   B   C
    #  D E F G
    # H

    # root.dfs_preorder()  # A (B (D (H) E)) (C (F G))
    # root.dfs_inorder()  # (H D B) E (A) (F C) G
    # root.dfs_postorder()  # (H (D E) B) ((F G) C) A

    root.bfs_levelorder()


if "__main__" == __name__:
    main()
