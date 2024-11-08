cigarros = int(input("Quantos cigarros você acende por dia? "))
anos = float(input("Há quanto tempo você está nessa caminhada? "))

reducao_minutos = anos * 365 * cigarros * 10
reducaodias = reducao_minutos / (24 * 60)
print("seu tempo de vida perdido foi: ", reducaodias)
