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

    maria_wins = 0
    ben_wins = 0
    n = max(nums)

    for _ in range(x):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for num in nums:
            if is_prime[num]:
                for i in range(num, n + 1, num):
                    is_prime[i] = False
                maria_wins += 1
                break
        else:
            ben_wins += 1
            continue

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
