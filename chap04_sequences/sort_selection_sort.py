from pylist import IntList


def selection_sort(seq: IntList) -> None:
    """
    Sort lists in-place (complexity: O(n²), yikes).
    Ref: https://djangocentral.com/selection-sort-in-python/
    """

    start: int
    idx: int

    for start in range(len(seq)):
        min_pos = start

        for idx in range(start, len(seq)):
            if seq[idx] < seq[min_pos]:
                min_pos = idx

        (seq[start], seq[min_pos]) = (seq[min_pos], seq[start])


def main() -> None:
    pass


if "__main__" == __name__:
    main()
