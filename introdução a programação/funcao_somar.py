def calculadora(v1, v2, operacao ):
        match operacao:
         case 'soma' | 'somar':
               resultado = v1 + v2      
        case 'sub' | 'subtracao':
                resultado = v1 - v2
        case 'multiplicacao' | 'multi':
                resultado = v1 * v2
        case 'divisao' | 'div'
                resutado = v1 / v2
                    
        return resultado
print(calculadora(1, 2, somar))
