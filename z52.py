import math
print ("Задание 52 ")
u = input("Введите u: ")
t = input("Введите t: ")
s = input("Введите s: ")
d = input("Введите d: ")
c = input("Введите c: ")
b = input("Введите b: ")
a = input("Введите a: ")
u = float(u)
t = float(t)
s = float(s)
d = float(d)
c = float(c)
b = float(b)
a = float(a)
z1 = ((s*a)+t)*(b+u)
z2 = ((s*c)+t)*(d+u)
if ((z1*z2)<0): print("Принадлежат разным полуплоскостям")
else: print("Принадлежат одной полуплоскости")