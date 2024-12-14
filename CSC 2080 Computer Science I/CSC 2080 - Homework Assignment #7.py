# CSC 2080 - Homework Assignment #7

# Discussion Question 1
# Part (a)
# Comparing definite loop vs. indefinite loop
definite_loop_example = sum([i for i in range(10)]) # A loop with a fixed range
indefinite_loop_example = 0
while indefinite_loop_example < 10:
    indefinite_loop_example += 1  # A loop that depends on a condition

# Part (b)
# Comparing for loop vs. while loop
for_loop_example = [i ** 2 for i in range(5)]  # "for" loop
while_loop_example = []
count = 0
while count < 5:  # "while" loop
    while_loop_example.append(count ** 2)
    count += 1

# Part (c)
# Comparing interactive loop vs. sentinel loop
interactive_loop = []
while True:
    user_input = input("Enter a value or type 'exit' to stop: ")
    if user_input.lower() == 'exit':
        break
    interactive_loop.append(user_input)

sentinel_loop = []
user_input = input("Enter numbers; type '-1' to stop: ")
while user_input != '-1':
    sentinel_loop.append(int(user_input))
    user_input = input("Enter another number: ")

# Part (d)
# Comparing sentinel loop vs. end-of-file loop
# (Explanation goes here based on context)

# Discussion Question 2
# Truth Tables
truth_table = [
    {'P': P, 'Q': Q, 'R': R, 'not(P and Q)': not (P and Q), '(not P) and Q': (not P) and Q, '(P and Q) or R': (P and Q) or R}
    for P in [True, False] for Q in [True, False] for R in [True, False]
]

# Discussion Question 3 (a, c)
# (a) Sum of the first n counting numbers
n = int(input("Enter n: "))
sum_n = 0
for i in range(1, n + 1):
    sum_n += i
print("Sum of first n numbers:", sum_n)

# (c) Sum of a series of numbers entered by the user until the value 999 is entered
sum_series = 0
while True:
    user_input = int(input("Enter a number (999 to stop): "))
    if user_input == 999:
        break
    sum_series += user_input
print("Sum of series:", sum_series)

# Programming Exercise 1
# Fibonacci sequence
n = int(input("Enter n for Fibonacci sequence: "))
def fibonacci(n):
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b if n > 1 else a

print("Fibonacci number:", fibonacci(n))

# Programming Exercise 4
# Syracuse (Collatz) sequence
x = int(input("Enter a starting value for the Syracuse sequence: "))
while x != 1:
    print(x, end=" -> ")
    if x % 2 == 0:
        x //= 2
    else:
        x = 3 * x + 1
print(1)

# Git repository link will be added once uploaded to GitHub.
