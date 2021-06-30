for number in numbers:
    soma = soma + float(number.replace(",", "."))
    if(float(number.replace(",", ".")) != 0):
        somah = somah + 1/float(number.replace(",", "."))
    numeros.append(float(number.replace(",", ".")))
    mult = mult*((float(number.replace(",", ".")))/100 + 1)
    cont += 1