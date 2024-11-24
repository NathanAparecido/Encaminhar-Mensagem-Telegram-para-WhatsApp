# Encaminhar Mensagem grupo Telegram para grupo WhatsApp

Este repositório contém um script em Python para capturar mensagens de um grupo no Telegram e enviá-las automaticamente para um grupo específico no WhatsApp utilizando automação com `Telethon` e `PyAutoGUI`.

## Funcionalidades

- Captura mensagens em tempo real de um grupo específico no Telegram.
- Remove caracteres de formatação (por exemplo, asteriscos de negrito).
- Envia as mensagens para um grupo específico no WhatsApp via WhatsApp Web.

## Requisitos

- Python 3.7 ou superior.
- Conta no Telegram e suas credenciais de API (`api_id` e `api_hash`).
- WhatsApp Web configurado no navegador.
- Pacotes Python:
  - `telethon`
  - `pyperclip`
  - `pyautogui`
  - `asyncio`

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/telegram-to-whatsapp.git
   cd telegram-to-whatsapp
   ```
2. Instale as dependências:
  ```bash
  pip install telethon pyperclip pyautogui
  ```
3. Configuere o script:
- Substitua as variáveis no código com suas credenciais e configurações:
  - `api_id` e `api_hash` com suas credenciais da API do Telegram.
  - `phone_number` com o número do telefone associado à sua conta do Telegram.
  - `grupo_telegram_id` com o ID do grupo do Telegram.
  - `nome_grupo_whatsapp` com o nome do grupo do WhatsApp.

## Como Usar

1. Obtenha suas credenciais do Telegram:
   
  - Acesse o site oficial do Telegram API para criar um novo aplicativo e obter o `api_id` e o `api_hash`.

2. Obtenha o ID do grupo do Telegram:
  - Use uma ferramenta como Telethon ou loga no web.telegram.org e quando entrar no grupo na url informa ID do grupo.

3.  Execute o script:
   ```bash
   python telegram_to_whatsapp.py
   ```
  Durante a primeira execução, você será solicitado a autenticar sua conta do Telegram inserindo o código enviado para  seu telefone.

4. Certifique-se de que o WhatsApp Web está ativo no navegador e que o nome do grupo no WhatsApp corresponde exatamente ao especificado no script.

## Notas Importantes
  - Automação do WhatsApp Web: O script utiliza o `PyAutoGUI` para automação da interface do WhatsApp Web. Certifique-se de que a resolução e a interface do navegador estão configuradas de forma consistente.
  - Segurança: Não compartilhe suas credenciais do Telegram ou do WhatsApp em repositórios públicos. Oculte-as utilizando variáveis de ambiente ou arquivos de configuração.

## Limitações
  - A automação com `PyAutoGUI` depende da resolução e layout do WhatsApp Web. Ajuste as coordenadas no script conforme necessário.
  - Este script não funciona com mensagens de mídia (apenas texto).
  - Certifique-se de respeitar as políticas de uso tanto do Telegram quanto do WhatsApp.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar PRs com melhorias.

##3Licença

Este projeto é licenciado sob a MIT License.
