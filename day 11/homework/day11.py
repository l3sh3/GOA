#exercise 1
"""Write a program that takes an input from the user and checks if it's a positive, 
negative, or zero number using if-else."""

num = int(input("Enter your number: "))
if num > 0:
    print("The number is positive!")
elif num < 0:
    print("The number is negative!")
else:
    print("The number is zero!")


#exercise 2
"""Write a program that prints all the even numbers between 1 and 20 using 
a for loop and if statement."""

for i in range(20 + 1):
    if i % 2 == 0:
        print(i)

#exercise 3
"""Write a program that calculates the sum of a number entered by the user 
using a for loop."""

user_num = int(input("Enter the number: "))
sum = 0
for i in range(user_num):
    sum += i
print(sum)


#exercise 4
"""Write a program that simulates a basic ATM. It should ask the user for their PIN, 
and if it's correct, display a text withdrawal, deposit, and balance. 
"""

pin = 1234
user_input = int(input("Enter your pin: "))
if pin == user_input:
    print("withdrawal; deposit;  balance.")
else:
    print("INCORRECT PIN!")

#exercise 5
"""Write a program that simulates a simple login system.
 Ask the user for a username and password, and if they enter "admin" and 
 "password123", respectively, print "Login successful" using if-else."""

username = "admin"
password = "password123"
users_name = input("Enter your username: ")
user_password = input("Enter your password: ")
if username == users_name and password == user_password:
    print("Login successful!")
else:
    print("Incorrect username or password!")


#exercise 6
"""Write a program that asks the user for their age and
 prints a message based on the age range (e.g., "Child", "Teenager", "Adult")
   using if-elif-else."""

user_age = int(input("Enter your age: "))
if user_age < 10:
    print("You are child!")
elif user_age >= 10 and user_age < 18:
    print("You are teenager!")
else:
    print("You are adult!")