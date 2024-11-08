print("calculadora de IMC, atualizada em python!!")

peso = float(input("Digite seu peso: "))
altura = float(input("Agora sua altura: "))

imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}")

if (imc < 18.5):
    print("Abaixo do peso.")
elif (imc >= 18.5 and imc <= 24.9):
    print("Peso ideal.")
elif (imc >= 25.0 and imc <= 34.9):
    print("Sobrepeso.")
else:
    print("OBESO!")
