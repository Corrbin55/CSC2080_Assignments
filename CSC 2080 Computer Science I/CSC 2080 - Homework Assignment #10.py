# Homework Assignment #10
# Chapter 11

# Problem 1: Discussion Question 1 (pg 411-412)
# Given the initial statements
s1 = [2, 1, 4, 3]
s2 = ['c', 'a', 'b']

# Results of evaluating the following sequence expressions:
# a) s1 + s2
# Concatenate both lists
s1_plus_s2 = s1 + s2  # [2, 1, 4, 3, 'c', 'a', 'b']

# b) 3 * s1 + 2 * s2
# Repeat s1 three times and s2 two times
repeat_s1_s2 = 3 * s1 + 2 * s2  # [2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 'c', 'a', 'b', 'c', 'a', 'b']

# c) s1[1]
# Access the element at index 1 of s1
element_s1_1 = s1[1]  # 1

# d) s1[1:3]
# Slice s1 from index 1 to index 3 (exclusive)
slice_s1_1_3 = s1[1:3]  # [1, 4]

# e) s1 + s2[-1]
# Add last element of s2 to s1
s1_plus_last_s2 = s1 + [s2[-1]]  # [2, 1, 4, 3, 'b']

# Problem 2: Programming Exercise 6 (pg 413)
# Function to shuffle a list
import random

def shuffle(myList):
    random.shuffle(myList)
    return myList

# Test shuffle function
example_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle(example_list)

# Problem 3: Programming Exercise 8 (pg 413)
# Function to remove duplicates from a list
def removeDuplicates(someList):
    return list(set(someList))

# Test removeDuplicates function
example_list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_list = removeDuplicates(example_list_with_duplicates)


