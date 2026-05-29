#[Naive Approach] By Finding the Remainder - O(1) Time and O(1) Space
"""
def isEven(n):

    rem = n%2
    if rem == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input())
    if isEven(n):
        print("Even")
    else:
        print("Odd")
"""

#[Optimized Approach] By Using Bitwise Operator - O(1) Time and O(1) Space

def isEven(n):
    
    # finding remainder of n
    rem = n % 2; 
    if rem == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    n = 15
    if isEven(n):
        print("true")
    else:
        print("false")


