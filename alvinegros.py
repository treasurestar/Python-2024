print("======================")
print("ALVINEGROS")
print("======================")
print("1. Estudante \n 2. Não Estudante")
while True:

    valorIngresso = 24
    categoria = int(input("Qual é sua categoria? "))
    nome = input("Qual é seu nome?")
    break
if categoria == 1:
    print("O valor do seu é ingresso é R$ 12,00")
    estudante = int(input("Quantos ingressos de estudante? "))
    ingressos = (24 / 2) * estudante
    print(f"O valor ficou de R${ingressos:.2f}")

elif categoria == 2:
    print("O valor do seu ingresso é R$ 24,00")
    ingressos = int(input("Quantos ingressos de Não Estudante? "))
    ingressos = ingressos * 24
    print(f"O valor ficou de R${ingressos:.2f}")

elif categoria != 1 and 2:
    print("Não entendi o comando, repita o processo.")


    print(f"{nome}, seja bem-vindo ao cinema dos Alvinegros. O valor a pagar será de acordo com sua categoria.")