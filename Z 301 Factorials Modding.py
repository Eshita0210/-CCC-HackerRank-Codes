def factorial_mod(a, b, m):
    # Calculate (b+1) * (b+2) * ... * a modulo m
    prod = 1
    for i in range(b+1, a+1):
        prod = (prod * i) % m
    
    return prod % m

# Reading input
a, b, m = map(int, input().split())

# Calculating (a! / b!) % m
result = factorial_mod(a, b, m)

# Printing output
print(result)
