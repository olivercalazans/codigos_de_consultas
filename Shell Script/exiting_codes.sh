#!/bin/bash

# O comando "exit" encerra o código. Porém ele pode informa seu status com os códigos de saída.
# O código de saída é usado para informar o processo pai sobre o status na saída.
# Usa-se um número de 0 - 255. O 0 informa sucesso, qualquer outro número informa um erro.
# EX.:

echo "Hello, world"
exit 0

# Quando o comando exit de um script é usado sem um argumento de código de saída, o script retorna o código de saída do último comando que foi executado dentro do script.
