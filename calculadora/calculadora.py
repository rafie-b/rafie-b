from operacoes import soma, subtracao, multiplicacao, divisao, potencia, raiz_quadrada, logaritmo

def menu():

    print("Selecione a operação desejada:")

    print("1 - Soma")

    print("2 - Subtração")

    print("3 - Multiplicação")

    print("4 - Divisão")

    print("5 - Potenciação")

    print("6 - Raiz Quadrada")

    print("7 - Logaritmo")

    opcao = int(input("Digite a opção desejada: "))

    return opcao



def calculadora():

    opcao = menu()



    if opcao == 1:

        a = float(input("Digite o primeiro número: "))

        b = float(input("Digite o segundo número: "))

        resultado = soma(a, b)

        print("O resultado da soma é:", resultado)

    elif opcao == 2:

        a = float(input("Digite o primeiro número: "))

        b = float(input("Digite o segundo número: "))

        resultado = subtracao(a, b)

        print("O resultado da subtração é:", resultado)

    elif opcao == 3:

        a = float(input("Digite o primeiro número: "))

        b = float(input("Digite o segundo número: "))

        resultado = multiplicacao(a, b)

        print("O resultado da multiplicação é:", resultado)

    elif opcao == 4:

        a = float(input("Digite o primeiro número: "))

        b = float(input("Digite o segundo número: "))

        resultado = divisao(a, b)

        print("O resultado da divisão é:", resultado)

    elif opcao == 5:

        a = float(input("Digite o número base: "))

        b = float(input("Digite o expoente: "))

        resultado = potencia(a, b)

        print("O resultado da potenciação é:", resultado)

    elif opcao == 6:

        a = float(input("Digite o número: "))

        resultado = raiz_quadrada(a)

        print("O resultado da raiz quadrada é:", resultado)

    elif opcao == 7:

        a = float(input("Digite o número: "))

        resultado = logaritmo(a)

        print("O resultado do logaritmo é:", resultado)

    else:

        print("Opção inválida")



if __name__ == '__main__':

    calculadora()