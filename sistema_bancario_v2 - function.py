    
# def menu():
#     print("""
#     ===== MENU =====
#     [d]     Depositar
#     [s]     Sacar
#     [e]     Extrato
#     [nc]    Nova Conta
#     [lc]    Listar Contas
#     [nu]    Novo Usuário
#     [q]     Sair
#     """)
        
#     return (input("Digite a opção desejada: "))
    

# def depositar(saldo, valor_deposito, extrato):
#     if valor_deposito > 0:
#         saldo += valor_deposito
        
#         print(f"Valor depositado com sucesso. Seu novo saldo é de {saldo:.2f}")
#         extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
       
    
#     else:
#         print("Digite um valor válido")
        
#     return saldo, extrato

# def sacar(*, saldo, extrato, numero_saques, limite, limite_saques, valor_saque):
#     excedeu_saldo = valor_saque > saldo
#     excedeu_limite = valor_saque > limite
#     excedeu_limite_saques = numero_saques >= limite_saques
    
#     if excedeu_saldo:
#         print("Você não possui saldo suficiente")
        
    
#     elif excedeu_limite:
#         print("O limite para esta operação é de R$500,00")
        
    
#     elif excedeu_limite_saques:
#         print("Você ultrapassou o limite diário de saques")
        
    
#     elif valor_saque > 0:
#         saldo -= valor_saque
        
#         extrato += f"Saque: R$ {valor_saque:.2f}\n"
#         numero_saques +=1
#         print(f"Saque realizado com sucesso. Seu novo saldo é de: R$ {saldo}")
    
#     else:
#         print("informe um valor válido")
    
#     return saldo, extrato, numero_saques

# def exibir_extrato(saldo, extrato):
#     print("""
#           ====== EXTRATO ======
          
#           """)
#     print("Não foram realizadas movimentações" if not extrato else extrato)
#     print(saldo)
    
# def criar_usuario(usuarios):
#     cpf = input("Digite o número do CPF (Apenas números): ")
#     usuario = verificar_usuario(cpf, usuarios)
    
#     if usuario:
#         print("Este numero de CPF já foi cadastrado")
        
#     else:
#         nome = input("Digite seu nome completo: ")
#         data_nascimento = input("Digite a sua data de nascimento: ")
#         endereço = input("Digite o seu endereço completo (Rua, nro. bairro - cidade - estado)")
        
#         usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereço })
        
#         print("Usuario cadastrado com sucesso")
                
# def verificar_usuario(cpf, usuarios):
#     usuario_existe = [ usuario for usuario in usuarios if usuario["cpf"] == cpf] 
#     return usuario_existe[0] if usuario_existe else None

# def criar_conta(usuarios, agencia, numero_conta):
#     cpf = input("Digite o número do CPF(apenas dígitos): ")
#     usuario = verificar_usuario(cpf, usuarios)
    
#     if usuario:
#         print("Conta criada com sucesso")
        
#         return{"usuario": usuario, "agencia": agencia, "numero_conta": numero_conta}

#     else:
#         print("Usuário não encontrado, por gentileza cadastrar um usuário ")        

# def listar_contas(contas_bancarias):

#     for conta in contas_bancarias:

#         contas_cadastro = f"""
#         Titular: {conta["usuario"]["nome"]};
#         Agência: {conta["agencia"]};
#         C/C: {conta["numero_conta"]};
#         """
#         print(contas_cadastro)
    

 
# def main():
    
#     saldo = 0
#     extrato = ""
#     numero_saques = 0
#     usuarios = []
#     contas_bancaria = []
#     LIMITE_SAQUES = 3
#     LIMITE = 500
#     AGENCIA = "0001"
    
#     while True:
#         opcao = menu()
        
#         if opcao == "d":
#             print("Opção Depositar:")
#             valor_deposito = float(input("Digite o valor a ser depositado: "))
            
#             saldo, extrato = depositar(saldo, valor_deposito, extrato )
        
#         elif opcao == "s":
#             print("Opção sacar")
#             valor_saque = float(input("Informe o valor que deseja sacar: "))
            
#             saldo, extrato, numero_saques = sacar(
#                 saldo=saldo, 
#                 extrato=extrato, 
#                 valor_saque=valor_saque,
#                 numero_saques=numero_saques, 
#                 limite=LIMITE, 
#                 limite_saques=LIMITE_SAQUES ) 
        
#         elif opcao =="e":
#             print("Opção Extrato:")
#             exibir_extrato(saldo, extrato = extrato)
            
#         elif opcao =="nu":
#            print("Opção Criar usuário:")
           
#            criar_usuario(usuarios)

#         elif opcao =="nc":
#             print("Opção Criar Conta")
            
#             numero_conta = len(contas_bancaria) + 1
#             conta = criar_conta(usuarios, AGENCIA, numero_conta)
            
#             if conta:
#                 contas_bancaria.append(conta)
#                 print(contas_bancaria)

#         elif opcao =="lc":
#             print("Opção Listar Contas")
            
#             listar_contas(contas_bancaria)
            
#         elif opcao =="q":
#             break

# main()

consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:

def recomendar_plano(consumo):
  if consumo <= 10:
    return"Plano Essencial Fibra - 50Mbps"
  
  elif consumo >10 and consumo <=20:
    return"Plano Prata Fibra - 100Mbps"
  
  else:
    return("Plano Premium Fibra - 300Mbps")

print(recomendar_plano(consumo))