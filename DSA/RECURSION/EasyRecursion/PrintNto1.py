def PrintNTo1(n):
    
    if n == 0:
        return
    
    print(n, end=" ")
    
    PrintNTo1(n-1)
    
if __name__ == "__main__":
    n = 10
    PrintNTo1(n)