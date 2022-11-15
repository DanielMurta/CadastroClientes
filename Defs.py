def cabeçalho():
    print('-'*34)
    print('[1] Cadastrar Cliente')
    print('[2] Cadastrar Indereço do Cliente')
    print('[3] Consultar Cliente')
    print('[4] Sair')
    print('-'*34)

def CadastrarCliente():
    print('[Forneça as informações do Cliente]')
    nome = str(input('Nome: '))
    senha = str(input('Senha: '))
    email = str(input('E-mail: '))
    telefone = int(input('Telefone: '))
    matricula = int(input('Matrícula: '))
    print('[Cadastro Concluído]')

