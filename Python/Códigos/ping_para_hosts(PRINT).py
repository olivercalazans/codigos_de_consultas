import subprocess, platform, re, ipaddress, socket, threading

def ping(host, mascara):

    def verificando_se_e_ip_ou_dominio(host, mascara):
        caracteresUsadosNoIpv4 = r'^(\d{1,3}\.){3}\d{1,3}$'
        caracteresUsadosNoIpv6 = r'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4})|(::([0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4})|(([0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4}::([0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4})|([0-9a-fA-F]{1,4}::)$'
        
        if re.match(caracteresUsadosNoIpv4, host) or re.match(caracteresUsadosNoIpv6, host):
            if '/' in mascara: mascara = mascara.replace('/','')
            
            if re.match(caracteresUsadosNoIpv4, host):   objetoComOsIps = ipaddress.IPv4Network(f"{host}/{mascara}", strict=True)
            elif re.match(caracteresUsadosNoIpv6, host): objetoComOsIps = ipaddress.IPv6Network(f"{host}/{mascara}", strict=True)
            
            listaDeIps = list()
            for ip in objetoComOsIps: listaDeIps.append(str(ip))

        else:
            if '-1' in host: host = host.replace('-1','')
            else: host = socket.gethostbyname(host)
            listaDeIps = [host]

        return listaDeIps
    
    def pacote_do_ping(ip):
        if platform.system() == 'Windows': opcao = '-n'
        elif platform.system() == 'Linux': opcao = '-c'

        try:
            resultados = subprocess.run(['ping', opcao, '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            if f'Resposta de {ip}' in resultados.stdout or f'64 bytes from {ip}' in resultados.stdout:
                print(f'{ip} --> ACESSÍVEL')
        except:
            pass


    def criando_pool_de_threads(listaDeIps):
        poolDeThreads = list()
        for ip in listaDeIps:
            thread = threading.Thread(target=pacote_do_ping, args=(ip,))
            poolDeThreads.append(thread)
        
        return poolDeThreads

    def executando_threads(poolDeThreads):
        maxThreads = 50
        threadsAtuais = []
        for thread in poolDeThreads:
            threadsAtuais.append(thread)
            thread.start()
            if len(threadsAtuais) >= maxThreads:
                for t in threadsAtuais:
                    t.join()
                threadsAtuais = []
    
        # Aguarda a conclusão de threads restantes
        for thread in threadsAtuais:
            thread.join()

    listaDeIps    = verificando_se_e_ip_ou_dominio(host, mascara)
    poolDeThreads = criando_pool_de_threads(listaDeIps)
    executando_threads(poolDeThreads)

# =============================================================================================================

host = input('\nIP ou nome: ')
mascara = input("Insira a máscara da rede (em formato CIDR, por exemplo, /24): ")
lista = ping(host, mascara)
