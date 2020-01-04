from pylist import IntList


def merge(seq: IntList, start: int, mid: int, stop: int) -> None:
    lst: IntList = []
    i: int = start
    j: int = mid

    while i < mid and j < stop:
        if seq[i] < seq[j]:
            lst.append(seq[i])
            i += 1
        else:
            lst.append(seq[j])
            j += 1

    while i < mid:
        lst.append(seq[i])
        i += 1

    for i in range(len(lst)):
        seq[start + i] = lst[i]


def merge_sort_recursively(seq: IntList, start: int, stop: int) -> None:
    if start >= stop - 1:
        return None

    mid: int = (start + stop) // 2

    # One of the most hard-to-understand part for me is these three lines,
    # after making some researches, I'm finally be able to comprehend these.
    # Here's some tricks while debugging it: focus on the params you passed,
    # goddamn! I don't even notice it before, it's the most easy way to know
    # what "call stack" you are in, and when the next recursive call is called,
    # "the next" means the 2nd line (NOT recursively called BUT exec to there).
    merge_sort_recursively(seq=seq, start=start, stop=mid)
    merge_sort_recursively(seq=seq, start=mid, stop=stop)

    merge(seq=seq, start=start, mid=mid, stop=stop)


def merge_sort(seq: IntList) -> None:
    merge_sort_recursively(seq=seq, start=0, stop=len(seq))


def main() -> None:
    pass


if "__main__" == __name__:
    main()
