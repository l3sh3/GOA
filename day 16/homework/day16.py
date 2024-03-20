#exercise 1
"""შექმენით ქუჩის ქვიზი, 
სადაც ბენსიმონებში გაზმანული შავი ბიჭი გამვლელს შეეკითხება "რა კაცი ხარ" 

ხოლო სავარაუდო პასუხების მიხედვით გადაწყდება მისი ბედი
1) ცემა 
2) დაძმაკაცება 
3) ფულის ახევა"""

def quchis_qvizi():
    print("ra kaci xar? \n a) qalachuna \n b) kai bichi \n c) chmori")
    user_answer = input("Enter yor answer : a), b) or c) -")
    if user_answer == "a":
        print("shen gailaxe")
    elif user_answer == "b":
        print("chavdzmakacdit")
    elif user_answer == "c":
        print("puli agexa")

quchis_qvizi()


#exercise 2
"""We need a function that can transform a number (integer) into a string."""

def number_to_string(num):
    return str(num)


#exercise 3
"""Complete the solution so that it reverses the string passed into it."""

def solution(string):
    return string[::-1]


#exercise 4
"""Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse)."""

def opposite(number):
    return number * -1


#exercise 5
"""In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?"""

def make_negative( number ):
    if number > 0:
        return number * -1
    else:
        return number


#exercise 6
"""Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false."""

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"