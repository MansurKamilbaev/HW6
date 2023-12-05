#Переменные
# a=15(int)
# b="Hello"(str)
# c=1.5(float)
# g=True

#Условные операторы
# a="Hello"
# if a=="Hello":
#     print("Yes")
# else:
#     print("No")

#Список
# a=[12,23,24,"ROW",True]
# b=a.append(12)
# print(a)

#Кортежи
# a=[2,3,4,5,'Dead',"Ghost"]
# if 2 in a and 'Dead' in a:
#     print(a[3:4])

#Циклы
# a=[12,34,5,6]
# for i in a:
#     i+=1
#     print(i)
# a=1
# while True:
#     a+=1
#     if a==100:
#         break
#     print(a)

#List Comprehension
# num=[i for i in range(1,21)]
# num_chotnie=[a for a in num if a%2==0]
# num_nechotnie=[b for b in num if b%2!=0]
#
# print(num_chotnie,num_nechotnie)

#Словари
# a={}
# a['name']="Mansur"
# print(a)
# a={'name':'Mansur'}
# a.clear()
# print(a)

#Сеты
# a={1,2,3,4,5,2,3,4,2,23,3,2}
# print(a)
# a=[1,2,3,4,5,2,1,2,3,2]
# b=set(a)
# print(b)

#Функия

# def Mansur():
#     return "Kamilbaev"
#
# print(Mansur())

# def gid(*args):
#     return args
#
# print(gid(1,2,3,"Mansur"))

# def primer(**kwargs):
#     return kwargs
#
# print(primer(name='Mansur'))

#Lambda
# a=lambda x: x**2
# print(a(20))
# x=[2,3,45]
# a=map(lambda d: d*2,x)
# print(list(a))
# a=[1,2,3,4,5,8]
# b=list(filter(lambda d:d%2==0,a))
# print(b)

#Классы
# class Car:
#     def __init__(self,type,year,speed):
#         self.type=type
#         self.year=year
#         self.speed=speed
# nexia=Car('Chevrolet',2009,220)
# print(nexia.type,nexia.year,nexia.speed)


#Наследование
# class Animal:
#     def make_sound(self):
#         pass
#
# class Dog(Animal):
#     def make_sound(self):
#         print("Голос собаки: Гав-гав!")
#
# class Cat(Animal):
#     def make_sound(self):
#         print("Голос кошки: Мяу-мяу!")
#
# class Cow(Animal):
#     def make_sound(self):
#         print("Голос коровы: Му-му!")
#
# dog=Dog()
# cat=Cat()
# cow=Cow()
#
# dog.make_sound()
# cat.make_sound()
# cow.make_sound()
