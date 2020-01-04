from pylist import IntList

from sort_selection_sort import selection_sort
from sort_merge_sort import merge_sort
from sort_quick_sort import *

arr_sel: IntList = [19, 4, 9, 20, 10]
arr_mer: IntList = [19, 4, 9, 20, 10]
arr_quk: IntList = [19, 4, 9, 20, 10]

# selection_sort(seq=arr_sel)
# assert arr_sel == [4, 9, 10, 19,20]

# merge_sort(seq=arr_mer)
# assert arr_mer == [4, 9, 10, 19, 20]

merge_sort(seq=arr_quk)
assert arr_quk == [4, 9, 10, 19, 20]
