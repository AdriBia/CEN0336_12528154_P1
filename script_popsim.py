#!/usr/bin/env python3

## Tamanho da população (P0)
P0 = input("Digite o tamanho inicial da população: ") # pede ao usuário que insira o tamanho inicial da população.

# verificar que a entrada é positiva e inteira:
if not P0.isdigit():
	print("Por favor, certifique-se de que o tamanho da população seja um número inteiro e positivo")
	exit(1) # finaliza o programa caso os requisitos não sejam atendidos.

P0 = int(P0) # armazena o tamanho inicial como um inteiro.

## Taxa de crescimento (r):
r = input("Digite a taxa de crescimento anual em decimais (ex: 0.05 para 5%): ") # pede ao usuário que insira a taxa de crescimento.

# verificar se a entrada é positiva:
if not r.replace(".","",1).isdigit():
	print("Por favor, certifique-se de que o crescimento seja positivo")
	exit(1) # encerra o programa caso os requisitos não sejam atendidos.

r = float(r) # armazena a taxa de  crescimento como um float.

## Tempo (t)
t = input("Digite o número de anos: ") # pede ao usuário que insira um número de anos.

# verificar se o número de anos é inteiro e positivo.
if not t.isdigit():
	print("Por favor, certifique-se de que o número de anos seja positivo e inteiro")
	exit(1)

t = int(t) # Armazena o tempo como um inteiro.

## Calculo do tamanho da população por ano
populacao = P0 # assume populacao como o tamanho inicial

for ano in range(1, t + 1):
    populacao = populacao * (1 + r)  # Aplicando a fórmula de crescimento
    print(f"A população instantânea para o Ano {ano} é: {populacao:.4f}")
