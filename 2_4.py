my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

print(type(my_list))
for i in range(len(my_list)):
    name = my_list[i].split()
    print("'", "Привет, ", name[-1].title(),"!", "'", sep="")


