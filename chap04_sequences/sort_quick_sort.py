import random
from pylist import IntList


def partition(seq: IntList, start: int, stop: int) -> int:
    pivot_index: int = start
    pivot: int = seq[pivot_index]

    i: int = start + 1
    j: int = stop - 1

    while i <= j:
        while i <= j and not pivot < seq[i]:
            i += 1
        while i <= j and pivot < seq[j]:
            j -= 1

        if i < j:
            seq[i], seq[j] = seq[j], seq[i]
            i += 1
            j -= 1

    seq[pivot_index] = seq[j]
    seq[j] = pivot

    return j


def quick_sort_recursively(seq: IntList, start: int, stop: int) -> None:
    if start >= stop - 1:
        return None

    pivot_index = partition(seq=seq, start=start, stop=stop)

    quick_sort_recursively(seq=seq, start=start, stop=pivot_index)
    quick_sort_recursively(seq=seq, start=pivot_index + 1, stop=stop)


def quick_sort(seq: IntList) -> None:
    i: int
    j: int
    seq_len: int = len(seq)

    for i in range(seq_len):
        j = random.randint(0, seq_len - 1)
        seq[i], seq[j] = seq[j], seq[i]  # swap seq[i] and seq[j]

    quick_sort_recursively(seq=seq, start=0, stop=seq_len)


def main() -> None:
    pass


if "__main__" == __name__:
    main()
