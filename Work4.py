#Напишите программу, которая по заданному номеру четверти, 
#показывает диапазон возможных координат точек в этой четверти (x и y).

quarterNumber = int(input('Введите номер четверти: '))
 
if quarterNumber == 1:
    print('x > 1, y > 1')
elif quarterNumber == 2:
    print('x < 1, y > 1')
elif quarterNumber == 3:
    print('x < 1, y < 1')
elif quarterNumber == 4:
    print('x > 1, y < 1')
else:
    print('Вы ввели неправильный номер четверти')