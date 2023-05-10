def karatsuba(x, y):
    """
    Karatsuba algorithm for integer multiplication.
    See: https://en.wikipedia.org/wiki/Karatsuba_algorithm

    Assumes x, y to be n-digit numbers.
    """
    n_max = max(len(str(x)), len(str(y)))
    n = n_max + n_max % 2
    B = 10 ** (n // 2)

    # base case
    if x < 10 or y < 10:
        return x * y

    else:
        a = x // B
        b = x % B
        c = y // B
        d = y % B
        
        t1 = karatsuba(a, c)
        t3 = karatsuba(b, d)
        t2 = karatsuba((a + b), (c + d)) - t1 - t3

        return (10 ** n * t1 + B * (t2) + t3)

if __name__ == "__main__":
    # test
    pairs = [
        (123, 952),
        (6233467, 7623242),
        (1212, 1264),
        (9411, 5228),
        (63, 91)
    ]

    for pair in pairs:
        p1, p2 = pair
        print(karatsuba(p1, p2) == (p1 * p2))