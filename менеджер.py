#Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000
#— 5%, свыше 1000 — 8%. Пользователь вводит с клавиатуры уровень продаж для трех
#менеджеров. Определить их зарплату, определить лучшего менеджера, начислить ему премию
#200$, вывести итоги на экран
#
# a = int(input('введите что набарыжил первый: '))
# b = int(input('введите что набарыжил второй манагер: '))
# c = int(input('введи чё набарыжил третий: ')) #a,b,c - выручка каждого менеджера
# o =200 # o - оклад
# if a > 1000:
#     z1 = o + a*0.08 # z1, z2, z3 - зарплаты манагеров
# else:
#     if a < 500:
#         z1 = o + a*0.03
#     else:
#         z1 = o + a*0.05
#         if b > 1000:
#             z2 = o + b* 0.08
#         else:
#             if b < 500:
#                 z2 = o + b*0.03
#             else:
#                 z2 =o + b*0.05
#                 if c > 1000:
#                     z3= o + c*0.08
#                 else:
#                     if c < 500:
#                         z3= o + c*0.03
#                     else:
#                         z3= o +c*0.05
#                         if z1>z2 and z1>z3:
#                             print('лучше барыжит первый!')
#                             z1 += 200
#                             if z2>z1 and z2>z3:
#                                 print('лучший барыга второй манагер!')
#                                 z2 +=200
#                                 if z3 > z1 and z3 >z2:
#                                     print('лучший барыга третий манагер!')
#                                     z3 += 200
#                                     print('зарплата 1 манагера', z1)
#                                     print('зарплата 2 манагера', z2)
#                                     print('зарплата 3 манагера', z3)

#-_______________________________________________
#ЕЩЁ СПОСОБ
salaries=[a,b,c]
for i, salary in enumirate(salaries):
    if salary < 500: