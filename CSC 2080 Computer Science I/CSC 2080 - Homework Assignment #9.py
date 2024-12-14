# CSC 2080 - Homework Assignment #9

# Problem 1: True/False
# True/False answers
# 1. New objects are created by invoking a constructor. - True
# 2. Functions that live in objects are called instance variables. - False
# 3. The first parameter of a Python method definition is called this. - False
# 4. An object may have only one instance variable. - False
# 5. In data processing, a collection of information about a person or thing is called a file. - False

# Problem 2: Multiple Choice
# 1. What Python reserved word starts a class definition?
# Answer: b) class
# 2. A method definition with four formal parameters is generally called with how many actual parameters?
# Answer: d) it depends
# 3. A method definition is similar to a(n) 
# Answer: d) function definition
# 4. Within a method definition, the instance variable x could be accessed via which expression?
# Answer: b) self.x
# 5. A Python convention for defining methods that are "private" to a class is to begin the method name with
# Answer: c) an underscore (_)

# Problem 3: Discussion Question
# Explanation of instance variables vs regular function variables
# Instance variables belong to the object and are accessed using self, while regular function variables are local to the method
# and are only accessible within that method.

# Problem 4: Sphere Class Definition
import math

class Sphere:
    def __init__(self, radius):
        # Initializes the sphere with a given radius
        self.radius = radius

    def getRadius(self):
        # Returns the radius of the sphere
        return self.radius

    def surfaceArea(self):
        # Calculates the surface area of the sphere using the formula 4 * pi * r^2
        return 4 * math.pi * (self.radius ** 2)

    def volume(self):
        # Calculates the volume of the sphere using the formula (4/3) * pi * r^3
        return (4/3) * math.pi * (self.radius ** 3)

# Example usage of the Sphere class
def sphere_example(radius):
    sphere = Sphere(radius)
    # Returning results instead of printing them
    return sphere.getRadius(), sphere.surfaceArea(), sphere.volume()

# Main function to call Programming Exercise 9
if __name__ == "__main__":
    # Example radius value
    example_radius = 5
    results = sphere_example(example_radius)
    # Example of how to use the results
    print(f"Radius: {results[0]}")
    print(f"Surface Area: {results[1]}")
    print(f"Volume: {results[2]}")
