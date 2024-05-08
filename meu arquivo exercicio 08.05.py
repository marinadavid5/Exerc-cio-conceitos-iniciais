#1
def questao1 ():
    Nome = input ("Informe seu nome: ")
    f = open ('meu_arquivo_questao1.txt', 'w')
    f.write (Nome)
    f.close ()

#2
def questao2 ():
    variavel = input ("Escreva o nome de um arquivo de texto: ")
    f = open (variavel, 'w')
    conteudo = input ("Escreva o conteúdo a se impresso no arquivo: ")
    f.write (conteudo)
    f.close ()

#3
def questao3 ():
    f = open('arquivo-exemplo.txt', 'r')
    exemplo = f.read()

    f = open ('novo_arquivo_questao3.txt', 'w')
    f.write(exemplo) 
    f.close()

#4
def questao4 ():
    numero = input ("Escreva um número da lista: ")
    f = open ('arquivo-exemplo.txt', 'r')
    for linha in f:
        partes = linha.split (';')
        if numero == partes [0]:
            print (partes [1])
    f.close()


    

    
    
    
