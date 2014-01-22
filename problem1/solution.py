def sum_of_multiples(ceiling):
    rolling_sum = 0
    
    for i in range(ceiling):
        if (i % 3 == 0) or (i % 5 == 0):
            rolling_sum += i
    
    return rolling_sum
    
def sum_of_multiples2(ceiling):
    """
    Sum of multiples of three under 10:
    
    3 + 6 + 9 = (3 * 1) + (3 * 2) + (3 * 3)
              = 3 * (1 + 2 + 3)
    """
    def g(multiple, ceiling):
        # subtract one because you want < not <= to ceiling
        num_of_multiples = (ceiling-1) // multiple
        
        return multiple * sum(i+1 for i in range(num_of_multiples))
    
    return g(3, ceiling) + g(5, ceiling)