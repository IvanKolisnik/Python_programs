import math
import random
print("Задание 178 а")
n = (int(input("Введите n = ")))
print(n)
k = 0
i = 1
for i in range(n):
    a = int(input(f"Введите {i} число "))
    if (a % 2 != 0):
         k += 1
print("Результат ", k)
print("_________________________________")

print("Задание 178 б")
n = (int(input("Введите n = ")))
print(n)
k = 0
i = 1
for i in range(n):
    a = int(input(f"Введите {i} число "))
    print(a)
    if (a%3 == 0) and (a%5!=0):
        k += 1
print("Результат = ",k)
print("_________________________________")

print("Задание 178 в")
mass = [9,16,25,36,49,]
 
print(len([i for i in mass if math.sqrt(i)%2==0]))
print("_________________________________")

print("Задание 178 г")
    
