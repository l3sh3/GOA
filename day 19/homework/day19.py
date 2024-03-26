#exercise 1
"""Given an array of integers your solution should find the smallest integer."""

def find_smallest_int(arr):
    return min(arr)


#exercise 2
"""Write a function that removes the spaces from the string, then return the resultant string."""

def no_space(x):
    for i in x:
        x = x.replace(" ", "")
    return x


#exercise 3
"""Implement a function which convert the given boolean value into its string representation."""

def boolean_to_string(b):
    return str(b)


#exercise 4
"""Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. 
If the array does not contain any numbers then you should return 0."""

def sum_array(a):
    sum = 0
    for i in a:
        sum += i
    return sum


#exercise 5
"""Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them."""

def abbrev_name(name):
    index = 0
    for i in name:
        index += 1
        if i == " ":
            break
    return name[0].upper()+"."+name[index].upper()


#exercise 6
"""Given an array of integers, return a new array with each value doubled."""

def maps(a):
    new_arr = []
    for i in a:
        i *= 2
        new_arr.append(i)
    return new_arr


#exercise 7
"""Write a function which converts the input string to uppercase."""

def make_upper_case(s):
    return s.upper()


#exercise 8
"""Write a function which calculates the average of the numbers in a given list.
Note: Empty arrays should return 0."""

def find_average(numbers):
    sum = 0
    for i in numbers:
        sum += i
    if len(numbers) == 0:
        return 0
    else:
        result = sum / len(numbers)
        return result
    

#exercise 9
"""Write function bmi that calculates body mass index (bmi = weight / height2).
if bmi <= 18.5 return "Underweight"
if bmi <= 25.0 return "Normal"
if bmi <= 30.0 return "Overweight"
if bmi > 30 return "Obese"""

def bmi(weight, height):
    body_mass_index = weight / (height * height)
    if body_mass_index <= 18.5:
        return "Underweight"
    elif body_mass_index <= 25.0:
        return "Normal"
    elif body_mass_index <= 30.0:
        return "Overweight"
    elif body_mass_index > 30:
        return "Obese"
