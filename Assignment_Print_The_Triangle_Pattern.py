# Lower Triangle with '*'

def lower_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("\r")

# Upper Triangle 
def upper_triangle(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("\r")

# Pyramid
def pyramid(n):
    for i in range(1, n + 1):
        
        for j in range(n - i):
            print(" ", end="")
        for k in range(1, 2*i):
            print("*", end="")
        print("\r")


n=4
pyramid(n)