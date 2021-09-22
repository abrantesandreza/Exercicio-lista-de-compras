print('Vamos fazer as compras das frutas da semana? ')
print('Digite: 1- Maçã; 2- Banana; 3- Laranja; 4-Kiwi; 5-Morango; 6-Limão; 7-Mamão; 8-Manga; 9-Melão; 10-Uva; 0-Nenhuma fruta')
qtd1 = int(input('Digite aqui a quantidade desejada de Maçãs: '))22
res1 = qtd1 * 2

qtd2 = int(input('Digite aqui a quantidade desejada de Bananas: '))
res2 = qtd2 * 2.50

qtd3 = int(input('Digite aqui a quantidade desejada de Laranjas: '))
res3 = qtd3 * 1.50

qtd4 = int(input('Digite aqui a quantidade desejada de kiwi: '))
res4 = qtd4 * 1.50

qtd5 = int(input('Digite aqui a quantidade desejada de Morangos: '))
res5 = qtd5 * 1

qtd6 = int(input('Digite aqui a quantidade desejada de Limão: '))
res6 = qtd6 * 1.75

qtd7 = int(input('Digite aqui a quantidade desejada de Mamão: '))
res7 = qtd7 * 1

qtd8 = int(input('Digite aqui a quantidade desejada de Manga: '))
res8 = qtd8 * 3

qtd9 = int(input('Digite aqui a quantidade desejada de Melão: '))
res9 = qtd9 * 1

qtd10 = int(input('Digite aqui a quantidade desejada de Uva: '))
res10 = qtd10 * 2.75

res11 = (res1 + res2 + res3 + res4 + res5 + res6 + res7 + res8 + res9 + res10)

print('As compras de fruta da semana totalizaram em: {} reais'.format(res11))






