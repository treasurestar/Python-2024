cedulas = [50, 20, 10, 5, 1]
valor = int(input("Digite o valor para pagar ou 0 para sair. NÃO DÊ CALOTE! "))

valor_original = valor
print(f"\nPreciso de R$ {valor_original}")

for cedula in cedulas:
        if valor >= cedula:
            quantidade = valor // cedula
            print(f"R$ {cedula}: {quantidade} cédula(s)")
            valor %= cedula
        else:
            print(f"R$ {cedula}: 0 cédula(s)")

print("Pagamento realizado.")