# CSC 2080 - Homework Assignment #3

from graphics import *
import math

# Chapter 3 - Programming Exercise #13
# Program to sum a series of numbers entered by the user
n = int(input("How many numbers will you enter? "))
total = 0
for i in range(n):
    number = float(input(f"Enter number {i + 1}: "))
    total += number
print("The total sum is:", total)

# Chapter 3 - Programming Exercise #14
# Program to find the average of a series of numbers entered by the user
n = int(input("How many numbers will you enter? "))
total = 0
for i in range(n):
    number = float(input(f"Enter number {i + 1}: "))
    total += number
average = total / n
print("The average is:", average)

# Chapter 4 - Programming Exercise #2
# Archery target with concentric circles
win = GraphWin("Archery Target", 400, 400)
win.setCoords(0, 0, 400, 400)
center = Point(200, 200)
radius = 40
colors = ["white", "black", "blue", "red", "yellow"]
for i in range(5):
    circle = Circle(center, radius * (5 - i))
    circle.setFill(colors[i])
    circle.draw(win)

# Chapter 4 - Programming Exercise #3
# Draws a simple face
face = Circle(center, 100)
face.setFill("peachpuff")
face.draw(win)

eye1 = Circle(Point(170, 230), 10)
eye1.setFill("black")
eye1.draw(win)

eye2 = Circle(Point(230, 230), 10)
eye2.setFill("black")
eye2.draw(win)

mouth = Oval(Point(170, 170), Point(230, 190))
mouth.setFill("red")
mouth.draw(win)

# Chapter 4 - Programming Exercise #8
# Line segment information
def get_line_info():
    win = GraphWin("Line Segment Info", 400, 400)
    win.setCoords(0, 0, 400, 400)

    # Get two points from user
    p1 = win.getMouse()
    p2 = win.getMouse()

    # Draw line segment
    line = Line(p1, p2)
    line.draw(win)

    # Calculate and display midpoint
    midpoint = Point((p1.getX() + p2.getX()) / 2, (p1.getY() + p2.getY()) / 2)
    midpoint.setFill("cyan")
    midpoint.draw(win)

    # Calculate slope and length
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    length = math.sqrt(dx ** 2 + dy ** 2)
    slope = dy / dx if dx != 0 else "undefined"

    print("Length of the line:", length)
    print("Slope of the line:", slope)
    
    win.getMouse()  # Wait for user to close
    win.close()

get_line_info()
win.getMouse()  # Wait for final close
win.close()
