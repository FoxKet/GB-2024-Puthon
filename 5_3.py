#  Есть два списка:
# tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо
# вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)

from sys import getsizeof

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']
#
#
# def my_gen():
#nums_gen = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))
# eng_letters_gen = (chr(code) for code in range(ord('a'), ord('z') + 1))
# print(*eng_letters_gen, sep='')  # abcdefghijklmnopqrstuvwxyz

#temp = [klasses[i] if i < len(klasses) else None for i in range(len(tutors))]

a = tuple(zip(tutors,[klasses[i] if i < len(klasses) else None for i in range(len(tutors))]))
print(type(a), a)

#запуск генератора и вывод всех значений
gen = (a[i] for i in range(len(tutors)))
print(type(gen), *gen)

#запуск генератора до истощения
gen = (a[i] for i in range(len(tutors)))
for i in range(len(tutors)+1):
    print(next(gen))

# a = tuple(zip(tutors,klasses))
# #len = len(tutors)
# #gen = ( for a in)
# for i in range(len(tutors)):
#
#
#     print(a[i])





#     len_klasses = len(klasses)
#
#     return ((tutor, klasses[i]) if i < len_klasses else (tutor, None)
#         for i, tut in enumerate(tutors))
#
#
# if __name__ == '__main__':
#
#     gen = my_gen()
#     print(type(gen), *gen)

