from typing import List

IntList = List[int]


def reverse_list(l: IntList) -> IntList:
    """Reverse a list via simple list concatenation."""
    accumulator: IntList = []

    i: int
    for i in l:
        accumulator = [i] + accumulator  # the order matters

    return accumulator


def reverse_list_recursive(l: List[int]) -> List[int]:
    if l == []:
        return []

    rest_rev = reverse_list_recursive(l[1:])
    first = l[0:1]

    result = rest_rev + first

    return result


def reverse_string_recursive(s: str) -> str:
    if s == "":
        return ""

    rest_rev = reverse_string_recursive(s[1:])
    first = s[0:1]

    result = rest_rev + first

    return result


def main() -> None:
    assert reverse_list([9, 8, 7]) == [7, 8, 9]
    assert reverse_list_recursive([9, 8, 7]) == [7, 8, 9]

    assert reverse_string_recursive("Let it go") == "og ti teL"


if __name__ == "__main__":
    main()
