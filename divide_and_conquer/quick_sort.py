import random

def quick_sort(array):
    """
    QuickSort algorithm.
    Sort list of integers in ascending order
    in (on average) n*log(n) time complexity.
    """
    return qsort(array, 0, len(array))


def qsort(array, a, b):
    """
    QuickSort subroutine recursively sorts left and right
    halves subsequently smaller parts of the original array
    (relative to pivot `p`).
    """
    if a < b:
        p = partition(array, a, b)
        
        # sort left & right halves of pivot
        qsort(array, a, p)
        qsort(array, p+1, b)

        return array


def partition(array, p, q):
    """
    Partition subroutine splits array into halves
    less than pivot and greater or equal to pivot.
    """
    r = random.randint(p, q - 1)
    pivot = array[r]

    # move pivot to beginning of array
    array[p], array[r] = pivot, array[p]
    
    i = p + 1
    for j in range(i, q):
        if array[j] < pivot:

            # swap incorrectly ordered elements
            array[i], array[j] = array[j], array[i]

            i += 1
    
    # put pivot in it's proper index
    array[p], array[i-1] = array[i-1], pivot

    return i - 1

if __name__ == "__main__":
    # test
    cases = (
        [5,2,6,1,7,3,9],
        [3,3,1,9,4,7,12,5,2],
        [3,3,1,2,2,2,0,2,2,2,2]
    )

    for case in cases:
        print(quick_sort(case) == sorted(case))