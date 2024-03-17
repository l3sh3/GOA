#exercise 1
"""Create an array which will include numbers from 0 to 20 (write it manually, without loops), then print whole array."""

first_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15, 16, 17, 18, 19, 20]
print(first_array)


#exercise 2
"""Create a new array, which will include even numbers from the first array. Then print this new array."""

second_array = []
for i in first_array:
    if i % 2 == 0:
        second_array.append(i)

print(second_array)


#exercise 3
"""Create an array, then add numbers from 50 to 100 to it. In the end,
 print the part of this array with negatives indexes."""

third_array = []
for num in range(50, 100):
    third_array.append(num)

print(third_array[-10])


#exercise 4
"""Ask user for two inputs and store them as variables, their type has to be int. 
Then use for loop, use lower number from this two variables as start, Higher number 
as end, you do not need step. After that, you'll have to use if statement to only print multiples of five."""

first_num = int(input("Enter your first number :"))
second_num = int(input("Enter your second number :"))
for number in range(min(first_num, second_num), max(first_num, second_num)):
    if number % 5 == 0:
        print(number)


#exercise 5
"""Create a new array. Ask user his/her age and if it will be over 18, ask him/her name. 
Then add this name to already created array and print it."""

new_array = []
user_age = int(input("Enter yor age :"))
if user_age > 18:
    user_name = input("Enter your name :")
    new_array.append(user_name)

print(new_array)
