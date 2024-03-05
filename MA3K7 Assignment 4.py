from math import comb

def sum_function(start=12, end=24):
    total_sum = 0
    for n in range(start, end+1):
        total_sum += comb(n, 2*n - 24) * (1/2)**n
    return total_sum

print(sum_function())

