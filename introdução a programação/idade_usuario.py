rodando = True

while rodando:

    try:
        nome_do_usuario = str(input("Digite seu nome completo: "))
        data_de_nascimento_do_usuario = str(input("Digite a data do seu nascimento: "))

        if 1922 < data_de_nascimento_do_usuario > 2021:
            print("ERRO: ano de nascimento inválido!")
        else:
            print("Sua idade é", 2022 - data_de_nascimento_do_usuario)
            break
    except ValueError:
        print("os dados inseridos são inválidos!")

