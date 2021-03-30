import random


def partition(seq, start, stop):
    """
    #TODO more notes need!
    """
    pivot_index = start
    pivot = seq[pivot_index]
    i = start + 1
    j = stop - 1

    while i <= j:

        while i <= j and not pivot < seq[i]:
            i += 1

        while i <= j and pivot < seq[j]:
            j -= 1

        if i < j:
            tmp = seq[i]
            seq[i], seq[j] = seq[j], tmp

            i += 1
            j -= 1

    seq[pivot_index] = seq[j]
    seq[j] = pivot

    return j


def quicksort_recursive(seq, start, stop):
    if start >= stop - 1:
        return None

    # Assumed steps that gone through (take [9, 1, 5, 3, 20, 10] for example)
    #   get a pivot from ↑
    #       LEFT-sub    [1, 5, 3] < [pivot] < [20, 10]
    #       -------------------------------------------
    #       LEFT-sub    []        < [pivot] < [5, 3]
    #       LEFT-sub    [3]       < [pivot] < []        // [pivot, 3, 5]
    #       -------------------------------------------
    #      RIGHT-sub    [10]      < [pivot] < []        // [10, 20]
    #   two-step process
    #       use recursion to reduce the comparison to basic `i < j`
    #       pick pivot and compare
    #                only two   compare & return
    #           more than two   continue the recursion
    pivot_index = partition(seq, start, stop)

    quicksort_recursive(seq, start, pivot_index)
    quicksort_recursive(seq, pivot_index + 1, stop)


def quicksort(seq):
    """
    O(N logN)

    The point of picking a pivot is
    - the pivot is in its final location (won't move anywhere else)
    - the two sublists are now smaller  (pivot - either side be bigger/smaller)
    """

    # A good pivot is quite important for the O(N logN) complexity
    #   It should reside exactly in or around the middle
    #   Hard to do so, so we randomized the list instead (then [0] for pivot)
    for idx in range(len(seq)):
        rd_int = random.randint(0, len(seq) - 1)

        tmp = seq[idx]
        seq[idx], seq[rd_int] = seq[rd_int], tmp

    quicksort_recursive(seq, 0, len(seq))


def main():
    """
    Understanding of different parts
    - recursion         100%
    - incr in partition meh
    """
    d, d_sorted = [17, 2, 9, 70, 6, 11, 5], [2, 5, 6, 9, 11, 17, 70]
    quicksort(d)
    assert d == d_sorted


if __name__ == "__main__":
    main()
