
POS = 87


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


def variancia(numeros, media):
    sum = 0
    for numero in numeros:
        sum = sum + (numero-media)**2
    var = (1/(len(numeros)-1)*sum)
    return var


def desvio_padrao(numeros, media):
    return variancia(numeros, media)**(1/2)


def percentil(numeros, pos):
    numeros = sorted(numeros)
    q = (pos/100)*(len(numeros)+1)
    alfa = int(str(q)[0:str(q).index(".")])
    beta = q - alfa
    print(f'alfa:{alfa}  beta: {beta}')
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

medias = {"soma ": sum(numeros), "n ": len(numeros), "media aritimetrica ": media_aritimetrica(numeros),
          "media Harmonica ": media_harmonica(numeros), "media geometrica": media_geometrica(numeros), f'Percentil de {POS} ': percentil(numeros, POS),
          "desviopadrao:": desvio_padrao(numeros, media_aritimetrica(numeros))}

print("----------------------------")
for media in medias:
    print(media+str(medias[media]))
    print("----------------------------")

print(sorted(numeros))
