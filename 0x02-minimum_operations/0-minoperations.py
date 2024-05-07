#!/usr/bin/python3
"""
A python function that calculate the minimum amount of operation
needed to get n number of 'H's in a file
"""


def minOperations(n) -> int:
    """A python function that calculate the minimum amount of operation
    needed to get n number of 'H's in a file
    Args:
        n(int): the number of 'H's needed
    Returns:
        The total operations needed
    """
    if n < 2:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
