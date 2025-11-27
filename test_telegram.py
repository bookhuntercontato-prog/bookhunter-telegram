# test_telegram.py
import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

def send_test_message():
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    if not bot_token or not chat_id:
        print("❌ Erro: TELEGRAM_BOT_TOKEN ou TELEGRAM_CHAT_ID não configurado no .env")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": "✅ Teste do VS Code! O BookHunter está online! 🚀",
        "parse_mode": "HTML"
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print("✅ Mensagem enviada com sucesso!")
    else:
        print(f"❌ Erro: {response.status_code} - {response.text}")

if __name__ == "__main__":
    send_test_message()