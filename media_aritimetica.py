numbers = []
harmonica = []
somah = 0
soma = 0
cont = 0
mult = 1


def media_harmonica(somaInversa, cont):
    return cont*(somaInversa**-1)


def media_geometrica(mult, cont):
    return (mult**(1/cont)-1)*100


with open('sum.txt', 'r') as inp:
    for line in inp:
        x = line.split()
        numbers = numbers + x

for number in numbers:
    soma = soma + float(number.replace(",", "."))
    somah = somah + 1/float(number.replace(",", "."))
    mult = mult*((float(number.replace(",", ".")))/100 + 1)
    cont += 1


print("soma: " + str(soma))
print("n: " + str(cont))
print("media arimetica: " + str(soma/cont))
print("media Harmonica " + str(media_harmonica(somah, cont)))
print("media geometrica: " + str(media_geometrica(mult, cont)))
