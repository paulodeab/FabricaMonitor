import socket
import nmap
import json

#API da NSE - https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=?

class ScanNetwork:

    def __init__(self):
        self._ip = None  # Armazena o IP local
        self.network_prefix = None  # Prefixo da rede
        self.devices = []  # Armazena dispositivos encontrados

    def set_ip(self):
        """Define o IP local automaticamente."""
        hostname = socket.gethostname()
        self._ip = socket.gethostbyname(hostname)
        print(f"IP Local: {self._ip}")

        # Define o prefixo da rede
        self.network_prefix = self.get_network_prefix()

    def get_ip(self):
        """Retorna o IP local."""
        return self._ip

    def get_network_prefix(self):
        """Calcula o prefixo da rede com base no IP local."""
        if not self._ip:
            raise ValueError("IP não definido. Use set_ip para definir o IP.")

        ip_parts = self._ip.split('.')
        network_prefix = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}"
        print(f"Prefixo da Rede: {network_prefix}.0/30")
        return network_prefix

    def scan_ip(self, ip: str):
        """Escaneia um IP específico usando Nmap."""
        try:
            # Instância do PortScanner
            scanner = nmap.PortScanner()
            scanner.scan(hosts=ip, arguments="-sS -sV -O -A -T4 --version-all --system-dns")
          
            if scanner[ip].state() == "up":
                mac = scanner[ip]['addresses'].get('mac', 'MAC desconhecido')
                os = scanner[ip].get('osmatch', [{'name': 'SO desconhecido'}])[0]['name']

                # Obtém o nome do host (DNS reverso)
                hostname = scanner[ip].hostname() or "Host desconhecido"

                # Coleta informações das portas abertas com serviço e versão
                open_ports = []
                if 'tcp' in scanner[ip]:
                    for port, port_data in scanner[ip]['tcp'].items():
                        service = port_data.get('name', 'Serviço desconhecido')
                        version = port_data.get('version', 'Versão desconhecida')
                        open_ports.append((port, service, version))

                # Adiciona o dispositivo encontrado à lista
                self.devices.append({
                    "ip": ip,
                    "hostname": hostname,
                    "mac": mac,
                    "os": os,
                    "open_ports": open_ports
                })
        except Exception as e:
            pass

    def scan_network(self):
        """Escaneia a rede de forma sequencial, sem usar threads."""
        if not self.network_prefix:
            raise ValueError("Prefixo da rede não definido. Use set_ip para definir o IP.")

        # Escaneia IPs de 1 a 254 de forma sequencial
        for i in range(1, 3):
            ip = f"{self.network_prefix}.{i}"
            self.scan_ip(ip)



    def generate_json(self) -> str:
        """Gera um JSON com os resultados do escaneamento."""
        return self.devices





















