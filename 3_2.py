def num_translate_adv(number):
#number = input("Введите число:  ")


    translation = dict({"one":"один", "two":"два", "three":"три", "four":"четыре", "five":"пять", "six":"шесть", "seven":"семь",
                               "eight":"восемь", "nine":"девять", "ten":"десять"})

    #a = number.lower() # слово в нижний регистр как в словаре
    if number.istitle() and translation.get(number.lower()):
        # a = translation.get(number.lower())
        # print(a.capitalize())

        #print(translation.get(number.lower()).capitalize())
        return translation.get(number.lower()).capitalize()

        # print(translation.get(number.isupper()))
        #return translation.get(number)
    else:
        #print(translation.get(number.lower()))
        return translation.get(number.lower())



m = input("Введите число:  ")

print(num_translate_adv(m))
