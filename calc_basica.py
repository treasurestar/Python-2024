while opcao != 6:
    print("Calculadora Básica")
    print("Menu de escolha:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Resto da Divisão")
    print("6. Sair")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        n1 = int(input("\n\nInsira o primeiro valor: "))
        n2 = int(input("Insira o segundo valor: "))
        print(f"A soma dos valores é: {n1 + n2}\n")
    
    elif opcao == 2:
        n1 = int(input("\n\nInsira o primeiro valor: "))
        n2 = int(input("Insira o segundo valor: "))
        print(f"A subtração dos valores é: {n1 - n2}\n")
    
    elif opcao == 3:
        n1 = int(input("\n\nInsira o primeiro valor: "))
        n2 = int(input("Insira o segundo valor: "))
        print(f"A multiplicação dos valores é: {n1 * n2}\n")
    
    elif opcao == 4:
        n1 = int(input("\n\nInsira o primeiro valor: "))
        n2 = int(input("Insira o segundo valor: "))
        
        if n2 == 0:
            print("Erro: Divisão por zero não é permitida.\n")
        else:
            print(f"A divisão dos valores é: {n1 / n2}\n")
    
    elif opcao == 5:
        n1 = int(input("\n\nInsira o primeiro valor: "))
        n2 = int(input("Insira o segundo valor: "))
        
        if n2 == 0:
            print("Erro: Divisão por zero não é permitida.\n")
        else:
            print(f"O resto da divisão dos valores é: {n1 % n2}\n")
    
    elif opcao == 6:
        print("Finalizando o código!")
    
    else:
        print("Opção inválida. Tente novamente.\n")