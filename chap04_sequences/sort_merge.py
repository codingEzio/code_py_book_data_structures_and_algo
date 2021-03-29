def merge(seq, start, mid, stop):
    """
    merge lists (sub-lists) that have been sorted
    """

    lst = []
    _start = start
    _mid = mid

    while _start < mid and _mid < stop:
        if seq[_start] < seq[_mid]:
            lst.append(seq[_start])
            _start += 1
        else:
            lst.append(seq[_mid])
            _mid += 1

    # leftover
    while _start < mid:
        lst.append(seq[_start])
        _start += 1

    # copy the items back to the original sequence
    for idx in range(len(lst)):
        seq[start + idx] = lst[idx]


def merge_sort_recursive(seq, start, stop):
    """
    a helper function to get things (split & sort) started
    """

    if start >= stop - 1:
        return None

    mid = (start + stop) // 2

    merge_sort_recursive(seq, start, mid)
    merge_sort_recursive(seq, mid, stop)

    # half, half-of-half, half-of-half-of-half -> merge
    # half, half-of-half, half-of-half-of-half -> merge another
    # merge both                               -> the end
    merge(seq, start, mid, stop)


def merge_sort(seq):
    """
    O(N logN)
        O(logN) for dividing the list into lists of size 1
        O(N)    for merging the sorted sublists
    """
    merge_sort_recursive(seq, 0, len(seq))


def main():
    """
    Not 100% percent get this algorithm, but nearly done :)
    """
    d, d_sorted = [3, 7, 9, 40, 1, 13, 10], [1, 3, 7, 9, 10, 13, 40]
    merge_sort(d)
    assert d == d_sorted


if "__main__" == __name__:
    main()
