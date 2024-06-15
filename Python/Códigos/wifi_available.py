# --------------------------------------------------------------------------------
# Este exemplo lista as redes WIFI disponíveis.
# --------------------------------------------------------------------------------

import subprocess 

# Executa o comando 'netsh wlan show network' e captura a saída
devices = subprocess.check_output(['netsh','wlan','show','network']) 

# Decodifica a saída em uma string usando a codificação 'utf-8' e lida com erros usando 'backslashreplace'
devices = devices.decode('utf-8', errors ='backslashreplace').split('\n')

# Cria listas com informações específicas das redes Wi-Fi
# Aqui, o código percorre as linhas em 'devices' e extrai informações com base em palavras-chave
redes_list     = [a.split(":")[1][1:-1] for a in devices if 'SSID' in a]
autentica_list = [a.split(":")[1][1:-1] for a in devices if 'Autentica' in a]
cripto_list    = [a.split(":")[1][1:-1] for a in devices if 'Criptografia' in a]
tipo_list      = [a.split(":")[1][1:-1] for a in devices if 'Tipo' in a]

# Cria um dicionário para armazenar as informações das redes Wi-Fi
redes_dict = dict()

# Percorre a lista 'redes_list' e cria um dicionário 'redes_dict' com informações organizadas
posicao = 0
for rede in redes_list:
    redes_dict[rede] = {
            'TipoRede'    : tipo_list[posicao],
            'Autenticacao': autentica_list[posicao],
            'Criptografia': cripto_list[posicao]
        }
    posicao += 1

# Exibe as informações formatadas em um formato tabular
for key in redes_dict.keys():
    print(f'{key:<30} | {redes_dict[key]["TipoRede"]:<20} | {redes_dict[key]["Autenticacao"]:<20} | {redes_dict[key]["Criptografia"]}')

