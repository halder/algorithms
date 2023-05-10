import sys
from math import log

a, b, d = [int(arg) for arg in sys.argv[1:]]

if a == b ** d:
    case = "log(n)"
    if d == 1:
        case = f"n * {case}"
    if d > 1:
        case = f"n^{d} * {case}"

elif a < b ** d:
    case_2 = {
        "0": "1",
        "1": "n",
        "d": f"n^{d}"
    }

    key = str(d) if d < 2 else "d"
    case = case_2[key]

else:
    case = f"n^{round(log(a, b), 2)}"

print(f"The running time of your algorithm is O({case}).")