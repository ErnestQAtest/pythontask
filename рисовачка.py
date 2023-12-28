# Напишите программу для вывода новогодней елочки из звездочек

lin = 1
tree_height = int(input('введите высоту ёлочки: ')) # если ввести 99999999999999999 то комп сначало повиснет, а потом выключится
while lin <= tree_height:
    print((tree_height - lin)*' ' + lin * '*' + (lin-1)*'*')
    lin += 1

# напишите программу для черепахи,
# чтобы она рисовала вот так  (кол-во углов произвольное)

import turtle, random
t = turtle.Turtle()
colors = ["yellow", "red", "purple", 'green', 'black'] # я не понимаю почему каждый раз при запуске по разному цвета накладывает, как сделать что бы не путало???
lengths = 50
angles = 90
for i in range(8):
    if i % 2 == 1:
        t.pencolor(random.choice(colors))
    t.forward(lengths*(i/2))
    t.left(angles*(-1)**i)
turtle.done()