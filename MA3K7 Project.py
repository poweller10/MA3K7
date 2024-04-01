import numpy as np

def f(n_terms):
    sum = 0.0
    for n in range(0, n_terms + 1):
        term = (-1)**(n) * 1 / (2 * n + 1)  # Adjusted power to match the series starting at n=1
        sum += term
    return sum

n_terms = 10000000
calculation = f(n_terms)
print("Value of f(x) = ", calculation)
print("Value of pi/4 = ", np.pi/4)