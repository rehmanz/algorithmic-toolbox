"""Algorithmic toolbox module contains simple algorithms.
"""

__version__ = "0.1.0"


def max_pairwise_product(numbers):
    """Return max pairwise product.

    Keyword arguments:
    numbers -- string containing numbers
    """
    sorted_numbers = sorted(map(int, numbers.split()))
    num_len = len(sorted_numbers)
    return sorted_numbers[num_len - 1] * sorted_numbers[num_len - 2]
