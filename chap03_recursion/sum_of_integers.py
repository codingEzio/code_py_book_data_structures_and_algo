import sys


def sum_first_n(num: int):
    """It's O(1) since it only does "simple" computations."""
    return num * (num + 1) // 2


def sum_first_n_recursive(num: int):
    if num == 0:
        return 0
    else:
        return sum_first_n_recursive(num - 1) + num


def sum_first_n_recursive_without_else(num: int):
    if num == 0:
        return 0
    return sum_first_n_recursive_without_else(num - 1) + num


def main():
    n = int(input("Enter a non-neg integer: "))
    sum_ = sum_first_n(num=n)

    print(f"Sum of {n} equals {str(sum_)}")

    try:
        sum__ = sum_first_n_recursive(num=n)
        sum___ = sum_first_n_recursive_without_else(num=n)
    except RecursionError as err:
        print(f"\nError: {sys.exc_info()[1]}")
    else:
        print(f"Sum of {n} equals {str(sum__)} (recursive)")
        print(f"Sum of {n} equals {str(sum___)} (recursive)")


if __name__ == "__main__":
    main()
