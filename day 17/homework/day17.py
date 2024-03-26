#exercise 1
"""Write a function that takes a list of numbers as input and returns the sum of all the numbers in the list."""

def sum_of_members(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

print(sum_of_members([1, 2, 3]))


#exercise 2
"""Write a function that takes a list of strings as input and returns a new list containing
 only the strings that have a length greater than 5."""

def length_mesure(arr_of_strings):
    new_arr = []
    for word in arr_of_strings:
        if len(word) > 5:
            new_arr.append(word)
    return new_arr

print(length_mesure(["crocodile", "fox", "giraffe"]))


#exercise 3
"""Write a function that takes a list of numbers as input and returns a
new list containing only the even numbers from the original list."""

def number_check(arr_of_nums):
    new_nums_array = []
    for i in arr_of_nums:
        if i % 2 == 0:
            new_nums_array.append(i)
    return new_nums_array

print(number_check([1, 2, 3, 4]))


#exercise 4
"""Write a function that takes a list of numbers as input and returns the largest number in the list."""

def largest_num(array):
        return max(array)

print(largest_num([1, 2, 3, 4]))


#exercise 5
"""Write a function that takes a list of strings as input and returns a new list containing only the 
strings that start with the letter 'a'."""

def first_letter(array_of_strings):
    new_strings_array = []
    for i in array_of_strings:
        if i[0] == "a":
            new_strings_array.append(i)
    return new_strings_array

print(first_letter(["bird", "animal", "human", "amphibian"]))


#exercise 6
"""Write a function that takes a list of numbers as input and returns a new list containing the square of each number."""

def square_of_number(strings_array):
    squared_list = []
    for i in strings_array:
        i **= 2
        squared_list.append(i)
    return squared_list

print(square_of_number([1, 2, 3, 4]))


#exercise 7
"""Write a function that takes a list of strings as input and returns a new list containing the lengths of each string."""

def length_of_strings(list_of_strings):
    new_list_of_strings = []
    for i in list_of_strings:
        new_list_of_strings.append(len(i))
    return new_list_of_strings

print(length_of_strings(["giraffe", "lion", "fox"]))


#exercise 8
"""Write a function that takes a list of numbers as input and returns the sum of all the numbers 
that are greater than 10. """

def sum_of_nums(nums_list):
    sum_of_numbers = 0
    for i in nums_list:
        if i > 10:
            sum_of_numbers += i
    return sum_of_numbers

print(sum_of_nums([5, 8, 11, 20]))