# A simple example of a divide and conquer algorithm in Python
def divide_and_conquer(n):
    if n <= 1:
        return n
    else:
        mid = n // 2
        left = divide_and_conquer(mid)
        right = divide_and_conquer(n - mid)
        return left + right
# The time complexity of the function `divide_and_conquer(n)` is O(log n) because the input size is halved at each recursive call, leading to a logarithmic number of calls.    