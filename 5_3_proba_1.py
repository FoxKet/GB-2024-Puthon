import json

def thesaurus(*args):
    name = []

    for i in args:
        name.append(i)

    my_dict = dict()

    for i in range(len(name)):
        key = name[i][:1]
        my_dict.setdefault(key, list())
        my_dict[key].append(name[i])

    print(json.dumps(my_dict, indent=4, sort_keys=True, ensure_ascii=False))
    return my_dict

thesaurus("Иван", "Мария", "Петр", "Илья", "Дима", "Гена", "Полина", "Глеб")