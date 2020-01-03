from typing import List

IntList = List[int]


def reverse_list(l: IntList) -> IntList:
    """Reverse a list without making the list physically smaller."""

    def reverse_list_helper(index: int):
        if index == -1:
            return []

        rest_rev: IntList = reverse_list_helper(index - 1)
        first: IntList = [l[index]]

        result: IntList = first + rest_rev

        return result

    return reverse_list_helper(index=len(l) - 1)


def main() -> None:
    assert reverse_list([1, 2, 3]) == [3, 2, 1]


if __name__ == "__main__":
    main()
