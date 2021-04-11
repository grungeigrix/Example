#Условие
#Заданы две клетки шахматной доски.
# Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO.
# Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

if x1%2==0:
    if y1%2==0:
        color1 = 1
    else:
        color1 = 0
else:
    if y1%2==0:
        color1 = 0
    else:
        color1 = 1

if x2%2==0:
    if y2%2==0:
        color2 = 1
    else:
        color2 = 0
else:
    if y2%2==0:
        color2 = 0
    else:
        color2 = 1
if color1 == color2:
    print("YES")
else:
    print("NO")
