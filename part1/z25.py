from math import sqrt

print ("Задание 25: Треугольник задан координатами своих вершин. Найти Площадь и периметр")
print ('Введите координаты первой вершины (через пробел)')
x1,y1=map(float,input().split())
print ('Введите координаты второй вершины (через пробел)')
x2,y2=map(float,input().split())
print ('Введите координаты третьей вершины (через пробел)')
x3,y3=map(float,input().split())
a=sqrt((x2-x1)**2+(y2-y1)**2)
b=sqrt((x3-x2)**2+(y3-y2)**2)
c=sqrt((x1-x3)**2+(y1-y3)**2)
p=(a+b+c)/2.0
s=sqrt(p*(p-a)*(p-b)*(p-c))
print ('Площадь',"%.04f"%s,'Периметр',"%.04f"%(a+b+c))

input ("Нажмите ENTER для выхода")
