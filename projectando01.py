pares = []
impares = []
# criando uma lista que armazena e mostra numeros pares e impares
limite = int(input('limite dos numeros a seres exibidos: '))
numeros = [n for n in range(0,limite)]
for i in numeros:
    pares.append(i) if i % 2 == 0 else impares.append(i)
print("")
print('===' * 10)
print('Exibição dos Dados:')

print('Numeros pares: ',pares)
print('Numeros impares: ',impares)