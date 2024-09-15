saldo = 0
operacoes = []
usuarios = []
contas = []
qtd_saques = 0
AGENCIA = "0001"
VALOR_LIMITE_SAQUES = 500.00
QTD_LIMITE_SAQUES = 3

def menu():
    print(
          """
            [1] Depositar
            [2] Sacar
            [3] Extrato
            [4] Criar usuário
            [5] Criar conta
            [Q] Sair
          """
         )

def depositar():
    global saldo
    
    valor = float(input("Informe o valor do depósito: "))
    if valor >= 0:
        saldo += valor
        operacoes.append(f"Valor R$ {valor:.2f} inserido na conta!")
    else:
        print("Falha! Valor menor que zero não pode ser usado para depósito.")
    
    return saldo, operacoes

def sacar():
    global qtd_saques
    global saldo

    valor = float(input("Informe o valor do saque: "))
    if (qtd_saques < QTD_LIMITE_SAQUES) and (valor <= VALOR_LIMITE_SAQUES):
        if saldo >= valor:
            if valor > 0:
                saldo -= valor
                operacoes.append(f"Valor {valor:.2f} sacado da conta!")
                qtd_saques += 1
            else:
                print("Falha! Informe um valor válido.")
        else:
            print("Falha! Não há saldo suficiente na conta. Não foi possível realizar a operação.")
    else:
        print(f"Falha! Valor maior que R$ {VALOR_LIMITE_SAQUES:.2f} ou limite de {QTD_LIMITE_SAQUES} saques excedido.")

def extrato():
    if len(operacoes) == 0:
        print("Não foram feitas operações na conta.")
    else:
        print(operacoes)
        print(f"Saldo: R$ {saldo:.2f}")

def criar_usuario():
    cpf = input("Informe o CPF do usuário: ")
    
    if filtrar_usuarios(cpf, usuarios):
        print("Erro!! Já existe um usuário com esse CPF!")
    else:
        nome = input("Informe o nome do usuário: ")
        data_nascimento = input("Informe a data de nascimento do usuário (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco, "cpf": cpf})

def criar_conta_corrente(cpf, agencia):
    if filtrar_usuarios(cpf, usuarios):
        if len(contas) > 0:
            contas.append({"agencia": agencia, "conta": contas[-1]["conta"] + 1, "cpf": cpf})
        else:
            contas.append({"agencia": agencia, "conta": 1, "cpf": cpf})
    else:
        criar_cpf = input("Usuário com esse CPF não existe. Responda com a tecla <S> se deseja criar usuário: ")
        if criar_cpf == 'S' or criar_cpf == 's':
            criar_usuario()

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados

while True:
    if len(usuarios) == 0:
        print("Não há usuários cadastrados. Redirecionando...")
        criar_usuario()
    
    if len(contas) == 0:
        print("Não há contas cadastradas. Redirecionando...")
        cpf = input("Informe o CPF do usuario: ")
        criar_conta_corrente(cpf, AGENCIA)

    menu()
    opcao = input("Informe a operação: ")

    if   opcao == '1':
        print("Identificando a conta...")
        conta = input("Informe a conta: ")
        depositar()
    elif opcao == '2':
        print("Identificando a conta...")
        conta = input("Informe a conta: ")
        sacar()
    elif opcao == '3':
        print("Identificando a conta...")
        conta = input("Informe a conta: ")
        extrato()
    elif opcao == '4':
        criar_usuario()
    elif opcao == '5':
        cpf = input("Informe o CPF do usuario: ")
        criar_conta_corrente(cpf, AGENCIA)
    elif opcao == 'q' or opcao == 'Q':
        break
    else:
        print("Operação inválida! Por favor, escolha novamente.")

print("Volte sempre!")