import statistics as st

"""
Lista 6 - Probabilidade e Estatística - Coeficiente de variação

Faça um programa que calcule o coeficiente de variação de uma lista de valores.

Entrada: Um inteiro N, em seguida uma linha com N números.

Saida: O coeficiente de variação dos N números. (Imprima o resultado com 2 casas decimais)

Exemplos de Entrada e Saída
Entrada:

7
1.4 1.2 0.3 4.4 5.1 3.2 1.1
Saída:

0.77

"""
n = int(input())
numeros = list(map(float, input().split()))
# print(numeros)

# Soma os elementos da lista:
soma = sum(numeros)
# print(soma)

# Média:
media = st.mean(numeros)
# print(media)

# Desvio padrão:
desvio = st.stdev(numeros)
# print(desvio)

# Coeficiente de variação:
cv = desvio / media
print(f'{cv:.2f}')
