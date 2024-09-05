#!/usr/bin/python3
"""
Prime Game - Maria and Ben are playing a game of prime numbers
"""


def sieve_of_eratosthenes(n):
    """Generate a list of booleans representing prime numbers up to n"""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def count_prime_multiples(n, primes):
    """Count the number of prime multiples up to n"""
    prime_count = 0
    for i in range(2, n + 1):
        if primes[i]:
            prime_count += 1
    return prime_count


def isWinner(x, nums):
    """
    Determine who is the winner after x rounds of prime game.
    Maria goes first, and both play optimally.
    
    Args:
    x (int): Number of rounds
    nums (list): List of numbers (n) for each round
    
    Returns:
    str: Name of the player with the most wins or None
    """
    if not nums or x < 1:
        return None
    
    # Precompute primes up to the maximum value in nums
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        prime_count = count_prime_multiples(n, primes)
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
