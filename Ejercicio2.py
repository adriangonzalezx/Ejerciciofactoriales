def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

print(recursive_factorial(5))
print(recursive_factorial(10))
