kmrodados = float(input("Quantos KM foram rodados? "))
dias = int(input("Por quantos dias o carro foi usado? "))

valor = (60 * dias) + (0.15  * kmrodados)
print(f"O valor a pagar pelo aluguel do carro é {valor} reais")
