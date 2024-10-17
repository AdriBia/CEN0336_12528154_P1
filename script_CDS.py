#!/usr/bin/env python3

# importa a biblioteca sys, permitindo receber os parâmetros a partir da linha de comando
import sys

# testar o número de argumentos para garantir que sejam entregues sete argumentos
if len(sys.argv) != 8:
    print ("Por favor, informe os sete argumentos")
    exit(1) # o programa finaliza se não houver sete argumentos

# atribuir os sete argumentos as variaveis
DNA = (sys.argv[1])
n1 = (sys.argv[2])
n2 = (sys.argv[3])
n3 = (sys.argv[4])
n4 = (sys.argv[5])
n5 = (sys.argv[6])
n6 = (sys.argv[7])

# transforma a sequência de DNA deixando todas as letras maiusculas
DNA = DNA.upper()

# atribui o tamanho da sequência de DNA a uma variavel
tamanho = len(DNA)

# verifica se todos os argumentos são números inteiros e positivos
if n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit() and n5.isdigit() and n6.isdigit():
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    n4 = int(n4)
    n5 = int(n5)
    n6 = int(n6) 	# transforma todos os dados de string da linha de comando para numeros inteiros
    if not (0 < n1 <= tamanho and 0 < n2 <= tamanho and 0 < n3 <= tamanho and 0 < n4 <= tamanho and 0 < n5 <= tamanho and 0 < n6 <= tamanho):
        print ("Por favor, certifique-se de que os numeros sao positivos e não maiores do que o tamanho da sequencia de DNA")
        exit (1) 	# o programa finaliza se os números forem negativos ou maiores que o tamanho da sequência de DNA
else:
    print ("São esperados 6 números inteiros")
    exit (1)
# o programa finaliza se os argumentos não forem inteiros

# extrair a sequência do CDS1 e verificar se inicia com o códon ATG
cds1 = DNA[n1-1:n2] # subtrai 1 pois a sequência em python inicia em 0
if cds1[:3] != "ATG":
    print ("Por favor, certifique-se de que a sequência se inicia com o códon de iniciação ATG")
    exit(1) # caso a sequência não iniciar com o codon de iniciação ATG, o programa se encerra.


# extrair a sequência do CDS2:
cds2 = DNA[n3-1:n4]

# extrair a sequência do CDS3 e verificar se termina com um dos códons de parada
cds3 = DNA[n5-1:n6]
if cds3[-3:] != "TAG" and cds3[-3:] != "TAA" and cds3[-3:] != "TGA":
    print ("Por favor, certifique-se de que a sequencia termina com os códons de parada")
    exit(1) #O programa é encerrado se a sequência de DNA não finalizar com os códons de parada

# concatenar CDS1, CDS2 e CDS3
concat = cds1+cds2+cds3
print (concat)
