#exercise 1
"""შექმენით ფუნქცია, რომელსაც გადაეცემა 1-იდან 20-ის ჩათვლით რიცხვების სია. 
თქვენ უნდა დააბრუნოთ გაფილტრული სია, სადაც უკვე მარტო 4-ის ჯერადები იქნება."""

def nums_from_one_to_twenty():
    new_arr = []
    for i in range(1, 20 + 1):
        if i % 4 == 0:
            new_arr.append(i)
    return new_arr

print(nums_from_one_to_twenty())


#exercise 2
"""შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლისგან მიღებულ სახელსა და გვარს. შემდეგ ისინი დაამატეთ სიაში და დააბრუნეთ სია."""
def name_and_surname():
    user_arr = []
    name = input("Enter your name :")
    surname = input("Enter yoour surname :")
    user_arr.append(name)
    user_arr.append(surname)
    return user_arr

print(name_and_surname())


#exercise 3
"""მომხმარებელს შეეკითხეთ საწყისი და საბოლოო რიცხვები. ეს რიცხვები გადაეცით ფუნქციას, 
for ციკლით სიაში შეინახეთ მათ შორის არსებული რიცხვები. შემდეგ მოახდინეთ გაფილტვრა, ისევ 
for ციკლით განიხილეთ თითოეული რიცხვი - თუ რიცხვი ლუწი იქნება, ახალ სიაში დაამატეთ მისი მეორე ხარისხი, 
ხოლო თუ კენტი იქნება სიაში დაამატეთ მისი კვადრატული ფესვი (0.5 ხარისხი)."""


def filterd_arr():
    num1 = int(input("Enter your first number :"))
    num2 = int(input("Enter your second number :"))
    final_arr = []
    for i in range(min(num1, num2), max(num1, num2)):
        if i % 2 == 0:
            i *= i
            final_arr.append(i)
        else:
            i **= 0.5
            final_arr.append(i)
    return final_arr

print(filterd_arr())


#exercise 4
"""შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლის გვარს. გვარის თითოეული ასო გადაიტანეთ ახალ სიაში. 
შემდეგ for ციკლის გამოყენებით იმუშავეთ ამ სიაზე - მარტო ლუწ ინდექსებზე მყოფი ასოები დაამატეთ ახალ სიაში. 
საბოლოოდ დააბრუნეთ ეს სია.Bonus (არაა სავალდებულო): ეს სია გარდაქმენით სთრინგად და ამ სახით დააბრუნეთ."""

def func():
    surname = input("Enter your surname :")
    filtered_surname_arr = []
    index = 0
    for i in surname:
        index += 1
        if index % 2 == 0:
            filtered_surname_arr.append(i)
    arr_into_string = ""
    for i in filtered_surname_arr:
        arr_into_string += i
    return arr_into_string

print(func())


#exercise 5
"""შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. თქვენ უნდა დააბრუნოთ ამ სიის საშუალო არითმეტიკული ( ჯამი / სიგრძე )"""

def arithmetic_avarage(list_of_numbers):
    sum = 0
    for i in list_of_numbers:
        sum += i
    if len(list_of_numbers) == 0:
        return 0
    else:
        result = sum / len(list_of_numbers)
        return result

print(arithmetic_avarage([1, 2, 3, 4]))


#exercise 6
"""შექმენით ფუნქცია, რომელიც მიიღებს მომხმარებლისგან სიტყვას. შემდეგ თქვენ უნდა მოახდინოთ ამ სიტყვის შებრუნება, 
მაგ: word - drow. საბოლოდ კი დააბრუნეთ შედეგი."""
def reverse(word):
    return word[::-1]

print(reverse("lasha"))


#exercise 7
"""შექმენით ფუნქცია, რომელიც მიიღებს რიცხვების სიას და თქვენ დააბრუნებთ მის გაფილტრულ ვერსიას, 
რომელსაც არ ექნება დუპლიკატები (ერთი და იგივე ელემენტები)."""

def no_duplicates(numbers_list):
    without_dublicate = []
    for i in numbers_list:
        if i not in without_dublicate:
            without_dublicate.append(i)
    return without_dublicate

print(no_duplicates([1, 2, 2, 3, 4 ,5, 5]))