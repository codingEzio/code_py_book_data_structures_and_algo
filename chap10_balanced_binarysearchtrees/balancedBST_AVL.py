# Ref:
# https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
# https://www.geeksforgeeks.org/avl-tree-set-2-deletion/


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):
    def insert(self, root, key):
        """
        Returns inserted/modified tree nodes directly.
        """

        # Step one: perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step two: update the height of the ancestor node
        root.height = 1 + max(
            self.get_height(root.left), self.get_height(root.right)
        )

        # Step three: get the balance factor
        balance = self.get_balance(root)

        # Step four: if the node is unbalanced, try out these four cases

        # ---- Case 1: LEFT LEFT   ----
        if balance > 1 and key < root.left.value:
            return self.right_rotate(root)

        # ---- Case 2: RIGHT RIGHT ----
        if balance < -1 and key > root.right.value:
            return self.left_rotate(root)

        # ---- Case 3: LEFT RIGHT  ----
        if balance > 1 and key > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # ---- Case 4: RIGHT LEFT  ----
        if balance < -1 and key < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, key):
        """
        Recursive function to delete a node with given key from sub-tree with
        given root. It returns root of the modified sub-tree.
        """

        # Step one: perform normal BST
        if not root:
            return root
        elif key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp, root = root.right, None
                return temp
            elif root.right is None:
                temp, root = root.left, None
                return temp

            temp = self.get_min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        # If the tree has only one node, simply return it
        if root is None:
            return root

        # Step two: update the height of the ancestor node
        root.height = 1 + max(
            self.get_height(root.left), self.get_height(root.right)
        )

        # Step three: get the balance factor
        balance = self.get_balance(root)

        # Step four: if the node is unbalanced, try out these four cases

        # ---- Case 1: LEFT  LEFT   ----
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # ---- Case 2: RIGHT RIGHT  ----
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # ---- Case 3: LEFT  RIGHT  ----
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # ---- Case 4: RIGHT LEFT   ----
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_height(self, root):
        if not root:
            return 0

        return root.height

    def get_balance(self, root):
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root

        return self.get_min_value_node(root.left)

    def right_rotate(self, z):
        # y = z.left
        # T = z.left.right
        y = z.left
        T = y.right

        # z.left.right = z
        # z.left       = z.left.right
        y.right = z
        z.left = T

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def left_rotate(self, z):
        # y = z.right
        # T = z.right.left
        y = z.right
        T = y.left

        # z.left.right = z
        # z.left       = z.left.right
        y.left = z
        z.right = T

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def pre_order(self, root):
        if not root:
            return None

        print(f"{root.value}", end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)


def main() -> None:
    avl = AVLTree()
    root = None

    root = avl.insert(root, 10)
    root = avl.insert(root, 20)
    root = avl.insert(root, 30)
    root = avl.insert(root, 40)
    root = avl.insert(root, 50)
    root = avl.insert(root, 25)

    print(avl.pre_order(root))

    root = avl.delete(root, 30)
    print(avl.pre_order(root))


if "__main__" == __name__:
    main()
