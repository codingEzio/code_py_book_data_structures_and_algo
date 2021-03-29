def reverse_sequence_recursion(sequence):
    # e.g.
    # type('yes')       <class 'str'>
    # type([9, 7, 1])   <class 'list'>
    # type((9, 7, 1))   <class 'tuple'>
    seq_type = type(sequence)

    # this type of operations are called 'reflection'
    #   "a way of getting class names at runtime then crt objs of that class"
    empty_seq = seq_type()

    if sequence == empty_seq:
        return empty_seq

    # take [9, 7, 1] for example (a list of call frames)
    #   [9, 7, 1]
    #   [7, 1]
    #   [1]
    #   []
    rest_reverse = reverse_sequence_recursion(sequence[1:])

    # []      + []  PRODUCES [ ]
    # [ ]     + [1] PRODUCES [1]
    # [  1]   + [7] PRODUCES [1, 7]
    # [  1 7] + [9] PRODUCES [1, 7, 9]
    first = sequence[0:1]
    # the left  side is the value being returned
    # the right side is the value of `first`

    return rest_reverse + first


# references
#   concept
#       https://stackoverflow.com/a/37635/6273859
#   concept with examples
#   see more
#       reflection in other languages
#           https://en.wikipedia.org/wiki/Reflective_programming


def main():
    assert reverse_sequence_recursion([9, 7, 1]) == [1, 7, 9]
    assert reverse_sequence_recursion((9, 7, 1)) == (1, 7, 9)
    assert reverse_sequence_recursion("rust") == "tsur"


if "__main__" == __name__:
    main()
