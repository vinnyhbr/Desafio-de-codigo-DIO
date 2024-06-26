def verificar_cpf_existente(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return True
    return False

def cadastrar_usuario(usuarios):
    while True:
        nome_completo = input("Informe o nome completo do usuário: ")
        cpf = input("Informe o CPF do usuário: ")
        endereco = input("Informe o endereço do usuário: ")
        data_nascimento = input("Informe a data de nascimento do usuário (dd/mm/aaaa): ")
        saldo = float(input("Informe o saldo inicial: "))
        
        if verificar_cpf_existente(cpf, usuarios):
            print("Erro: Este CPF já está cadastrado.")
        else:
            usuarios.append({'nome_completo': nome_completo, 'cpf': cpf, 'endereco': endereco, 'data_nascimento': data_nascimento, 'saldo': saldo})
            print("Usuário cadastrado com sucesso!")
            break

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite_saques, limite):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso!")
        if numero_saques == limite_saques:
            print("Atenção: Você atingiu o limite de saques.")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def credito(saldo, extrato):
    valor = float(input("Informe o valor do crédito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Crédito: R$ {valor:.2f}")
        print("Crédito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    usuarios = []
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input("""
[c] Cadastrar Usuário
[d] Depositar
[s] Sacar
[u] Crédito
[e] Extrato
[q] Sair

=> """)
        if opcao == "c":
            cadastrar_usuario(usuarios)
        elif opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite)
        elif opcao == "u":
            saldo, extrato = credito(saldo, extrato)
        elif opcao == "e":
            extrato(saldo, extrato)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
