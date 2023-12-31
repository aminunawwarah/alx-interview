#!/usr/bin/python3

"""
    The method determines the number of minimum operations given n characters
"""


def minOperations(n):
    """
        The method above calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
        args: n: The number of characters to be displayed
        return:
               number of min operations
    """

    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
