numeros= []
for i in range(5):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)

print("Maior número:", maior)
print("Menor número:", menor)
print("Soma dos números:", soma)