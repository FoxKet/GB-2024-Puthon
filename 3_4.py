import pprint

import args as args


def thesaurus_adv(*args):

#name = ['Миша', 'Михаил','Даша', 'Макс', 'Дима', 'Лена', 'Леша', 'Таня', 'Яша', 'яша']
    name_list: list[str] = []
    name = []

    for i in args:
        name.append(i)

    my_dict = dict()

    for i in range(len(name)):
        key = name[i][:1]

        my_dict.setdefault(key,list())
        my_dict[key].append(name[i])

    return(my_dict)



#thesaurus("Иван", "Мария", "Петр", "Илья")
a = thesaurus_adv("Иван", "Мария", "Петр", "Илья", "Дима", "Гена", "Полина")
# печать ключ/значение с новой строки
#pprint.pprint(a)
pprint.pprint(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
#print(a)
#pprint.pprint(a, sort_dicts=False)
#pprint.pprint(thesaurus("Иван", "Мария", "Петр", "Илья"))

