# Ref: https://github.com/keon/algorithms/blob/master/algorithms/sort/heap_sort.py


def heap_sort(arr, simulation=False):
    """Heap sort that uses a max heap to sort an array in ascending order.
    """
    iteration = 0
    if simulation is True:
        print(f"Iteration {iteration}:", *arr)

    for idx in range(len(arr) - 1, 0, -1):
        iteration = _heapify(arr, idx, simulation, iteration)

    if simulation:
        iteration += 1
        print(f"Iteration {iteration}:", *arr)

    return arr


def _heapify(arr, end, simulation, iteration):
    last_parent = (end - 1) // 2

    # Iterate from last parent to first
    for parent in range(last_parent, -1, -1):
        current_parent = parent

        while current_parent <= last_parent:
            child = current_parent * 2 + 1

            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1

            if arr[child] > arr[current_parent]:
                arr[current_parent], arr[child] = (
                    arr[child],
                    arr[current_parent],
                )
                current_parent = child

                if simulation is True:
                    iteration += 1
                    print(f"Iteration {iteration}:", *arr)
            else:
                break

    arr[0], arr[end] = arr[end], arr[0]
    return iteration


def main() -> None:
    arr = [9, 1, 3]

    assert heap_sort(arr) == [1, 3, 9]
    assert heap_sort(arr, simulation=True) is not None


if "__main__" == __name__:
    main()
