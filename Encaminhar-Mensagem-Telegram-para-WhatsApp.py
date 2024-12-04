from telethon.sync import TelegramClient, events
import pyperclip
import pyautogui
import time
import asyncio

# Substitua as informações abaixo com as suas credenciais do Telegram
api_id = '25011234'
api_hash = 'eb492c6043ad31d1234aab9123439e8d'
phone_number = '+5537912341234'

# Substitua "grupo_telegram_id" pelo ID do grupo do Telegram de onde você deseja obter mensagens
grupo_telegram_id = -45676578  # Substitua pelo ID do seu grupo

# Substitua "nome_grupo_whatsapp" pelo nome do grupo no WhatsApp
nome_grupo_whatsapp = "monitoramento"

async def main():
    # Inicializar o cliente Telegram
    client = TelegramClient('session_name', api_id, api_hash)

    # Conectar-se ao Telegram
    await client.connect()

    # Autenticar
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Digite o código de autenticação: '))

    @client.on(events.NewMessage(chats=grupo_telegram_id))
    async def handle_new_message(event):
        # Captura a mensagem recebida no grupo
        mensagem_telegram = event.message.text

        # Remove os caracteres de formatação de negrito
        mensagem_telegram = mensagem_telegram.replace('*', '')

        # Copia a mensagem para a área de transferência
        pyperclip.copy(mensagem_telegram)

        # Abre o navegador e entra no WhatsApp Web
       # pyautogui.hotkey('ctrl', 't')
        #time.sleep(1)
        #pyautogui.write('https://web.whatsapp.com/')
        #pyautogui.press('enter')
        #time.sleep(15)  # Aguarde tempo suficiente para fazer o login manualmente

        # Procura o grupo no WhatsApp Web
        pyautogui.click(x=230, y=160)  # Coordenação para clicar na barra de pesquisa
        pyautogui.write(nome_grupo_whatsapp)
        time.sleep(2)
        pyautogui.press('enter')

        # Aguarda 5 segundos para garantir que a conversa seja carregada
        time.sleep(2)

        # Cola a mensagem da área de transferência e envia
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

    # Inicia o loop de eventos
    await client.run_until_disconnected()

# Inicia o loop de eventos assíncrono
asyncio.run(main())
