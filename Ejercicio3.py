# Implementación iterativa de la secuencia de Fibonacci
def fibonacci_iterativo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib

# Implementación recursiva de la secuencia de Fibonacci
def fibonacci_recursivo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci_recursivo(n-1)
        fib.append(fib[-1] + fib[-2])
        return fib

# Ejemplo de uso
n = 10
fib_iterativo = fibonacci_iterativo(n)
fib_recursivo = fibonacci_recursivo(n)
print("Secuencia de Fibonacci (iterativo):", fib_iterativo)
print("Secuencia de Fibonacci (recursivo):", fib_recursivo)
