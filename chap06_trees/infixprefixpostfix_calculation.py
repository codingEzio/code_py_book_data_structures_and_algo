class TimesNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()

    def inorder(self):
        return f"({self.left.inorder()} * {self.right.inorder()})"


class PlusNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()

    def inorder(self):
        return f"({self.left.inorder()} + {self.right.inorder()})"


class NumNode:
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num

    def inorder(self):
        return str(self.num)


def main():
    x, y = NumNode(2), NumNode(5)

    # a tree built from bottom to the root
    cal_times = TimesNode(x, y)
    cal_plus = PlusNode(x, y)

    # Once you start using the `eval` method, the methods inside both node will
    # be called. This concept is called as 'mutual recursion'.
    sum_times_plus = PlusNode(cal_times, cal_plus)

    # Almost all of the explanations SUCK. Most do not have a single real-world
    # use case to explain the WHY and its alternatives. Sigh :(
    # 1. https://stackoverflow.com/a/10295928/6273859
    # 2. https://bit.ly/3mh5qX4
    # 3. https://bit.ly/3fEV0iX

    # Conceptually, it is a type of recursion that two recursive functions
    # calling/depending each other. The code could be "short and elegant".

    assert sum_times_plus.eval() == 17
    assert sum_times_plus.inorder() == "((2 * 5) + (2 + 5))"


if "__main__" == __name__:
    main()
