# all points p_i(x_i, y_i) are distinct
# create two copies using merge_sort:
## sorted by x coordinate
## sorted by y coordinate
# divide sorted lists into left & right

## base case: 2 points -> brute force

#

def closest_pair(input):
    """
    input: list of tuples
    """
    h = len(input) // 2
    
    Sx = sorted(input, key=lambda e: e[0])
    Sy = sorted(input, key=lambda e: e[1])

    Lx, Ly = Sx[:h], Sy[:h]
    Rx, Ry = Sx[h:], Sy[h:]

    # base case
    if len(input) <= 3:
        best = {
            "d": None,
            "pair": None
        }

        for p in input:
            for q in input:
                if q != p:
                    is_best_d = False
                    d = ((q[0] - p[0])**2 + (q[1] - p[1])**2) ** .5

                    if d is None or d < best["d"]:
                        is_best_d = True
                    if is_best_d:
                        best["d"] = d
                        best["pair"] = (p, q)
                    
        return best["pair"] 
    
    else:
        best_left_pair = closest_pair()

closest_pair([(5,3), (1,2), (6,1), (3,4)])

