#!/bin/bash

###### COMANDO NO SSH
#
## FORMA ESTRUTURAL: ssh <usuário>@<ip/nome_servidor> "<comando>" 
# 
ssh user@servidor "ip -c a | grep -e 'wlan' -e 'enp0s.' -e"
#
# A conexão ssh é feita e o comando será executado. Após isso, a conexão é fechada.
# O(s) comando(s) deve(m) ser colocado(s) da mesma forma que na linha de comando em uma única linha.
