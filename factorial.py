

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def fadtorial(n):
    if n == 1:
        return 1
    return n + fadtorial(n - 1)

print(factorial(4))
print(fadtorial(4))