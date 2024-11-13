Sistema de monitoramento de dispositivos conectados a rede da fábrica.
Objetivo Monitoramento, verificar dispositivos ligados e desligados.
Identificar dispositivos ligados a rede dados de cada dispositivo(ID, MAC, NOME, SO).
Scan de vulnerabilidades dos dispositivos. Em especial os IIoT


1. Arquitetura do Sistema
Módulos principais:
Módulo de Descoberta de Dispositivos:

Escaneia a rede e identifica dispositivos conectados.
Coleta dados: IP, MAC, nome do dispositivo, sistema operacional.
Módulo de Monitoramento Contínuo:

Acompanha o status (ligado/desligado) de cada dispositivo em tempo real.
Módulo de Análise de Vulnerabilidades:

Executa varreduras periódicas e verifica vulnerabilidades.
Dashboard e Relatórios:

Interface web para visualização e relatórios do status e segurança da rede.
Alertas e Notificações:

Envia notificações por e-mail ou outros canais em caso de problemas críticos.