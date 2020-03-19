#!/usr/bin/python

import sys


def making_change(amount, denominations, cache=None):
    # Forces cache to become a list full of zero values
    if cache is None:
        cache = [1] + [0]*amount

    # BASE CASE
    if amount <= 0:
        return 1

    # Need to loop through the amount of coins that are in
    # the list of denominations
    for coins in denominations:
        # I need to take the index (coin) and add the amount of one
        for coin in range(coins, amount + 1):
            # Return the cache option on whatever is the difference
            # between the single coin and the coins
            cache[coin] += cache[coin - coins]

    return cache[amount]

denominations = [1, 5, 10, 25, 50]
print(making_change(10, denominations))

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format
              (ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
