# test_env.py
from dotenv import load_dotenv
import os

# Força recarregar variáveis
load_dotenv()

token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

print("TELEGRAM_BOT_TOKEN presente?", token is not None)
print("TELEGRAM_CHAT_ID presente?", chat_id is not None)

if token and chat_id:
    print("✅ Ambas as variáveis estão configuradas!")
else:
    print("❌ Uma ou ambas as variáveis estão faltando.")