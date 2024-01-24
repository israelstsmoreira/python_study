nome = "Israel dos Santos Moreira"
print(nome[0])
print(nome[:6]) #se não colocar o em qual posição desejamos começar, ele pega desde o inicio 
print(nome[11:17]) #colocamos para começar no caractere de indice 11(começando do zero)e parar no de indice 17
print(nome[11:17:2]) #colocamos ele para começar da letra de indice 11 e pegar de 2 em 2 até a de indice 17
print(nome[:])  #pega toda a string
#metodo para espelhar uma string 
print(nome[:: -1])