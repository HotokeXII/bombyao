#ЛАБА №1
#1. работа со структурами данных
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[0]) #вывод первого элемента
print(my_list[2]) #вывод третьего элемента
print(my_list[-1]) #вывод последнего элемента
my_list[1] = 100 #замена второго элемента

#2. работа с циклами
for i in range(1, 11):
    print(i)

i = 10
while i>= 1:
    print(i)
    i -= 1

#3.работа с условными операторами
num = int(input('введите число: '))
if num % 2 == 0:
    print('число четное')
else:
    print('число нечетное')

num = int(input('введите число: '))
if num > 0:
    print('число положительное')
elif num < 0:
    print('число отрицательное')
else:
    print('число равно нулю')

#4.дз
#файл 1, задача 1
a = int(input('Введите число: '))
for i in range(1, a+1):
    print(i)

#файл 1, задача 2
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if a > b:
    print(a)
if b > a:
    print(b)
if a == b:
    print('числа равны')


#ЛАБА №2
#1.написание простых функций
def greet(name):
    print('здравствуйте,', name)
greet('Леонид Колбасняк')

def square(number):
    return print(number ** 2)
square(4)

def max_of_two(x, y):
    if x > y: return x
    if y > x: return y
print(max_of_two(7, 6))

#2.работа с аргументами функций
def des_per(name, age=30):
    x = f'имя: {name}, возраст: {age} лет'
    return print(x)
des_per('Леонид Колбасняк')

#3.использование функций для решения алгоритмических задач
def is_prime(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
        else:
            return True
print(is_prime(18))
