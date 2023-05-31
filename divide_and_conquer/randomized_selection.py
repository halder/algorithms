import random

def rand_select(array, i):
    """
    RandSelect i-th order statistic of array.
    Not inplace, uses additional memory.
    O(n) time complexity.
    """
    if len(array) == 1:
        return array[0]
    else:
        r = random.randint(0, len(array)-1)
        pivot = array[r]

        left = [n for n in array if n < pivot]
        right = [n for n in array if n > pivot]

        if len(left) == i - 1:
            return pivot
        elif len(left) < i - 1:
            # ith order statistic is in right side
            return rand_select(right, i - len(left) - 1)
        else:
            # ith order statistic is in left side
            return rand_select(left, i)

if __name__ == "__main__":
    # test
    cases = (
        [5,2,6,1,7,3,9],
        [3,1,9,4,7,12,5,2],
        [4,2,7,1,9,5,2]
    )

    for case in cases:
        print(sorted(case), rand_select(case, 3))




