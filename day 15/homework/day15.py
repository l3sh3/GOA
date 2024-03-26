#exercise 1
"""Write a program that takes asks user for number (use input). If number is even, 
print that number is even. Else print that number is not even,
 also print next even number, for example if input is 15, print 16."""

user_num = int(input("Enter your number :"))
if user_num % 2 == 0:
    print("That number is even!")
else:
    print("This number is not even! ", user_num + 1)


#exercise 2
"""Create a while loop that asks the user to enter a password. 
Keep asking until they enter the correct password "Goa best". 
Also print the count of incorrect passwords."""

password = "Goa best"
users_input = input("Enter your password :")
try_count = 1
while users_input != password:
    users_input = input("Enter your password :")
    try_count += 1
    print("You tried", try_count, "times!")

if try_count == 1:
    print("You tried 1 time")


#exercise 3
"""Write an algorithm that takes a string as input and returns 
True if first character of that string is "G"."""

user_input = input("Enter your word :")
if user_input[0] == "G":
    print("True")


#exercise 4
"""Ask user for five names (use input five times). Add all of them in one 
list and print only first three names."""

names_list = []
for i in range(5):
    user_names = input("Enter name :")
    names_list.append(user_names)

print(names_list[:3])


#exercise 5
"""Write an algorithm that checks if a given number is prime or not 
(prime number has only two divisors) Use a for loop for this task."""

number1 = int(input("Enter your number :"))
count_of_divisions = 0
for i in range(1, number1 + 1):
    remain = number1 % i
    if remain == 0:
        count_of_divisions += 1

if count_of_divisions > 2:
    print("This number is not prime!")
else:
    print("This number is prime!")


#exercise 6
"""Create a while loop that prints numbers from 10 to 0."""
num = 10
while num >= 0:
    print(num)
    num -= 1


#exercise 7
"""Implement a simple calculator that takes two numbers and an operator (+, -, *, /)
 as input from the user and performs the corresponding operation. Bonus task if you want,
   it's not necessary - add degree (ხარისხი), use ** operator for it."""

num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
operation = input("Enter operation")
if operation == "+":
    print("answer is", num1 + num2)
elif operation == "-":
    print("answer is", num1 - num2)
elif operation == "*":
    print("answer is", num1 * num2)
elif operation == "/":
    print("answer is", num1 / num2)
elif operation == "**":
    print("answer is", num1 ** num2)


#exercise 6
"""Ask user to enter name and print the last character of that string."""
user_name = input("Enter your name :")
print(user_name[-1])


#exercise 9
"""Using for loop, ask user for number. Then create a list which will have even numbers 
in next range: from 0 to user's number. At last, print out whole list. """

list1 = []
num_range = int(input("Enter number :"))
for number in range(0, num_range):
    if number % 2 ==0:
        list1.append(number)

print(list1)


#exercise 10
"""Ask user for whole number. Then create a factorial for 
this number and print it out. """

factorial_num = 1
number_for_user = int(input("enter your number :"))
for factorial in range(1, number_for_user + 1):
    total_factorial = factorial_num * factorial
    factorial_num = total_factorial

print(total_factorial)