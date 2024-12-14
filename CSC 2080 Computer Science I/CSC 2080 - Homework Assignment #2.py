# CSC 2080 - Homework Assignment #2

# Chapter #2 - Discussion Problem #4(a,b,c,d)
print("Chapter #2 - Discussion Problem #4")
# (a) Squares of numbers from 0 to 4
print("(a) Squares of numbers from 0 to 4:")
for i in range(5):
    print(i * i)

# (b) Print elements of the list with a space
print("\n(b) Elements of the list [3,1,4,1,5]:")
for d in [3, 1, 4, 1, 5]:
    print(d, end=" ")
print()  # For newline after the loop

# (c) Print "Hello" 4 times
print("\n(c) Print 'Hello' 4 times:")
for i in range(4):
    print("Hello")

# (d) Print i and 2^i for i in range(5)
print("\n(d) Values of i and 2^i for i in range(5):")
for i in range(5):
    print(i, 2 ** i)

# Chapter #3 - Discussion Problem #1(a,c,e)
print("\nChapter #3 - Discussion Problem #1")
# (a) Evaluate 4.0 / 10.0 + 3.5 * 2
print("(a) 4.0 / 10.0 + 3.5 * 2 =", 4.0 / 10.0 + 3.5 * 2)

# (c) Evaluate abs(4 - 20 // 3) ** 3
print("(c) abs(4 - 20 // 3) ** 3 =", abs(4 - 20 // 3) ** 3)

# (e) Evaluate 3 * 10 // 3 + 10 % 3
print("(e) 3 * 10 // 3 + 10 % 3 =", 3 * 10 // 3 + 10 % 3)

# Chapter #3 - Discussion Problem #2(b,c)
print("\nChapter #3 - Discussion Problem #2")
import math  # Required for mathematical functions

# (b) Translate 4πr^2
r = 5  # Example radius
print(f"(b) 4πr^2 where r = {r}:", 4 * math.pi * r ** 2)

# (c) Sum of n(n-1)/2
n = 6  # Example value of n
print(f"(c) n(n-1)/2 where n = {n}:", n * (n - 1) / 2)

# Chapter #3 - Discussion Problem #4(b,c)
print("\nChapter #3 - Discussion Problem #4")
# (b) Print i and i^3 for odd numbers in [1, 3, 5, 7, 9]
print("(b) Cubes of odd numbers in [1, 3, 5, 7, 9]:")
for i in [1, 3, 5, 7, 9]:
    print(i, ":", i ** 3)
print("Last i =", i)

# (c) Print j and x+y for range(0, y, x) where x=2, y=10
print("\n(c) Values of j and x+y where x=2, y=10:")
x, y = 2, 10
for j in range(0, y, x):
    print(j, end=" ")
    print(x + y)
print("done")

# Chapter #3 - Programming Exercise #6
print("\nChapter #3 - Programming Exercise #6")
# Slope of a line through two points (x1, y1) and (x2, y2)
x1, y1 = 1, 2  # Example point 1
x2, y2 = 4, 6  # Example point 2
slope = (y2 - y1) / (x2 - x1)
print(f"The slope of the line through ({x1}, {y1}) and ({x2}, {y2}) is {slope}")

# Chapter #3 - Programming Exercise #7
print("\nChapter #3 - Programming Exercise #7")
# Distance between two points (x1, y1) and (x2, y2)
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance}")
