#davaleba1
# list1 = []
# for i in range(0, 50):
#     list1.append(i)

# print(list1[:25])
# print(list1[:25:3])




#davaleba2
# list2 = []
# num = int(input("enter number: "))
# for i in range(num, num + 10):
#     list2.append(num)

# print(list2[::2])

#davaleba1
# def multiply():
#     num = int(input("enter number"))
#     print(num * 3)

# multiply()


# #davaleba2
# def multiply(num):
#     print(num * 3)

# multiply(20)
# multiply(15)
# multiply(30)
# multiply(45)
# multiply(50)

"""მოხმარებელს შემოატანინეთ პაროლი იქამდე სანამ არ დაემტხვევა რეგისტრირებულ პაროლს, 
while ციკლის და  if else _ის გამოყენებით"""


user_password = "12345678"
autorized = False

while autorized == False:
    password = input("Enter your password: ")
    if password == user_password:
        autorized = True
        print("ACCESS GRANTED")
    else:
        print("invalid password. Please try again!")


