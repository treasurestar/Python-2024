contador = 0
while contador <= 100:
    contador += 1

    if (contador == 6):
        print("O número 6 não será mostrado.") 
        continue
    if (contador >= 10 and contador <= 27):
        print("não vou mostrar") 
        continue

    print(contador)

    if contador == 40:
        break