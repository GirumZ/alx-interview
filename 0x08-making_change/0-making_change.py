#!/usr/bin/python3
""" Making changes withh coins"""


def makeChange(coins, total):
    """ Function that returns the min no of coins needed for a change"""

    if total <= 0:
        return 0

    min_coins = [float('inf')] * (total + 1)
    # zero coins to return for zero total
    min_coins[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            min_coins[amount] = min(
                    min_coins[amount], min_coins[amount - coin] + 1)

    if min_coins[total] != float('inf'):
        return min_coins[total]
    else:
        return -1
