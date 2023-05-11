import sys
from math import log

a, b, d = [int(arg) for arg in sys.argv[1:]]

if a == b ** d:
    case = 1
    rt = "log(n)"
    if d == 1:
        rt = f"n * {rt}"
    if d > 1:
        rt = f"n^{d} * {rt}"

elif a < b ** d:
    case = 2
    rt_2 = {
        "0": "1",
        "1": "n",
        "d": f"n^{d}"
    }

    key = str(d) if d < 2 else "d"
    rt = rt_2[key]

else:
    case = 3
    rt = f"n^{round(log(a, b), 2)}"

complexity = f"The running time of your algorithm is O({rt})."
if case == 3:
    complexity = f"{complexity} [O(n^log_{b}({a}))]"

print(f"{complexity}")