cube_list = []
summa = 0
# заполнение списка кубами нечетных чисел +17 от 0 до 1000
for number in range(1, 1000):
    if number % 2 != 0:
        cube_list.append(number ** 3+17)
print("список", cube_list)

for i in range(len(cube_list)):
    d = 1                #делитель для нахождение разряда (1 - единицы,, 10 - десятки...)
    b = 0                # сумма цифр числа
    a = cube_list[i]     # iй элемент списка

# определив длину числа находим сумму его цифр
    while (a // d) !=0:
        b = b + (a // d % 10)
        d = d * 10

#складываем числа сумма цифр которых делиться нацело на 7
    if b % 7 == 0:
        summa += cube_list[i]
print(summa)
