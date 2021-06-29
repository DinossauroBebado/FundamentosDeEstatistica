numbers = []
harmonica = []
somah = 0
soma = 0
cont = 0
mult = 1
numeros = []


def variancia(numeros, media):
    sum = 0
    for numero in numeros:
        sum = sum + (numero-media)**2
    var = (1/(len(numeros)-1)*sum)
    return var


def desvio_padrao(numeros, media):
    return variancia(numeros, media)**(1/2)


def percentil(numeros, pos):
    q = (pos/100)*(len(numeros)+1)
    alfa = int(str(q)[0:str(q).index(".")])
    beta = float(str(q)[str(q).index(".")+1:])/10
    return q


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
    if(float(number.replace(",", ".")) != 0):
        somah = somah + 1/float(number.replace(",", "."))
    numeros.append(float(number.replace(",", ".")))
    mult = mult*((float(number.replace(",", ".")))/100 + 1)
    cont += 1


print("soma: " + str(soma))
print("n: " + str(cont))
print("media arimetica: " + str(soma/cont))
print("media Harmonica " + str(media_harmonica(somah, cont)))
print("media geometrica: " + str(media_geometrica(mult, cont)))

# para calcular moderadas porcentils e tals
print(sorted(numeros))

print("desviopadrao: " + str(desvio_padrao(numeros, soma/cont)))
