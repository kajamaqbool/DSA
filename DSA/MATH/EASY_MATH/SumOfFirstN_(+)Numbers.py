#[Naive Approach] Using Loop - O(n) Time and O(1) Space
"""
def findSum(n):
    sum = 0
    i = 1
    
    # Iterating over all the numbers between 1 to n
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum
if __name__ == "__main__":
    n = 5
    print(findSum(n))
"""

#[Alternative Approach] Using Recursion -O(n) and O(n) Space
"""
def findSum(n):
    # base condition
    if n == 1:
        return 1
    return n + findSum(n - 1)

if __name__ == "__main__":
    n = 5
    print(findSum(n))
"""

#[Expected Approach] Formula Based Method- O(1) Time and O(1) Space

def findSum(n):
    # Using mathematical formula to compute
    # sum of first n natural numbers
    return n * (n + 1) // 2
if __name__ == "__main__":
    n = 5
    print(findSum(n))
