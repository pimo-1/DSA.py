# A simple example of a quadratic big O notation function in Python
def quadratic_big_o(n):
    for i in range(n):
        for j in range(n):
            # Perform a constant time operation
            print(i, j)

# Notice we only take care of dominant terms 
def quadratic1(m):
    for j in range(m):
        for k in range(m):
            # Perform a constant time operation
            print(j, k) 

def proportional(k):
    for k in range(k):
            # Perform a constant time operation
            print(k)  
            
# The time complexity of the function `quadratic_big_o(n)` is O(n^2) because there are two nested loops, each running n times.      