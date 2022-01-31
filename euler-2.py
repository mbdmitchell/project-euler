# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.
# ---------------------

def sum_of_even_fib(max_num):
    a, b = 1, 1 # first two terms of series
    total = 0
    while b < max_num: # adds the even-valued terms while max_num hasn't been reached
        if b % 2 == 0:
            total += b
        a, b = b, a + b # reassigns a and b
    return total


print(sum_of_even_fib(4000000))
