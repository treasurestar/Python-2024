def primo(numero):
    if numero <= 1:
      return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Solicita um número ao usuário
num = int(input("Digite um numero: "))

if primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")