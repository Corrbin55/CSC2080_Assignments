# CSC 2080 -  Homework Assignment #1

# Problem 1: Chapter #1 - Programming Exercises #1 (a) to (k)
def problem_1():
    # a) Print a string with punctuation
    print("Hello, world!")  # Outputs: Hello, world!

    # b) Print a string with space-separated words
    print("Hello", "world!")  # Outputs: Hello world!

    # c) Print an integer
    print(3)  # Outputs: 3

    # d) Print a float
    print(3.0)  # Outputs: 3.0

    # e) Print the sum of two integers
    print(2 + 3)  # Outputs: 5

    # f) Print the sum of two floats
    print(2.0 + 3.0)  # Outputs: 5.0

    # g) Print a string that looks like an equation
    print("2 + 3")  # Outputs: 2 + 3 (as a string)

    # h) Print a string and a calculated result
    print("2 + 3 =", 2 + 3)  # Outputs: 2 + 3 = 5

    # i) Print a multiplication result
    print(2 * 3)  # Outputs: 6

    # j) Print an exponentiation result
    print(2 ** 3)  # Outputs: 8

    # k) Print a division result
    print(7 / 3)  # Outputs: 2.3333333333333335

    # l) Print a floor division result
    print(7 // 3)  # Outputs: 2

# Problem 5: Chapter #1 - Modify the chaos program
def problem_5():
    print("This program illustrates a chaotic function.")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))

    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)

# Problem 10: Chapter #2 - Kilometers to Miles Conversion
def problem_10():
    print("This program converts kilometers to miles.")
    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometers * 0.62
    print(f"{kilometers} kilometers is approximately {miles} miles.")

# Exercise 5 from How to Think Like a Computer Scientist
def exercise_5():
    print("This program converts Celsius to Fahrenheit.")
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius} Celsius is {fahrenheit} Fahrenheit.")

# Call each function for testing
if __name__ == "__main__":
    print("Running Problem 1:")
    problem_1()
    print("\nRunning Problem 5:")
    problem_5()
    print("\nRunning Problem 10:")
    problem_10()
    print("\nRunning Exercise 5:")
    exercise_5()
