from time import sleep

while True:
        #coleta e tratamento de erros 
        try:
            quantidade_de_rodas = int(input('Quantas rodas seu veículo possue? '))
            peso_bruto = float(input('Qual o peso bruto de seu veículo?(KG) '))
            pessoas_veiculo = int(input('Quantas pessoas estão no veículo?'))

        except:
            print('Todas as informações devem ser números. ')

        else:
                print('Processando informações...')
                sleep(2)
                
                #condições
                if quantidade_de_rodas <= 3:
                    print(f'Um veículo com {quantidade_de_rodas} rodas, {peso_bruto}KG e que acomoda {pessoas_veiculo} pessoas se enquadra na categoria A.')
                    
                elif quantidade_de_rodas == 4 and pessoas_veiculo <= 8 and peso_bruto <= 3500:
                    print(f'Um veículo com {quantidade_de_rodas} rodas, {peso_bruto}KG e que acomoda {pessoas_veiculo} pessoas se enquadra na categoria B.')
                    
                elif quantidade_de_rodas >= 4 and  3500 <= peso_bruto <= 6000:
                    print(f'Um veículo com {quantidade_de_rodas} rodas, {peso_bruto}KG e que acomoda {pessoas_veiculo} pessoas se enquadra na categoria C.')
                    
                elif quantidade_de_rodas >= 4 and  pessoas_veiculo > 8:
                    print(f'Um veículo com {quantidade_de_rodas} rodas, {peso_bruto}KG e que acomoda {pessoas_veiculo} pessoas se enquadra na categoria D.')
                    
                elif quantidade_de_rodas >= 4 and  peso_bruto > 6000:
                    print(f'Um veículo com {quantidade_de_rodas} rodas, {peso_bruto}KG e que acomoda {pessoas_veiculo} pessoas se enquadra na categoria E.')   
                else:
                    print(f'Um veículo com {quantidade_de_rodas} rodas, {peso_bruto}KG e que acomoda {pessoas_veiculo} pessoas não se enquadra em nenhuma categoria.')
            
        # tratar se continua ou não no programa
        continuar = input('Deseja consultar outro veículo?').lower()
        
        match continuar:
            case 'sim' | 'yep' | 'continuar' | 'claro'|'com certeza'| 'pode ser'| 'vamos lá' | 'yes':
                continue
            case _:
                break
            
            

