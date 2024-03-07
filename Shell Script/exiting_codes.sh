#!/bin/bash

# O comando "exit" encerra o código. Porém ele pode informa seu status com os códigos de saída.
# O código de saída é usado para informar o processo pai sobre o status na saída.
# Usa-se um número de 0 - 255. O 0 informa sucesso, qualquer outro número informa um erro.
# EX.:

echo "Hello, world"
exit 0
