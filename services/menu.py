from models.transacoes import Saque, Deposito
from models.cliente import PessoaFisica
from models.conta import ContaCorrente
import textwrap

def menu():
    menu = """\n
    ============ MENU ============
    [D] \t Depositar
    [S] \t Sacar
    [E] \t Extrato
    [NC] \t Nova Conta
    [LC] \t Listar Contas
    [NU] \t Novo Usuário
    [Q] \t Sair
    """
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print('\n@@@ Cliente não possui conta! @@@')
        return None
    
    if len(cliente.contas) == 1:
        return cliente.contas[0]
    
    print('\nEscolha uma das contas: ')

    for i, conta in enumerate(cliente.contas, 1):
        print(f"[{i}] Conta número: {conta.numero}, Agência: {conta.agencia}")

    indice = int(input("Digite o número da conta desejada: ")) - 1

    if 0 <= indice < len(cliente.contas):
        return cliente.contas[indice]
    else:
        print("\n@@@ Opção inválida! @@@")
        return None

def selecionar_conta_por_cpf(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado: ")
        return None, None
    
    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return None, None
    
    return cliente, conta

def depositar(clientes):
    cliente, conta = selecionar_conta_por_cpf(clientes)
    if not cliente:
        return
    try:
        valor = float(input('Informe o valor do depósito: '))
        transacao = Deposito(valor)
    except ValueError:
        print("\n@@@ Valor inválido! Digite apenas números. @@@")
        return

    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cliente, conta = selecionar_conta_por_cpf(clientes)
    if not cliente:
        return
    try:
        valor = float(input('Informe o valor do saque: '))
        transacao = Saque(valor)
    except:
        print("\n@@@ valor inválido! Digite apenas npumeros. @@@")
        return

    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cliente, conta = selecionar_conta_por_cpf(clientes)
    if not cliente:
        return

    if not conta:
        return

    print("\n================ Extrato ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}: \n\tR${transacao['valor']:.2f}"
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("\n=========================================")

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado)")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")

def criar_conta(numero_conta, clientes, contas):
    cpf = input('Informe o cpf do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@')
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n === Conta criada com sucesso! ===")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))
