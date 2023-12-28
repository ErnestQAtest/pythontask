# написать программу которая принимает на вход число от 1 до 7 и выводит соотв день недели
day = int(input('vvedite chislo dnya '))
if day in range (1, 8):
    if day == 1:
        print ('ponedelnik')
    if day == 2:
        print ('vtornik')
    if day == 3:
        print ('sreda')
    if day == 4:
        print ('chetverg')
    if day == 5:
        print ('pyatnica')
    if day == 6:
        print ('sybbota')
    if day == 7:
        print ('voskresenie')
else:
     print ('ne ta cifra')
