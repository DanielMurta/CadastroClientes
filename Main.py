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





