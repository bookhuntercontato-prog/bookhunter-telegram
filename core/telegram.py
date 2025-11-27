# core/telegram.py
import os
import requests

def send_telegram_message(message: str):
    """Envia uma mensagem formatada para o canal do Telegram usando HTML."""
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    if not bot_token or not chat_id:
        raise ValueError("❌ TELEGRAM_BOT_TOKEN ou TELEGRAM_CHAT_ID não configurado no .env")
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }
    
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(f"❌ Erro no Telegram: {response.status_code} - {response.text}")
        return False
    return True