def exibir_menu():
    menu_texto = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return input(menu_texto)

def realizar_deposito(saldo, extrato):
    valor_deposito = float(input("Informe o valor do depósito: "))
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato.append(f"Depósito: R$ {valor_deposito:.2f}")
        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def realizar_saque(saldo, extrato):
    valor_saque = float(input("Informe o valor do saque: "))
    if valor_saque <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif valor_saque > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    else:
        saldo -= valor_saque
        extrato.append(f"Saque: R$ {valor_saque:.2f}")
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
    return saldo, extrato

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimentacao in extrato:
            print(movimentacao)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    saldo = 0
    extrato = []

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = realizar_deposito(saldo, extrato)
        elif opcao == "s":
            saldo, extrato = realizar_saque(saldo, extrato)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "q":
            print("Obrigado por usar nosso sistema bancário. Até logo!")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()