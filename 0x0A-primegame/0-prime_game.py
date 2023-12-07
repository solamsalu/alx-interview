#!/usr/bin/python3
"""Solution to prime game problem
"""


def isWinner(x, nums):
    """Returns name of the player that won the most rounds.
    """
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def getWinner(n):
        if n == 1 or (n > 2 and n % 2 == 0):
            return "Ben"
        else:
            return "Maria"

    winners = [getWinner(n) for n in nums]

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
