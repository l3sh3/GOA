#exercise 1

# def grow(arr):
#     multiply = 1
#     for i in arr:
#         multiply *= i
#     return multiply

# print(grow([1, 2, 3, 4]))


#exercise 2

# def bmi(weight, height):
#     body_mass_index = weight / (height * height)
#     if body_mass_index <= 18.5:
#         return "Underweight"
#     elif body_mass_index <= 25.0:
#         return "Normal"
#     elif body_mass_index <= 30.0:
#         return "Overweight"
#     elif body_mass_index > 30:
#         return "Obese"
    
# print(bmi(50, 1.80))


#exercise 3

# def get_count(sentence):
#     vowels = 0
#     for i in sentence:
#         if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#             vowels += 1
#     return vowels


#exercise 4

# def square_digits(num):
#     result = ""
#     num = str(num)
#     for i in num:
#         i = int(i)
#         i *= i
#         i = str(i)
#         result += i
#     result = int(result)
#     return result

# print(square_digits(3212))


#exercise 5
