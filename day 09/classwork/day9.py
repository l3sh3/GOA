#printing numbers  from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1




#printing numbers from 100 to 0
i = 100
while i >= 0:
    print(i)
    i -= 1




#printing sum of all numbers from 1 to 10
i = 1
sum = 0
while i <=10:
    sum += i
    i += 1

print(sum)





#printing sum of all even numbers from 0 to 10
i = 0
sum = 0
while i <= 10:
    if i % 2 == 0:
        print(i)
        sum += i
    i += 1

print(sum)




#printing all odd numbers from 0 to 10
i = 0
while i <= 10:
    if i % 2 == 1:
        print(i)
    i += 1