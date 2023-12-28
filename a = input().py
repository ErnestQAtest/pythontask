a = input().lower()
b = int(input('enter year: '))
if (b % 4 == 0) and b % 100 != 0 or b % 400 == 0:
    print(a=='feb',29)
else:
    print(28)