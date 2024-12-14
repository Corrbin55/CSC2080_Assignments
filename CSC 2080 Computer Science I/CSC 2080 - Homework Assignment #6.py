# CSC 2080 - Homework Assignment #6

# (14 pts.) Chapter #7 - Discussion Problem #2
# Discussion: How is exception handling using try/except similar to and different from decision structures like if/else?
#
# Similarities:
# - Both try/except and if/else are used to handle specific cases in the program.
# - They allow the program to handle unusual or "exceptional" conditions gracefully.
#
# Differences:
# - try/except is used to handle run-time errors or exceptions that occur during execution, whereas if/else is used to control the flow of the program based on conditions known before execution.
# - With try/except, the program jumps to the except block only if an exception is raised, while if/else explicitly evaluates a condition to determine the flow.


# (14 pts.) Chapter #7 - Programming Exercise #3: Grading System

# Program to calculate grades using decision structures.
def calculate_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

# Main program
try:
    score = float(input("Enter the exam score (0-100): "))
    if 0 <= score <= 100:
        grade = calculate_grade(score)
        print(f"The grade is: {grade}")
    else:
        print("Error: Score must be between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")


# (14 pts.) Chapter #7 - Programming Exercise #7: Babysitting Bill Calculator

def calculate_babysitting_bill(start_time, end_time):
    total_cost = 0
    current_time = start_time
    while current_time < end_time:
        if current_time < 21.0:  # Before 9 PM
            total_cost += 2.50
        else:  # After 9 PM
            total_cost += 1.75
        current_time += 1
    return total_cost

# Main program
try:
    start = float(input("Enter the starting time (e.g., 18.5 for 6:30 PM): "))
    end = float(input("Enter the ending time (e.g., 22.0 for 10:00 PM): "))
    if start < end:
        bill = calculate_babysitting_bill(start, end)
        print(f"The total babysitting bill is: ${bill:.2f}")
    else:
        print("Error: Ending time must be later than starting time.")
except ValueError:
    print("Invalid input. Please enter numeric values for times.")


# (14 pts.) Chapter #7 - Programming Exercise #8: Eligibility Check

def check_eligibility(age, citizenship_years):
    senate_eligible = age >= 30 and citizenship_years >= 9
    house_eligible = age >= 25 and citizenship_years >= 7
    return senate_eligible, house_eligible

# Main program
try:
    age = int(input("Enter your age: "))
    citizenship_years = int(input("Enter your years of US citizenship: "))

    senate, house = check_eligibility(age, citizenship_years)

    print(f"Eligibility for Senate: {'Yes' if senate else 'No'}")
    print(f"Eligibility for House: {'Yes' if house else 'No'}")
except ValueError:
    print("Invalid input. Please enter whole numbers for age and citizenship years.")


# (14 pts.) Modify a previous program with exception handling
# Modification: Adding exception handling to Chapter 6 Programming Exercise #12 (Sum of a List)
def sum_list(nums):
    return sum(nums)

# Main program
try:
    nums = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))
    total = sum_list(nums)
    print(f"The sum of the list is: {total}")
except ValueError:
    print("Error: Ensure all inputs are numeric values.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Explanation of runtime errors handled:
# 1. ValueError: Occurs if the user enters non-numeric values. The program informs the user to enter valid numbers.
# 2. General Exception: Catches unexpected errors to prevent the program from crashing, providing a fallback error message.
