#!/usr/bin/python

import argparse

price_list = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]


def find_max_profit(prices):
    """
    grab the max profit that can be made
    This can't be set to 0 because if the max profit is a
    negative, this will fail set to the opposite
    of whatever is the max of prices
    """
    max_profit = -max(prices)

    # Loop through the prices array and compare the values
    for x in range(len(prices)):
        # Had to add 1 to x so that it would skip the first index
        # and always be one ahead
        for i in range(x + 1, len(prices)):
            if prices[i] - prices[x] > max_profit:
                max_profit = prices[i] - prices[x]

    return max_profit

print(find_max_profit(price_list))

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
            description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='aninteger price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}."
          .format(profit=find_max_profit(args.integers), prices=args.integers))
