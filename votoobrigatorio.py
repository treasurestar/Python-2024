print("VOTAÇÃO!")

idade = int(input("qual é sua idade? "))

if idade >= 18 and idade < 65:
    print("Nesse país, você é obrigado a votar.")
elif idade >= 16 and idade <= 17 or idade >= 65:
    print("Você que decide se volta ou não.")
else:
    print("Voto não permitido.")
