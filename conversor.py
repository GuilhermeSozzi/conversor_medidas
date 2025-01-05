while True:
    print("\nOpções de conversão disponíveis:\n")
    print("1 - Celsius para Fahrenheint.")
    print("2 - Fahrenheint para Celsius.")
    print("3 - Metros para pés.")
    print("4 - Pés para metros.")

    lista = [1,2,3,4]

    try:
        opcao = int(input("\nDigite o número referente à conversão que deseja realizar:"))
    except ValueError:
        print("Valor de entrada inválido. Tente novamente com um número válido.")
        continue
    
    if opcao in lista:
        try:
            valor = float(input("Digite o valor numérico a ser convertido:"))
        except ValueError:
            print("Valor de entrada inválido. Digite um número na próxima tentativa.")
            continue
    else:
        print(f"Entrada inválida. {opcao} não é uma opção válida.")
        continue

    resultado = 0

    if opcao == 1:
        print("\nConvertendo Celsius para Fahrenheint.\nResultado:")
        resultado = (valor * 1.8) + 32
        print(resultado)
    elif opcao == 2:
        print("\nConvertendo Fahrenheint para Celsius.\nResultado:")
        resultado = (valor - 32) * (5/9)
        print(resultado)
    elif opcao == 3:
        print("\nConvertendo Metros para pés.\nResultado:")
        resultado = valor * 3.28084
        print(resultado)
    elif opcao == 4:
        print("\nConvertendo Pés para Metros.\nResultado:")
        resultado = valor * 0.3048
        print(resultado)

    print("\nDeseja realizar uma nova conversão?")
    print("1 para não.")
    print("Qualquer outra tecla para sim.")
    continuar = int(input())
    if continuar == 1:
        print("\nDesativando programa.")
        break