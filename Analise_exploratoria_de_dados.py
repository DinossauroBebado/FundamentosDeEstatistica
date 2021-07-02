
POS = 33


def parse(numbers):
    numeros = []
    for number in numbers:
        try:
            numero = float(number.replace(",", "."))
        except ValueError:
            print("ERROR valor digitado não é um número")
            quit()
        numeros.append(numero)

    return numeros


def coeficienteCurtose(numeros):
    sum = 0
    x = media_aritimetrica(numeros)

    for numero in numeros:
        sum = sum + (numero-x)**4

    coe = (1/(len(numeros)*desvio_padrao(numeros)**4)*sum) - 3
    return coe


def CoeficienteAssimetria(numeros):
    sum = 0
    x = media_aritimetrica(numeros)

    for numero in numeros:
        sum = sum + (numero-x)**3

    coe = 1/(len(numeros)*desvio_padrao(numeros)**3)*sum
    return coe


def Amplitude_interquarica(numeros):
    return (percentil(numeros, 75) - percentil(numeros, 25))


def AssimetriaQuantis(numeros):
    return (percentil(numeros, 75) + percentil(numeros, 25) - 2*mediana)/Amplitude_interquarica(numeros)


def variancia(numeros):
    sum = 0
    media = media_aritimetrica(numeros)
    for numero in numeros:
        sum = sum + (numero-media)**2
    var = (1/(len(numeros)-1)*sum)
    return var


def desvio_padrao(numeros):
    return variancia(numeros)**(1/2)


def desvio_medio(numeros):
    sum = 0
    x = media_aritimetrica(numeros)
    for numero in numeros:
        sum = sum + abs(numero - x)

    return (1/len(numeros))*sum


def percentil(numeros, pos):
    numeros = sorted(numeros)
    q = (pos/100)*(len(numeros)+1)
    alfa = int(str(q)[0:str(q).index(".")])
    beta = q - alfa
    perc = numeros[alfa-1] + beta*(numeros[alfa]-numeros[alfa-1])

    return perc


def media_harmonica(numeros):
    soma = 0
    for numero in numeros:
        if(numero != 0):
            soma = soma + 1/numero

    return len(numeros)*(soma**-1)


def media_geometrica(numeros):
    mult = 1
    for numero in numeros:
        mult = (mult*(numero/100 + 1))

    return (mult**(1/len(numeros))-1)*100


def media_aritimetrica(numeros):

    return sum(numeros)/len(numeros)


with open('sum.txt', 'r') as inp:
    numbers = []
    for line in inp:
        x = line.split()
        numbers = numbers + x


numeros = parse(numbers)

mediana = percentil(numeros, 50)

medias = {"soma ": sum(numeros), "n ": len(numeros), "media aritimetrica ": media_aritimetrica(numeros),
          "media Harmonica ": media_harmonica(numeros), "media geometrica ": media_geometrica(numeros), f'Percentil de {POS} ': percentil(numeros, POS),
          "Desvio padrao:": desvio_padrao(numeros), "Amplitude interquarica ": Amplitude_interquarica(numeros),
          "Desvio Médio ": desvio_medio(numeros), "Variância ": variancia(numeros), "Coeficiente de Assimetria ": CoeficienteAssimetria(numeros),
          "Coeficiente de assimetria(Quantis) ": AssimetriaQuantis(numeros), "Coeficiente de Curtose ": coeficienteCurtose(numeros)}

print("----------------------------")
for media in medias:
    print(media+str(medias[media]).replace(".", ","))
    print("----------------------------")

print(sorted(numeros))
