"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

# def sum_of_multiples(ceiling):
#     """Straight forward implementation"""
#     rolling_sum = 0

#     for i in range(ceiling):
#         if (i % 3 == 0) or (i % 5 == 0):
#             rolling_sum += i

#     return rolling_sum

def sum_of_multiples(ceiling):
    """
    The sum of multiples of three under a number (e.g. 10) can be factored out
    like so:

    3 + 6 + 9 = (3 * 1) + (3 * 2) + (3 * 3)
              = 3 * (1 + 2 + 3)
    """
    def g(multiple, ceiling):
        # subtract one because you want < not <= to ceiling
        num_of_multiples = (ceiling-1) // multiple

        # one optimization: sum of integers less than n can be expressed
        # as n = n(n+1)/2
        return multiple * num_of_multiples * (num_of_multiples + 1) // 2

    # g(15) is to remove duplicates since 15 = 3 * 5
    return g(3, ceiling) + g(5, ceiling) - g(15, ceiling)

if __name__ == '__main__':
    print(sum_of_multiples(1000))
