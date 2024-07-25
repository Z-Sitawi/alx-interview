#!/usr/bin/python3
"""
    Change comes from within
"""


def makeChange(coins, total):
    """
    :param coins: (list) representing a pile of coins of different values
    :param total: (int) A given amount
    :return: the fewest number of coins needed to meet a given amount total
    """
    if total <= 0 or coins == []:
        return 0
    if isinstance(coins, list):
        coins = sorted(coins)
        count = 0
        while total > 0:
            if total > max(coins):
                total -= max(coins)
                count += 1
            else:
                for i in range(len(coins)):
                    if coins[i] > total and coins[i] != coins[0]:
                        total -= coins[i-1]
                        count += 1
                        break

        if total < 0:
            return -1
        else:
            return count
