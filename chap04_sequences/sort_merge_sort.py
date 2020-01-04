from pylist import IntList


def merge(seq: IntList, start: int, mid: int, stop: int) -> None:
    lst: IntList = []

    # Just another name for the { start, mid }, => two sub-lists
    i: int = start
    j: int = mid

    # First, the reason we can do this is that the list we get here is
    # ALWAYS divided into a very small one (previously calculated `mid`).
    # Second, the logics in this `while` is pretty simple, only two parts,
    # 1) the `while condition`: tightening the indexes (changes happend
    # inside) 2) the `if condition` with increments: smaller one will be
    # added to the leftmost part.
    while i < mid and j < stop:
        # What you get from this `while` is: "the small partion (usually 2)
        # will be sorted (PARTIALLY) in a pretty simple way".
        if seq[i] < seq[j]:
            lst.append(seq[i])
            i += 1
        else:
            # This part (I mean `j`) isn't actually that useful considering
            # the current recursion (e.g. we got a seq[2] = 9)
            lst.append(seq[j])
            j += 1

    # Takes care of finishing up whichever the sublist had the left-over
    # elements (since you were limited by a `j < stop` in the prev loop).
    while i < mid:
        lst.append(seq[i])
        i += 1

    # Copy the sorted result to the original sequence!
    for i in range(len(lst)):
        seq[start + i] = lst[i]

    # Now the CURRENT recursion returned, onward to the next line of
    # the 'merge_sort_recursively' of '...recur...(seq, mid, stop)'.


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
