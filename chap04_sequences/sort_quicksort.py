import random


def partition(seq, start, stop):
    """
    #TODO more notes need!
    """
    pivot_index = start
    pivot = seq[pivot_index]
    sublist_start = start + 1
    sorted_last_el = stop - 1

    while sublist_start <= sorted_last_el:

        # notes on switching the '>=' to '<' (and the elements of course)
        #   benefits        only the `__lt__` needs to be implemented
        #   alternative     `while .. and not pivot < seq[sublist_start]`
        while sublist_start <= sorted_last_el and pivot >= seq[sublist_start]:
            sublist_start += 1

        while sublist_start <= sorted_last_el and pivot < seq[sorted_last_el]:
            sorted_last_el -= 1

        if sublist_start < sorted_last_el:
            tmp = seq[sublist_start]
            seq[sublist_start], seq[sorted_last_el] = seq[sorted_last_el], tmp

            sublist_start += 1
            sorted_last_el -= 1

    seq[pivot_index] = seq[sorted_last_el]
    seq[sorted_last_el] = pivot

    return sorted_last_el


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

    # recur -> recur -> RETURN
    #   -> RECUR            NEXT    some values being returned (None or else)
    #   -> RECUR next line  NEXT    the previous call stack is cleared
    quicksort_recursive(seq, start, pivot_index)

    # encounter a return   -> exec this line (in recursion) (⭐️)
    # clear the call stack -> exec this line (not in recur)
    quicksort_recursive(seq, pivot_index + 1, stop)


def quicksort(seq):
    """
    O(N logN)

    O(N^2) if a bad pivot is chosen or is/is-nearly sorted
        i.e. expected: ~middle, imagined-scenario: a really big/small number
        normally there won't be any problems after pre-randomizing the list

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
    - incr in partition better
    """
    d, d_sorted = [17, 2, 9, 70, 6, 11, 5], [2, 5, 6, 9, 11, 17, 70]
    quicksort(d)
    assert d == d_sorted


# references
#   concept with examples
#       https://www.reddit.com/r/explainlikeimfive/comments/lb7w1/eli5_how_in_the_hell_does_quicksort_work/c2r9isp/

if __name__ == "__main__":
    main()
