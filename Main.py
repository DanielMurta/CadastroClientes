import Defs

while True:
    Defs.cabeçalho()
    opcao = int(input('Opção: ').strip())
    if opcao == 1:
        while True:
            Defs.CadastrarCliente()
            r = str(input('Deseja cadastrar outro cliente?[S/N]: ')).strip().upper()
            if r == 'N':
                break

    if opcao == 2:
        while True:
            Defs.CadastrarEndereçoCliente()
            r = str(input('Deseja cadastrar outro endereço?[S/N]: ')).strip().upper()
            if r == 'N':
                break

    if opcao == 3:
        while True:
            Defs.ConsultarCliente()
            r = str(input('Deseja consultar outro cliente?[S/N]: ')).strip().upper()
            if r == 'N':
                break


    if opcao == 4:
        Defs.SairCadastro()
        break






