numbers = []
soma = 0
cont = 0
with open('sum.txt', 'r') as inp:
    for line in inp:
        x = line.split()
        numbers = numbers + x
for number in numbers:
    soma = soma + float(number.replace(",", "."))
    cont += 1

print("soma: " + str(soma))
print("n: " + str(cont))
print("media arimetica: " + str(soma/cont))
