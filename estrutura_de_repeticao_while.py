opcao = -1
saldo = 1000

while opcao != 0:
    opcao = int(input("Digite [1] para sacar, [2] para depositar e [0] para sair: "))
    if opcao == 1:
       saque = int(input("Digite o valor a ser sacado: "))
       if saldo >= saque:
            print("Sacando...")
            saldo -= saque
            print(f"Novo valor em conta: {saldo}")
       else:
           print("Saldo insuficiente!")
    
    if opcao == 2:
        saldo += int(input("Digite o valor a ser depositado: "))
        print(f"valor em conta = {saldo}")