MENU = """
=========== MENU ===========

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

============================

=> """

LIMITE = 500
LIMITE_SAQUES = 3

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: R$ "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito:     R$ {valor:>7.2f}\n"
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("❌ Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(saldo, extrato, numero_saques):
    valor = float(input("Informe o valor do saque: R$ "))

    if valor <= 0:
        print("❌ Operação falhou! O valor informado é inválido.")

    elif valor > saldo:
        print("❌ Operação falhou! Você não tem saldo suficiente.")

    elif valor > LIMITE:
        print(f"❌ Operação falhou! Limite por saque é de R$ {LIMITE:.2f}.")

    elif numero_saques >= LIMITE_SAQUES:
        print("❌ Operação falhou! Número máximo de saques diários atingido.")

    else:
        saldo -= valor
        extrato += f"Saque:        R$ {valor:>7.2f}\n"
        numero_saques += 1
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso.")

    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, extrato):
    print("\n=========== EXTRATO ===========")
    print("Sem movimentações registradas." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("================================\n")

def despedida():
    print("""
============================
 Obrigado por usar o sistema 
        bancário 💰
       Até a próxima! 
============================
""")

def main():
    saldo = 0
    extrato = ""
    numero_saques = 0

    while True:
        opcao = input(MENU).lower()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)

        elif opcao == "e":
            mostrar_extrato(saldo, extrato)

        elif opcao == "q":
            despedida()
            break

        else:
            print("⚠️  Opção inválida! Tente novamente.")

main()
