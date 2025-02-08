# EXERCICIOS

# 1) Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.


'''
# COMO EU FIZ

### 1a) Criando uma lista

lista: int = []
n: int = 0
while n < 10:
    n += 1 
    lista.append(n)
print("lista =", lista) 
print("n =", n)

### 1b) Usando a lista criada
for i in lista:
    i2: int = i ** 2
    print("numero:", i, "- quadrado:", i2)
print("programa executado com êxito.")    
exit()

# COMO É O GABARITO:

numeros = list(range(1, 11))
print("lista =", numeros)
print("n =", len(numeros))
for numero in numeros:
    print("numero:", numero, "- quadrado:", numero**2)
    
'''


# 2) Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# 3) Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# 4) Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# 5) Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o
#    preço total da lista de compras.


