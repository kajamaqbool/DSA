def Factorial(n):
    if n == 0:
        return 1
    return n * Factorial(n-1)

if __name__ == "__main__":
    n = 5
    print(Factorial(n))