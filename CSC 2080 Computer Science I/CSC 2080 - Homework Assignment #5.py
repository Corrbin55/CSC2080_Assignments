# CSC 2080 - Homework Assignment #5

# (14 pts.) Chapter 6 - Programming Exercise #1: Old MacDonald

def old_macdonald_verse(animal, sound):
    lyrics = f"""
Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!
And on that farm he had a {animal}, Ee-igh, Ee-igh, Oh!
With a {sound}, {sound} here and a {sound}, {sound} there.
Here a {sound}, there a {sound}, everywhere a {sound}, {sound}.
Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!
    """
    print(lyrics)

# Call the function for five different animals
old_macdonald_verse("cow", "moo")
old_macdonald_verse("duck", "quack")
old_macdonald_verse("pig", "oink")
old_macdonald_verse("dog", "woof")
old_macdonald_verse("cat", "meow")


# (14 pts.) Chapter 3 - Programming Exercise #14: Average Calculation with Function

def get_average(n):
    total = 0
    for _ in range(n):
        num = float(input("Enter a number: "))
        total += num
    return total / n

# Main program
count = int(input("How many numbers will you enter? "))
average = get_average(count)
print(f"The average is {average}")


# (14 pts.) Chapter 4 - Programming Exercise #8: Slope and Distance Calculation
import math

def compute_slope(dx, dy):
    if dx == 0:
        return None  # Undefined slope
    return dy / dx

def compute_distance(dx, dy):
    return math.sqrt(dx**2 + dy**2)

# Main program
x1, y1 = map(float, input("Enter the coordinates of the first point (x1, y1): ").split())
x2, y2 = map(float, input("Enter the coordinates of the second point (x2, y2): ").split())
dx = x2 - x1
dy = y2 - y1

slope = compute_slope(dx, dy)
distance = compute_distance(dx, dy)

print(f"The slope of the line is: {'undefined' if slope is None else slope}")
print(f"The distance between the points is: {distance}")


# (14 pts.) Chapter 6 - Programming Exercise #12: Sum of a List

def sum_list(nums):
    return sum(nums)

# Main program
nums = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))
total = sum_list(nums)
print(f"The sum of the list is: {total}")


# (14 pts.) Get Some Strings: Function Returning a List

def get_some_strings(count):
    strings = []
    for _ in range(count):
        string = input("Enter a string: ")
        strings.append(string)
    return strings

# Main program
n = int(input("How many strings will you enter? "))
user_strings = get_some_strings(n)
print(f"The list of strings is: {user_strings}")
