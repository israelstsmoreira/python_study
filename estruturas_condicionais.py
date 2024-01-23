conta_universitaria = False
conta_normal = True

saldo = 2000
cheque_especial = 450
saque = 2002

if conta_normal:
	if saldo >= saque:
		print("Saque efetuado com sucesso!")
	elif saque <= (saldo + cheque_especial):
		print("Saque efetuado com uso do cheque especial")
	else:
		print("saldo insuficiente!")
if conta_universitaria:
	if saldo >= saque:
		print("Saque realizado com sucesso!")
	else:
		print("Saldo insuficiente!")
else:
    print("O sistema não reconhece seu tipo de conta, por favor contatar seu gerente!")