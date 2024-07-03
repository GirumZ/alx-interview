#!/usr/bin/python3
""" Determining the winner of a prime game"""


def isWinner(x, nums):
    """ Returns the winner of a prime game
    Args:
        x: number of rounds of game
        nums: list of integers for each round of game
    Returns:
        The winner between Maria and Ben
    """

    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    def sieve(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(n ** 0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
        return is_prime
    n = max(nums) if nums else 0
    is_prime = sieve(n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        p_count = sum(is_prime[2:n + 1])
        if p_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
