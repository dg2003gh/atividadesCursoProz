qualOpção = """=-- Operações --=
1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair
==========-==========
Qual operação será?
"""

def calculadora():

    while True:

        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))
        operacao = int(input(qualOpção))

        if operacao == 0:
            break
        elif operacao == 1:
            resultado = num1 + num2
        elif operacao == 2:
            resultado = num1 - num2
        elif operacao == 3:
            resultado = num1 * num2
        elif operacao == 4:
            resultado = num1 / num2
        else:
            resultado = "esta opção não existe"

        return print(resultado)


calculadora()
