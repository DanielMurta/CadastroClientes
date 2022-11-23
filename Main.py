import Defs  # Importa as funções do módulo 'Defs.py'

while True:
    Defs.cabecalho()
    opcao = input('Opção: ').strip()
    if opcao.isdigit():  # Verifica se a opcao digitado é um número
        opcao = int(opcao)
        if opcao == 1:
            while True:
                Defs.CadastrarCliente()
                r = str(input('Deseja cadastrar outro cliente?[S/N]: ')).strip().upper()
                if r == 'N':
                    break
                while r != 'S':
                    print('\033[31mERRO! Digite uma opção válida!\033[m')
                    r = str(input('Deseja cadastrar outro cliente?[S/N]: ')).strip().upper()
                    if r == 'N':
                        break
                if r == 'N':
                    break


        if opcao == 2:
            while True:
                Defs.CadastrarEnderecoCliente()
                r = str(input('Deseja cadastrar outro endereço?[S/N]: ')).strip().upper()
                if r == 'N':
                    break
                while r != 'S':
                    print('\033[31mERRO! Digite uma opção válida!\033[m')
                    r = str(input('Deseja cadastrar outro endereço?[S/N]: ')).strip().upper()
                    if r == 'N':
                        break
                if r == 'N':
                    break


        if opcao == 3:
            while True:
                Defs.ConsultarCliente()
                r = str(input('Deseja consultar outro cliente?[S/N]: ')).strip().upper()
                if r == 'N':
                    break
                while r != 'S':
                    print('\033[31mERRO! Digite uma opção válida!\033[m')
                    r = str(input('Deseja consultar outro cliente?[S/N]: ')).strip().upper()
                    if r == 'N':
                        break
                if r == 'N':
                    break


        if opcao == 4:
            Defs.SairCadastro()
            break

        if opcao > 4:
            print('\033[31mEsse número não corresponde a nenhuma opção!\033[m')

    else:
        print('\033[31mDigite um valor numérico!\033[m')







