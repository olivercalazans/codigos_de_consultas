#!/bin/bash

# Os operadores lógico são:
###    -gt ... greater than (maior que).
###    -ge ... greater than or equal to (maior que ou igual a).
###    -lt ... less than (menor que).
###    -le ... less than or equal to (menor que ou igual a).
###    -eq ... equal to (igual a).
###    -ne ... not equal (não igual).

###    = .... atribui valor a uma variável.
###    == ... compara dois valores.
###    != ... diferencia dois valores.

###    -z ... verifica se a string está vazia.
string1="Hello"
if [ -z "$string1" ]; then
    echo "A string1 está vazia."
else
    echo "A string1 não está vazia."
fi


###    -n ... verifica se a string não está vazia.
string2=""
if [ -n "$string2" ]; then
    echo "A string2 não está vazia."
else
    echo "A string2 está vazia."
fi


###    -f ... verifica se um arquivo existe.
file="example.txt"

if [ -f "$file" ]; then
    echo "O caminho $file corresponde a um arquivo regular."
else
    echo "O caminho $file não corresponde a um arquivo regular."
fi


###    -d ... verifica se um diretório existe.
directory="/path/to/directory"

if [ -d "$directory" ]; then
    echo "O caminho $directory é um diretório."
else
    echo "O caminho $directory não é um diretório."
fi


###    -r ... verifica se o usuário tem permissão de leitura.
file="example.txt"

if [ -r "$file" ]; then
    echo "O arquivo $file tem permissão de leitura para o usuário."
else
    echo "O arquivo $file não tem permissão de leitura para o usuário."
fi


###    -L ... verifica se o arquivo é um link simbólico.
file="example.txt"

if [ -L "$file" ]; then
    echo "O arquivo $file é um link simbólico."
else
    echo "O arquivo $file não é um link simbólico."
fi
