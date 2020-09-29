"""
3. Escreva um programa que contenha as seguintes funções:
• ler: lê uma frase lida do teclado e devolve-a;
• gravar: grava para um ficheiro, cujo nome é passado como parâmetro, uma frase também passada como parâmetro à função;
• contaVogais: recebe uma frase e devolve o número de vogais.
Com as funções anteriores construa um programa que lê duas frases do teclado e grava para um ficheiro de texto a que tiver mais vogais. Confirme
abrindo o ficheiro criado num editor de texto.
"""
def ler():
    frase = input()
    return frase

def gravar(nome, frase):
    ficheiro = open(nome,'w')
    ficheiro.write(frase)
    ficheiro.close()

def contaVogais(frase):
    count = 0
    for i in frase:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            count = count + 1
    return count

frase1 = ler()
frase2 = ler()
if contaVogais(frase1) > contaVogais(frase2):
    gravar("Ficha 1/resultado.txt",frase1)
else:
        gravar("Ficha 1/resultado.txt",frase2)
