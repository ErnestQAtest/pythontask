# Напишите программу, которая принимает на вход три числа и выводит наибольшее из них.

#print('наибольшее', max(int(input('введите значение 1: ')), int(input('введите значение 2: ')), int(input('введите значение 3: '))))

# как то длинно было

a = int(input('введите число 1: '))
b = int(input('введите число 2: '))
c = int(input('введите число 3: '))
print('наибольшее', max(a,b,c))