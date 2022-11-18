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


def CadastrarEndereçoCliente():
    usuario = str(input('Deseja cadastrar o endereço de qual usuário?: '))
    print('[Forneça o Endereço do usuário]')
    rua = str(input('Rua: '))
    numero_casa_ap = str(input('Nº Casa ou Apartamento: '))
    complemento = str(input('Complemento [Opcional]: '))
    bairro = str(input('Bairro: '))
    cidade = str(input('Cidade: '))
    estado = str(input('Estado: '))


def ConsultarCliente():
    nome_cliente = str(input('Nome do ciente: '))


def SairCadastro():
    from time import sleep
    print('Saindo do sistema, aguarde...')
    sleep(3)
    print('Sistema finalizado com sucesso!S')
