def fib(n):
    """
    Complexity: O(2ⁿ)
    Once the input gets to greater than 30, it starts to get way slower.
    """

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


def main() -> None:
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55


if "__main__" == __name__:
    main()
