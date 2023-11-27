menu = """

[1] Deposito
[2] Sacar
[3] Extrato
[0] Sair

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    

    if opcao == "1":
        deposito = float(input("Valor a do depósito: "))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:5.2f}\n"

        else:
            print("Não foi possivel fazer o depósito! Valor informado invalido, tente novamente!")


    elif opcao == "2":
        saque = float(input("Valor a ser sacado: "))
        
        if saque > limite:
            print("O valor a ser sacado excede o limite!")
        
        elif saque > saldo:
            print("Não á saldo suficiente!")
        
        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diarios atingido.")
        
        elif saque <= saldo:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque: R$ {saque:5.2f}\n"
        
        else:
            print("Não foi possivel fazer o saque! ")

    elif opcao == "3":
        print("\n=============== EXTRATO DETALHADO ===============")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:5.2f}")
        print("=================================================")

    elif opcao == "0":
        print("Obrigado por utilizar nosso banco!")
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")