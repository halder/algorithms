# Master Method for running time analysis of algorithms

## Base case
$$
\begin{equation}
    T(n) \leq c
\end{equation}
$$

where $c$ = *constant* for all *sufficiently small* $n$.

## Non-base cases
Outside the base case, the running time $T$ based on the size of the input $n$ is bounded by the following equation:

$$
\begin{equation}
    T(n) \leq aT(\frac{n}{b}) + O(n^d)
\end{equation}
$$

where:
- $a$ is the number of recursive calls ($\geq 1$)
    + *(= number of subproblems)*
- $b$ is the input size shrinkage factor ($> 1$)
    + *(= size of subproblems relative to input)*
- $d$ is the exponent in running time outside of recursive calls ($\geq 0$)
    + *(= work done outside of recursion; "combine work")*
- $a$, $b$, $c$ are **constant** and independent of $n$

In the non-base case, the running time complexity is defined as:

$$
\begin{equation}
    T(n)=
    \begin{cases}
        O(n^d\text{log}n),      & \text{if} & a = b^d   & \text{Case 1} \\
        O(n^d)                  & \text{if} & a < b^d   & \text{Case 2} \\
        O(n^{\text{log}_ba})    & \text{if} & a > b^d   & \text{Case 3}
    \end{cases}
\end{equation}
$$