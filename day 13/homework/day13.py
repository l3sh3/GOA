#exercie 1
"""Write a program that prints numbers from 1 to 10 using a while loop."""

number = 0
while number <= 10:
    print(number)
    number += 1


#exercise 2
"""Write a program that prints the even numbers from 1 to 10 using a for loop."""

for i in range(10 + 1):
    if i % 2 == 0:
        print(i)


#exercie 3
"""Write a program that asks the user to enter a number and then prints whether the 
number is positive, negative, or zero using an if-else statement."""

num = int(input("Enter your number :"))
if num > 0:
    print("This number is positive!")
elif num < 0:
    print("This number is negative!")
else:
    print("This number is zero!")


#exercise 4
"""Write a program that asks the user to enter a password. If the password is 
"abc123", print "Access granted"; otherwise, print "Access denied"."""

password = input("Please enter your password :")
if password == "abc123":
    print("access granted!")
else:
    print("access denied!")


#exercise 5
"""Write a program that prints numbers from 1 to 10, but stops if the number is 5 
using a while loop and the break statement. break"""

numb = 0
while numb <= 10:
    print(numb)
    numb += 1
    if numb == 5:
        break


#exercise 6
"""Write a program that asks the user to enter a number between 1 and 5. If the number is less 
than 1 or greater than 5, print "Invalid input". If the number is between 1 and 5,
 print "Valid input"."""

one_to_five = int(input("Please enter number from 1 to 5 :"))
if one_to_five < 1 or one_to_five > 5:
    print("Invalid input!")
else:
    print("Valid input!")


#exercise 7
"""Write a program that asks the user to enter a number. If the number is divisible by 3, print "Fizz".
 If the number is divisible by 5, print "Buzz". If the number is divisible by both 3 and 5, print "FizzBuzz". 
 Otherwise, print the number itself."""

user_num = int(input("Enter your number :"))
if user_num % 3 == 0:
    print("Fizz")
elif user_num % 5 == 0:
    print("Buzz")
elif user_num % 3 == 0 and user_num % 5 == 0:
    print("FizzBuzz")
else:
    print(user_num)
    