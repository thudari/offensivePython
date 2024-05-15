Desenvolvendo um Script de Monitoramento Persistente

O objetivo deste exercício é desenvolver um script em Python que simula o monitoramento de um usuário com capacidades de persistência aprimoradas. Este script irá incluir funcionalidades de captura de teclas pressionadas (keylogging), captura de telas (screenshots), monitoramento do sistema e verificação de diretórios. Além disso, o script irá criptografar todos os dados capturados antes de transmiti-los para um servidor, garantindo o armazenamento e análise segura dos dados. Este exercício é fundamental para entender como funcionam as ferramentas de monitoramento e espionagem digital e sua relevância no contexto de cibersegurança, especialmente para a detecção de ameaças e a prevenção de vazamentos de dados.

Parte 1: Captura Avançada e Monitoramento

Tarefa 1: Captura de Teclas e Screenshots

Implementar um Keylogger: Vamos desenvolver um keylogger baseado em Python para capturar todas as teclas pressionadas pelo usuário e salvar esses dados em um arquivo de log. Este keylogger funcionará de forma oculta em segundo plano e será inicializado automaticamente quando o sistema for iniciado. Este exercício ajudará a compreender como as ações do usuário podem ser monitoradas sem o seu conhecimento.

Capturar Screenshots: Configuraremos um mecanismo para capturar e salvar periodicamente screenshots da tela do usuário em um diretório especificado. Isso é útil para entender como informações visuais podem ser coletadas para análise ou evidência sem alertar o usuário.

Tarefa 2: Monitoramento da Atividade do Sistema

Coletar Informações do Sistema: Escreva uma função para coletar informações críticas do sistema, como uso de CPU, uso de memória e uma lista dos processos em execução atualmente. Isso simula a vigilância sobre o ambiente de computação do usuário, o que é vital para identificar comportamentos anômalos ou maliciosos.

Tarefa 3: Persistência do Script

Garantir a Continuidade do Script: Projetar o script para garantir que ele permaneça ativo e continue executando mesmo após o reinício do sistema. Isso demonstra como programas maliciosos podem se manter persistentes em um sistema infectado, uma técnica comum em malware e rootkits.

Tarefa 4: Verificação de Diretório e Criação de Arquivo ZIP

Verificação de Rotina: Implementar uma rotina que verifica diariamente o conteúdo do diretório TARGETDIR, comprime seu conteúdo em um arquivo ZIP e o prepara para transmissão ao servidor. Este passo é crucial para entender como dados podem ser periodicamente coletados e preparados para exfiltração.

Parte 2: Criptografia e Transmissão de Dados

Tarefa 5: Criptografia de Dados

Criptografar Dados Capturados: Garantir que todos os dados capturados, incluindo teclas pressionadas, screenshots e arquivos ZIP, sejam criptografados antes de serem enviados ao servidor. Isso ensina a importância da criptografia para a segurança de dados durante a transmissão, protegendo informações sensíveis contra interceptação.

Tarefa 6: Envio de Dados Criptografados

Configurar a Transmissão de Dados: Configurar o script para transmitir os dados criptografados de forma segura para um servidor. Aqui, você aprenderá como garantir que a transferência de dados entre o cliente e o servidor seja realizada de maneira segura, usando protocolos de comunicação seguros.

Parte 3: Decodificação e Servidor de Notificação

Tarefa 7: Servidor Python

Desenvolvimento do Servidor: Desenvolver um script do lado do servidor que recebe, descriptografa e processa os dados criptografados enviados pelo script de monitoramento. Isso permite entender o processo de recepção e análise de dados em um contexto de servidor, que é essencial para operações de cibersegurança e análise forense digital.

Tarefa 8: Integração com o Telegram

Notificações via Bot do Telegram: Criar um bot do Telegram para receber e exibir notificações e alertas do servidor sobre os dados capturados e outros eventos significativos. Isso mostra como sistemas de alerta e notificação podem ser integrados em operações de cibersegurança para proporcionar monitoramento e resposta em tempo real.

Este exercício não apenas fortalece a compreensão técnica sobre como ferramentas de monitoramento operam mas também contextualiza a importância dessas habilidades em proteger informações e detectar atividades maliciosas. É uma excelente oportunidade para aplicar conceitos de cibersegurança em um cenário prático e realista.

Disclaimer: Uso Educacional Apenas

Este material é fornecido exclusivamente para fins educacionais e de aprendizado. O objetivo é ensinar conceitos de cibersegurança, práticas de monitoramento e a importância da proteção de dados em um contexto controlado e ético.
