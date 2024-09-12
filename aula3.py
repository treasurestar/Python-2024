# tipos de dados primitivos: 
# - inteiro(int): numeros inteiros
# - float (float): numeros reais, decimais
# - string (str): cadeias de caracteres, utilizando aspas
# - boolean (bool): tipo logico True ou False
# - complex (complex): numeros complexos, com parte real e imaginaria
# - list (list): lista de elementos, ordenados e imutaveis
# - tuple (tuple): tuple de elementos, ordenados e imutaveis
# - dictionary (dict): dicionario de elementos, não ordenados e indexados

# atribuição de variavel por captura
nome = input("Escreva seu nome: ")
print(type(nome))
idade = input("Quantos anos você tem? ")
print(type(idade))
altura = input("Qual sua altura? ")
print(type(altura))

print(f"nome: {nome} idade: {idade} altura: {altura}")

valorA = int(input("digite o valor de A: "))
valorB = int(input("digite o valor de B: "))
resultado = valorA + valorB
print(f"a soma = {resultado}")


valorA = float(input("digite o valor de A: "))
valorB = float(input("digite o valor de B: "))
resultado = valorA + valorB
print(f"a soma = {resultado}")