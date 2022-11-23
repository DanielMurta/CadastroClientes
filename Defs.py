Lista_Nomes = []

# Função p/ mostrar o menu principal
def cabecalho():
    print('-'*34)
    print('\033[36m[1] Cadastrar Cliente\033[m')
    print('\033[36m[2] Cadastrar Endereço do Cliente\033[m')
    print('\033[36m[3] Consultar Cliente\033[m')
    print('\033[36m[4] Sair\033[m')
    print('-'*34)

# Função que cadastra um cliente
def CadastrarCliente():
    print('[Forneça as informações do Cliente]')
    nome = str(input('Nome: ')).strip().lower()
    Lista_Nomes.append(nome)
    senha = str(input('Senha: '))
    email = str(input('E-mail: '))
    telefone = str(input('Telefone: '))
    matricula = str(input('Matrícula: '))
    with open(f'{nome}.txt', 'w') as arq:  # Cria o arquivo .txt com o nome do cliente
        arq.write(f'Nome: {nome.capitalize()} \nSenha: {senha} \nE-mail: {email} \nTelefone: {telefone} \nMatricula: '
                  f'{matricula}')  # Escreve as informações do cliente dentro do arquivo
    print('\033[32m[Cadastro Concluído]\033[m')

# Cadastra endereço do cliente
def CadastrarEnderecoCliente():
    usuario = str(input('Deseja cadastrar o endereço de qual usuário?: ')).strip().lower()
    while usuario not in Lista_Nomes:  # Verifica se o cliente digitado já está cadastrado
        print('\033[33mVocê precisa digitar o nome de um cliente já cadastrado!\033[m')
        usuario = str(input('Deseja cadastrar o endereço de qual usuário?: ')).strip().lower()
    print('[Forneça o Endereço do usuário]')
    rua = str(input('Rua: '))
    numero_casa_ap = str(input('Nº Casa ou Apartamento: '))
    complemento = str(input('Complemento [Opcional]: '))
    bairro = str(input('Bairro: '))
    cidade = str(input('Cidade: '))
    estado = str(input('Estado: '))
    with open(f'{usuario}.txt', 'a') as arq:  # Abre o arquivo do cliente digitado
        arq.write(f'\nRua: {rua} \nNumero Casa/Apartamento: {numero_casa_ap} \nComplemento: {complemento} \nBairro: '
                  f'{bairro} \nCidade: {cidade} \nEstado: {estado}')  # Insere as informações do endereço dentro do
        print('\033[32m[Endereço adicionado]\033[m')                  # arquivo

# Consulta cliente
def ConsultarCliente():
    nome_cliente = str(input('Nome do ciente: ')).strip().lower()
    while nome_cliente not in Lista_Nomes:  # Verifica se o cliente digitado já está cadastrado
        print('\033[33mVocê precisa digitar o nome de um cliente já cadastrado!\033[m')
        nome_cliente = str(input('Nome do ciente: ')).strip().lower()
    print('-'*34)
    with open(f'{nome_cliente}.txt', 'r') as arq:  # Abre o arquivo do cliente digitado
        for i in arq:  # Printa as informações do cliente na tela
            print(i)

# Encerra o programa
def SairCadastro():
    from time import sleep
    print('Saindo do sistema, aguarde...')
    sleep(3)
    print('Sistema finalizado com sucesso!')




