# CSC 2080 - Homework Assignment #4

# (7 pts.) Discussion Problem #1 (c, e, g)
s1 = " spam"
s2 = "ni ! "

# c) s1[1]
print(s1[1])  # Expected: 's'

# e) s1[2] + s2[:2]
print(s1[2] + s2[:2])  # Expected: 'a ni'

# g) s1.upper()
print(s1.upper())  # Expected: ' SPAM'


# (7 pts.) Discussion Problem #2 (a, d, e)
# a) "NI"
print(s2.upper()[:2])  # Expected: 'NI'

# d) "spam"
print(s1.strip())  # Expected: 'spam'

# e) ["sp", "m"]
print([s1[:3], s1[3]])  # Expected: [' sp', 'm']


# (7 pts.) Discussion Problem #3 (b, c, e)
# b) For loop over words in a string
for w in "Now is the winter of our discontent...".split():
    print(w)

# c) For loop splitting "Mississippi" by "i"
for w in "Mississippi".split("i"):
    print(w, end=" ")
print()  # For new line

# e) Increment each character of "secret" by 1
msg = ""
for ch in "secret":
    msg += chr(ord(ch) + 1)
print(msg)  # Expected: 'tfdsfu'


# (7 pts.) Program to produce a single line of output for grades
grades = ""
grades += "F" * 60
grades += "D" * 10
grades += "C" * 10
grades += "B" * 9
grades += "A" * 10
print(f'grades = "{grades}"')


# (14 pts.) Programming Exercise #3
# Accepts an exam score as input and prints the corresponding grade
score = int(input("Enter the exam score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"The grade is {grade}")


# (14 pts.) Programming Exercise #4
# Generates an acronym from a phrase
phrase = input("Enter a phrase: ")
acronym = "".join(word[0] for word in phrase.split()).upper()
print(f"The acronym is {acronym}")


# (14 pts.) Programming Exercise #5
# Calculates the numeric value of a name
name = input("Enter a name: ").lower()
name_value = sum(ord(char) - ord('a') + 1 for char in name if char.isalpha())
print(f"The numeric value of the name is {name_value}")
