menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Opção escolhida: Depósito")
        valor_deposito = float(input("Informe o valor do depósito: "))
        
        if valor_deposito > 0:
            print(f"Depositando {valor_deposito}")
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"seu saldo atual é de: {saldo}")
        elif valor_deposito <=0:
            print("Valor inválido")
        
    elif opcao == "s":
        
        
        if numero_saques > LIMITE_SAQUES:
            print("Você excedeu a quantidade de saques diários")
            break
        
        valor_saque = float(input("Informe o valor que deseja sacar: "))
        
        excedeu_saldo = valor_saque > saldo
        
        excedeu_limite = valor_saque > limite
        
        if excedeu_saldo:
            print("você não tem saldo suficiente")
        
        elif excedeu_limite:
            print("você excedeu o limite de saque por transação")
            
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print(f"seu saldo atual agora é de {saldo}")
            
        else:
            print("Operação invalida")
            
    elif opcao == "e":
        print("\n === Extrato ===")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
       
    elif opcao == "q":
        break
    
    else:
        print("Operação falhou!")

