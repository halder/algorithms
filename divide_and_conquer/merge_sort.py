def merge_sort(input, asc=True):
    """
    Merge sort algorithm.
    Sort list of integers in ascending (asc) or descending order
    in n*log(n) time complexity.
    """
    # base case
    if len(input) < 2:
        return input
    
    else:
        left, right = split(input)

        left_tree = merge_sort(left, asc=asc)
        right_tree = merge_sort(right, asc=asc)

        return merge(left_tree, right_tree, asc=asc)


def split(input):
    h = len(input) // 2

    return input[:h], input[h:]


def merge(left, right, asc=True):
    """
    Merge sort core routine.
    """
    l, r = len(left), len(right)
    merged = []
    i, j = 0, 0
    
    for _ in range(l + r):
        if asc:
            condition = (left[i] < right[j])
        else:
            condition = (left[i] > right[j])

        if condition:
            merged.append(left[i])
            i += 1
        else:
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

    return merged

if __name__ == "__main__":
    # test
    print(merge_sort([5,2,6,1,7,3,9]))
    print(merge_sort([3,3,1,9,4,7,12,5,2]))
    print(merge_sort([3,3,1,9,4,7,12,5,2], asc=False))
    print(merge_sort([3,3,1,2,2,2,0,2,2,2,2]))