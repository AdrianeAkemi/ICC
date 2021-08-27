'''

Combinando o menor número possível de cédulas
Escreva um programa que lê um valor em dinheiro e calcula qual o menor número possível de cédulas
de 100.00, 50.00, 10.00, 5.00 e 1.00 em que o valor lido pode ser decomposto. O programa deve
retornar o valor lido e a relação de notas necessárias.


# x recebe o valor em dinheiro
x = int(input())
cem = x // 100
cinquenta = (x - 100*cem) // 50
aux1 = x - cinquenta*50

print (f'{cem} de R$100,00')
print(f'{cinquenta} de R$50,00')

'''

x = int(input())
cem = x // 100
x -= 100*cem
cinquenta = x // 50
x -= 50*cinquenta
dez = x // 10
x -= 10*dez
cinco = x // 5
x -= 5*cinco
um = x // 1

print (f'{cem} de R$100,00')
print(f'{cinquenta} de R$50,00')
print (f'{dez} de R$10,00')
print(f'{cinco} de R$5,00')
print (f'{um} de R$1,00')

