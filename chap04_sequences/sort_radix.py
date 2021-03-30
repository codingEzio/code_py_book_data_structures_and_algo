def radix_sort(seq):
    """
    O(NK)
    """
    digit = 0
    max_digit, max_value = 1, max(seq)

    # the digits of the maximum number
    while 10 ** max_digit < max_value:
        max_digit += 1

    # compare based the last digits (0 ~ max digits)
    #   default     312 | 521 | _22 | __0 | 450 | _45
    #              -----------------------------------
    #   1st digit   __0 | 450 | 521 | 312 | _22 | _45  THEN
    #   2nd digit   __0 | 312 | 521 | _22 | _45 | 450  THEN
    #   3rd digit   __0 | _22 | _45 | 312 | 450 | 521  -> sorted
    while digit < max_digit:
        temp_empty_lists = [[] for i in range(10)]  # ten empty list

        # store a list of numbers in groups of different digits
        #   [
        #       # empty [] were omitted for brevity
        #       0 -> [0, 450],
        #       1 -> [521]
        #       2 -> [312, 22]
        #       5 -> [45]
        #   ]
        for idx in seq:
            t = int((idx / (10 ** digit)) % 10)
            temp_empty_lists[t].append(idx)

        sorted_based_on_digit_x = []

        for bucket in temp_empty_lists:
            for idx in bucket:

                # add those "semi/kinda" sorted to a empty bucket (list/array)
                sorted_based_on_digit_x.append(idx)

        # saved for the next loop (pick a new digit to compare)
        seq = sorted_based_on_digit_x

        digit += 1

    return seq


def main():
    d, d_sorted = [312, 521, 22, 0, 450, 45], [0, 22, 45, 312, 450, 521]
    assert radix_sort(d) == d_sorted


# references
#   examples only
#       https://github.com/hustcc/JS-Sorting-Algorithm/


if "__main__" == __name__:
    main()
