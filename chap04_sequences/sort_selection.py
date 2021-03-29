def select(seq, start):
    min_index = start

    for idx in range(start + 1, len(seq)):
        if seq[min_index] > seq[idx]:
            min_index = idx

    return min_index


def selection_sort_in_place(seq):
    """
    O(N^2) cuz there are two for-loops
    """

    for idx in range(len(seq) - 1):
        # compare the first and first+1 element with the other items
        # get its index so that we could skip it and keep in sync with `idx`
        min_index = select(seq, idx)

        # switch the value between the smallest and `seq[idx]` (1 vs else)
        # store  the value that is going to be replaced/swapped
        tmp = seq[idx]

        # move the smallest item to the first place (e.g. seq[0])
        # at the same time, retain the non-min value by swapping them
        seq[idx], seq[min_index] = seq[min_index], tmp

    return seq


def main():
    assert selection_sort_in_place([3, 9, 7, 1]) == [1, 3, 7, 9]


if "__main__" == __name__:
    main()
