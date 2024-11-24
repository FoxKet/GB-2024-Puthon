def num_translate(number):
    #number = input("Введите число:  ")


    translation = dict({"one":"один", "two":"два", "three":"три", "four":"четыре", "five":"пять", "six":"шесть", "seven":"семь",
                           "eight":"восемь", "nine":"девять", "ten":"десять"})

    #print(translation.get(number))

    #return translation.get(number)
    return translation.get(number.lower())


m = input("Введите число:  ")
#num_translate(number)

print(num_translate(m))



