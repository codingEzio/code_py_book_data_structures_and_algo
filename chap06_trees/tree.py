__doc__ = """Basics
  Abstract Syntax Tree (AST)
    Other than the common expression like '(10 + 5) * 2 + 1', we can also write
    it in other ways, which is changing the positions of the operands,
    here's the examples:
      prefix    + * + 10 5 2 1    en.wikipedia.org/wiki/Polish_notation
      postfix   10 5 + 2 * 1 +    en.wikipedia.org/wiki/Reverse_Polish_notation
"""


class NumNode:
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num


class PlusNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()


class TimesNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()


def main() -> None:
    x = NumNode(10)
    y = NumNode(5)
    x_plus_y = PlusNode(x, y)
    x_plus_y_times2 = TimesNode(x_plus_y, NumNode(2))
    whole_expression = PlusNode(x_plus_y_times2, NumNode(1))

    print(whole_expression)
    assert whole_expression.eval() == 31


if "__main__" == __name__:
    main()
