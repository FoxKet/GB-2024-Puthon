#Представлен список чисел. Определить элементы списка,
# не имеющие повторений. Сформировать из этих элементов список
# с сохранением порядка их следования в исходном списке, например:
#src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#result = [23, 1, 3, 10, 4, 11]

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []

# for i in range(len(src)):
#     if src.count(src[i]) == 1:
#         result.append(src[i])
# print(result)

result = [src[i] for i in range(len(src)) if src.count(src[i]) == 1]

print(result)




# src.sort()
# src.append(src[len(src)-1]+1)
# src = [src[0] - 1] + src
# print(src)
#
# for i in range(1, len(src)-1):
#     if ((src[i] != src[i+1]) and (src[i] != src[i-1])):
#         result.append(src[i])
#
# print(result)


