def PrintOneToN(n):
    
    if n == 0:
        return
    
    PrintOneToN(n-1)
    print(n, end=" ")
    
if __name__ == "__main__":
    n = 10
    PrintOneToN(n)