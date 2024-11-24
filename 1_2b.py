#for number in range(1, 1000):
#    if number % 2 != 0:
#        print(number**3)
list_e = []
list_d = []
list_s = []
list_et = []
list_dt = []
list_st = []
list_em = []
list_dm = []
list_sm = []
list_sum = []
list_zero = []
list_a = []

# создаем список из нечетных чисел от 1 до 1000 и увеличиваем каждый элемент на 17
cube_list = [(i*2+1)**3+17 for i in range(500)]
print(cube_list)
for i in range(len(cube_list)): # цикл поиска единиц
    list_e.append(cube_list[i] % 10)
print(list_e)
for i in range(len(cube_list)): # цикл поиска десятков
    list_d.append(cube_list[i] // 10 % 10)
print(list_d)
for i in range(len(cube_list)): # цикл поиска сотен
    list_s.append(cube_list[i] // 100 % 10)
print(list_s)
for i in range(len(cube_list)): # цикл поиска единиц тысяч
    list_et.append(cube_list[i] // 1000 % 10)
print(list_et)
for i in range(len(cube_list)): # цикл поиска десятки тысяч
    list_dt.append(cube_list[i] // 10000 % 10)
print(list_dt)
for i in range(len(cube_list)): # цикл поиска сотен тысяч
    list_st.append(cube_list[i] // 100000 % 10)
print(list_st)
for i in range(len(cube_list)): # цикл поиска единиц мил
    list_em.append(cube_list[i] // 1000000 % 10)
print(list_em)
for i in range(len(cube_list)): # цикл поиска дес мил
    list_dm.append(cube_list[i] // 10000000 % 10)
print(list_dm)
for i in range(len(cube_list)): # цикл поиска сотен мил
    list_sm.append(cube_list[i] // 100000000 % 10)
print(list_sm)

# складываем разряды чисел
for i in range(len(cube_list)):
    list_sum.append(list_e[i] + list_d[i] + list_s[i] + list_et[i] + list_dt[i] + list_st[i] + list_em[i] + list_dm[i] + list_sm[i])
print(list_sum)

# находим числа сумма цифр которого делиться на 7
for i in range(len(cube_list)):
    list_zero.append(list_sum[i] % 7)
print(list_zero)

for i in range(len(cube_list)):
    if list_zero[i] == 0:
        list_a.append(cube_list[i])
print(list_a)

summa = 0
for i in range (len(list_a)):
    summa += list_a[i]
print (summa)