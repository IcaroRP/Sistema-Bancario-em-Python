from services.menu import *

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()
        if opcao == 'd':
            depositar(clientes)
        elif opcao == 's':
            sacar(clientes)
        elif opcao == 'e':
            exibir_extrato(clientes)
        elif opcao == 'nu':
            criar_cliente(clientes)
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'q':
            break
        else:
            print('\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@')

if __name__ == "__main__":
    main()