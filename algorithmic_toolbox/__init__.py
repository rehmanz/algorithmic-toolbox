__version__ = "0.1.0"

"""Return max pairwise product

"""
def max_pairwise_product(numbers):
    sorted_numbers = sorted(map(int, numbers.split()))
    n = len(sorted_numbers)
    return sorted_numbers[n-1] * sorted_numbers[n-2]