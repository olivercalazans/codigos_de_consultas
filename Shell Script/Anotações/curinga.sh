#!/bin/bash

# O Linux usa o ponto '.' como curinga para substituir por qualquer caracter de uma string.
# Por exemplo: 'c.t' poderia ser 'cat', 'cet', 'cit', 'cot', 'cut', ...
#     - Isso inclui vogais, números, etc.
#
# Ex.:

echo -e '\n##### EXEMPLO 1: UM PONTO'
cat /etc/group | grep "s.s"
#
echo -e '\n##### EXEMPLO 2: DOIS PONTOS'
cat /etc/netconfig | grep "..p"
#
# OBS. 1: UM ÚNICO '.' APENAS SUBSTITUI UM ÚNICO CARACTER.
# OBS. 2: DOIS PONTOS SUBSTITUEM DOIS CARACTERES E ASSIM POR DIANTE.


  
# Porém, é possível ser específico nos caracteres que serão usados.
# Para isso usa-se '[]'. Dentro deles, coloca-se o caracter desejado.
#
echo -e '\n##### EXEMPLO 3.1: UM CARACTER ESPECÍFICO'
ip -c a | grep "f[e]0"
#
echo -e '\n##### EXEMPLO 3.2: UM CARACTER ESPECÍFICO'
ip -c a | grep "e[n]s"

echo

# Para poder procurar qualquer string com um ou mais caracteres de uma vez, deve-se usar um asterisco (*) fora das '[]'.
# Dessa forma, os caracteres especificados serão procurados de sozinhos e em conjunto.
#
echo -e '\n##### EXEMPLO 4.1: CARACTERES ESPECÍFICOS'
ip -c a | grep "f[e8]*0"
#
echo -e '\n##### EXEMPLO 4.2: CARACTERES ESPECÍFIOS 2'
ip -c a | grep "s[acto03]"
#
# OBS.: DESSA FORMA, ELE MOSTRA OS RESULTADOS COM QUALQUER QUANTIDADE USANDO OS CARACTERES ESPECÍFICADOS.

echo

# É possível misturar as duas formas acima. Porém, ela aceita qualquer caracter depois ou antes dos específicados.
# Dependendo da forma escolhida, ela pode mostrar resultados com um caracter genérico ou vários.
#
echo -e '\n##### EXEMPLO 5.1: UM ÚNICO CARACTER GENERICO APÓS OS ESPECÍFICADOS'
ip -c a | grep "s[ct]*."
# 
echo -e '\n##### EXEMPLO 5.2: QUALQUER QUANTIDADE DE CARACTERES GENÉRICOS APÓS OS ESPECÍFICADOS'
ip -c a | grep "s[ct].*"

echo

# Também é possível escolher a quantidade de caracteres entre os desejados.
# Porém, a quantidade é escolhida, mas os caracteres não. Os caracteres que serão mostrados serão genéricos.
#
echo -e '\n##### EXEMPLO 6.1: QUANTIDADE DE CARACTERES GENÉRICOS'
ip -c a | grep "f.\{1\}0"
#
echo -e '\n##### EXEMPLO 6.2 '
ip -c a | grep "f.\{2\}0"

