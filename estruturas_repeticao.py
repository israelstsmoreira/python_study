numero = 1 
VOGAIS = "AEIOU"

nome = input("Digite seu nome: ")
    #posso criar uma variável para guardar os caracteres ou valores para gerar uma comparação e gerar açoes atravez dela
for letra in nome: #para cada letra em nome
    if letra.upper() in VOGAIS: #se a letra estiver em VOGAIS
        print(letra, end=" ") #printa a letra com espaço
#endf 
print()

for numero in range(0, 10, 2): #para numero num raio de 0 a 10 de 2 em 2
    print(numero, end = " ") #printa o numero até o 10 com um espaço ao final | quando colocamos o espaço ele n quebra alinha
#endf numero
