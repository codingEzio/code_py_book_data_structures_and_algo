from pylist import IntList

from sort_selection_sort import selection_sort

arr_sel: IntList = [19, 4, 9, 20, 10]

selection_sort(seq=arr_sel)
assert arr_sel == [4, 9, 10, 19, 20]
