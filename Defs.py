Lista_Nomes = []
def cabecalho():
    print('-'*34)
    print('\033[36m[1] Cadastrar Cliente\033[m')
    print('\033[36m[2] Cadastrar Endereço do Cliente\033[m')
    print('\033[36m[3] Consultar Cliente\033[m')
    print('\033[36m[4] Sair\033[m')
    print('-'*34)


def CadastrarCliente():
    print('[Forneça as informações do Cliente]')
    nome = str(input('Nome: ')).strip().lower()
    Lista_Nomes.append(nome)
    senha = str(input('Senha: '))
    email = str(input('E-mail: '))
    telefone = str(input('Telefone: '))
    matricula = str(input('Matrícula: '))
    with open(f'{nome}.txt', 'w') as arq:
        arq.write(f'Nome: {nome.capitalize()} \nSenha: {senha} \nE-mail: {email} \nTelefone: {telefone} \nMatricula: '
                  f'{matricula}')
    print('\033[32m[Cadastro Concluído]\033[m')


def CadastrarEnderecoCliente():
    usuario = str(input('Deseja cadastrar o endereço de qual usuário?: ')).strip().lower()
    while usuario not in Lista_Nomes:
        print('\033[33mVocê precisa digitar o nome de um cliente já cadastrado!\033[m')
        usuario = str(input('Deseja cadastrar o endereço de qual usuário?: ')).strip().lower()
    print('[Forneça o Endereço do usuário]')
    rua = str(input('Rua: '))
    numero_casa_ap = str(input('Nº Casa ou Apartamento: '))
    complemento = str(input('Complemento [Opcional]: '))
    bairro = str(input('Bairro: '))
    cidade = str(input('Cidade: '))
    estado = str(input('Estado: '))
    with open(f'{usuario}.txt', 'a') as arq:
        arq.write(f'\nRua: {rua} \nNumero Casa/Apartamento: {numero_casa_ap} \nComplemento: {complemento} \nBairro: '
                  f'{bairro} \nCidade: {cidade} \nEstado: {estado}')
        print('\033[32m[Endereço adicionado]\033[m')


def ConsultarCliente():
    nome_cliente = str(input('Nome do ciente: ')).strip().lower()
    while nome_cliente not in Lista_Nomes:
        print('\033[33mVocê precisa digitar o nome de um cliente já cadastrado!\033[m')
        nome_cliente = str(input('Nome do ciente: ')).strip().lower()
    print('-'*34)
    with open(f'{nome_cliente}.txt', 'r') as arq:
        for i in arq:
            print(i)


def SairCadastro():
    from time import sleep
    print('Saindo do sistema, aguarde...')
    sleep(3)
    print('Sistema finalizado com sucesso!')


