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
