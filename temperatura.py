def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def kelvin_to_celsius(k):
    return k - 273.15

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def celsius_to_kelvin(c):
    return c + 273.15

def menu():
    print("\nMenu:")
    print("1. Converter Fahrenheit para Kelvin")
    print("2. Converter Fahrenheit para Celsius")
    print("3. Converter Kelvin para Fahrenheit")
    print("4. Converter Kelvin para Celsius")
    print("5. Converter Celsius para Fahrenheit")
    print("6. Converter Celsius para Kelvin")
    print("7. Sair do programa")

while True:
    menu()
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 7:
        print("Saindo do programa...")
        break

    temp = float(input("Insira a temperatura: "))

    if opcao == 1:
        print(f"{temp} °F é igual a: {fahrenheit_to_kelvin(temp):.2f} K")
    elif opcao == 2:
        print(f"{temp} °F é igual a: {fahrenheit_to_celsius(temp):.2f} °C")
    elif opcao == 3:
        print(f"{temp} K é igual a: {kelvin_to_fahrenheit(temp):.2f} °F")
    elif opcao == 4:
        print(f"{temp} K é igual a: {kelvin_to_celsius(temp):.2f} °C")
    elif opcao == 5:
        print(f"{temp} °C é igual a: {celsius_to_fahrenheit(temp):.2f} °F")
    elif opcao == 6:
        print(f"{temp} °C é igual a: {celsius_to_kelvin(temp):.2f} K")
    else:
        print("Opção inválida, tente novamente!")