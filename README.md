Cadastro de Clientes:

O programa possui dois arquivos principais de código. O primeiro é o arquivo 'Defs.py' que possuiu as funções que definem
o funcionamento do programa, e o segundo arquivo 'Main.py' vai importar essas funcões do arquivo Defs.py e 
executa-las na ordem proposta.

A função Cabecalho() vai exibir o menu inicial na tela. A partir dela o usuário poderá escolher qualquer
alternativa mostrada.

A função CadastrarClientes() vai pedir que o usuário forneça as informações e logo em seguida criará um arquivo .txt com o 
nome do cliente, armazenando assim todas as informações correspondentes.

A função CadastrarEnderecoCliente() permitirá que o usuário adicione um endereço ao cliente. O nome do cliente deve ser 
digitado. Se o usuário digitar o nome de um cliente que não foi efetuado o cadastro, aparecerá um erro na tela. Caso
contrário as informações de endereço serão adicionadas ao arquivo .txt correspondente ao nome do cliente digitado. Podem
ser adicionados quantos endereços o usuário quiser a um mesmo cliente.

A função ConsultarCliente() exibirá na tela as informações do cliente digitado pelo usuário. Caso o usuário digitar o 
nome de um cliente que não foi efetuado o cadastro, aparecerá um erro na tela. O usuário pode mostrar as informações do
cliente na tela quantas vezes ele quiser.

Por fim, a função SairCadastro() exibe uma mensagem dizendo que o programa está sendo finalizado e termina o programa.

O programa ainda conta com alguns tratamentos de erro, caso o usuário digite algo que esteja diferente do pedido na tela!