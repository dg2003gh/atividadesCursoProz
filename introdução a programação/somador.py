def calculadora(num1, num2, operacao):
    if operacao == "somar":
        resultado = num1 + num2
    elif operacao == "subtrair":
        resultado = num1 - num2
    elif operacao == "multiplicar":
        resultado = num1 * num2
    elif operacao == "divisão":
        resultado = num1 / num2

    return resultado

print(calculadora(1, 2, "somar"))
