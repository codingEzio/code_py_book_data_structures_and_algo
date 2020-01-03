from typing import List, Union

IntList = List[int]
SimpleSequence = Union[IntList, str]


def reverse_via_reflection(sequence: SimpleSequence) -> SimpleSequence:
    sequence_type: type = type(sequence)  # e.g. <class 'TYPE'>
    empty_sequence: SimpleSequence = sequence_type() # e.g. list() str()

    if sequence == empty_sequence:
        return empty_sequence

    rest_rev: SimpleSequence = reverse_via_reflection(sequence[1:])
    first: SimpleSequence = sequence[0:1]

    result: SimpleSequence = rest_rev + first

    return result


def main():
    assert reverse_via_reflection([1, 2, 3]) == [3, 2, 1]
    assert reverse_via_reflection("abc") == "cba"


if __name__ == "__main__":
    main()
