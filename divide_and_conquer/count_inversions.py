def count_inversions(array):
    """
    Count inversions. Leverages merge sort algorithm.

    An inversion is a pair of unsorted elements (i, j) in the input list.
    E.g. [1, 3, 5, 2, 4, 6] has 3 inversions,
    namely pairs (3, 2), (5, 2), (5, 4).
    """
    # base case
    if len(array) == 1:
        return array, 0
    
    else:
        n = len(array)
        left, right = array[:n//2], array[n//2:]

        left_tree, x = count_inversions(left)
        right_tree, y = count_inversions(right)
        sorted_array, z = merge_and_count_inversions(left_tree, right_tree)
        
        return sorted_array, x + y + z


def merge_and_count_inversions(left, right):
    """
    Merge sort core routine. Additionally count inversions.

    Since we are sorting the individual lists in ascending order,
    whenever we put an item from the `right` list into the `merged` list,
    this item is "missing" in the "correctly ordered" `left` list.
    
    Whenever the above happens, we automatically identify & count 1 inversion.
    """
    l, r = len(left), len(right)
    merged = []
    inversions = 0
    i, j = 0, 0

    for _ in range(l + r):

        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            inversions += len(left[i:])
            merged.append(right[j])
            j += 1

        # if we reach the end of either `left` or `right`
        # we can just dump the remainder of the other list into `merged`
        # since all elements left have to be in ascending order
        if i == l:
            merged.extend(right[j:])
            break
        if j == r:
            merged.extend(left[i:])
            break

    return merged, inversions

if __name__ == "__main__":
    # test
    sequences = (
        [3,1,2],
        [3,1,9,3,2,1],
        [6,5,4,3,2,1],
        [1,3,5,2,4,6],
        [3,3,1,9,4,7,12,5,2],
        [3,3,1,2,2,2,0,2,2,2,2]
    )

    for sequence in sequences:
        print(f"{sequence=}: {sequence[1]} inversions")