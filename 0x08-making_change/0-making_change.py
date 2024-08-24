#!/usr/bin/python3
"""
Module for makeChange function.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of the values of the coins available.
        total (int): The total amount to achieve.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Returns 0 if total is 0 or less.
             Returns -1 if total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order to prioritize larger denominations
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        # Determine how many of this coin can fit into the remaining total
        num_coins = total // coin
        count += num_coins
        # Reduce the total by the equivalent amount
        total -= num_coins * coin

    # If there's remaining total that couldn't be met
    if total != 0:
        return -1

    return count
