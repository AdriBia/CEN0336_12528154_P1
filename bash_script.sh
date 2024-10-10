#!/bin/bash

## Um comando que mostre a pasta/diretorio:
echo "Pasta/diretorio atual:";pwd
# o comando echo equivale ao print em python, indicando a mensagem a ser exibida na tela, tornando mais informativo ao usuario.
# pwd e o comando que mostra a localizacao atual.

## Um comando que gere uma lista detalhada e a redirecione a lista para o arquivo lista_HOME.txt
echo "a lista detalhada de conteúdos em HOME foram salvos em 'lista_HOME.txt'"
ls -l ~> lista_HOME.txt

# ls e o comando utilizado para mostrar o conteúdo de uma localizacao especifica, adicionando -ls essa listagem passa a ser detalhada
# ~ indica que a acao anterior se aplica ao diretorio HOME.
# > direciona as informacoes obtidas do comando ao arquivo, nesse caso inexistente agora sendo criado.
# para exibir o conteúdo armazenado em lista_HOME.txt adicionar o comando cat lista_HOME.txt

## Um comando que imprima a data atual na tela
echo "data:"; date +"%d-%m-%Y"

# O comando date exibe na tela a data atual, '+"%d-%m-%Y"' indica o formato em que a data deve aparecer, nesse caso: DD-MM-YYYY.
