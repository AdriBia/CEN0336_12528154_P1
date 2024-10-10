#!/usr/bin/env python3
import sys
#importa o modulo sys, que permite importar os parametros de linha de comando

if len(sys.argv) !=3:
	print ("Por favor, insira um numero inteiro e menor que 500 para cada um dos catetos")
	sys.exit(1)
# o comando confere se o usuario forneceu todas as informacoes necessarias, ou seja, os tres argumentos: nome do arquivo, cateto a e cateto b, caso contrario retorna uma mensagem solicitando as informacoes corretas

a_string = sys.argv[1]
b_string = sys.argv[2]
# recebe as informações fornecidas como cateto a e b como strings para que seja possivel conferir se sao numeros inteiros

if not a_string.isdigit() or not b_string.isdigit():
	print ("Por favor, os valores devem ser numeros inteiros positivos")
	sys.exit(1)
# verifica se a_string e b_string contém numeros inteiros, caso contrario retorna uma mensagem solicitando as informacoes corretas

a = int(a_string)
b = int(b_string)
# transforma a_string e b_string em inteiros (type=int) armazenando em a e b, respectivamente.

if a <= 0 or a >= 500 or b <= 0 or b >= 500:
	print("O comprimentos dos catetos devem ser numeros inteiros positivos e menores que 500")
# verifica se os inteiros sao positivos e menores que 500.

A = (a * b) / 2
# caso todos os requisitos sejam atendidos, realiza a funcao e armazena a informacao em A.

print(f"A area do triangulo retângulo de lados a= {a} e b= {b}, é {A}")
# retorna ao usuario uma mensagem com o resultado obtido.
