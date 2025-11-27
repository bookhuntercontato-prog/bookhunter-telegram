# test_supabase.py
import os
from dotenv import load_dotenv

# Carrega o .env
load_dotenv()

# Diagnóstico: imprime os valores (substitui parte da chave por *** por segurança)
print("🔍 Diagnóstico de variáveis de ambiente:")
print("SUPABASE_URL =", os.getenv("SUPABASE_URL"))
print("SUPABASE_KEY =", os.getenv("SUPABASE_KEY")[:10] + "..." if os.getenv("SUPABASE_KEY") else None)

# Agora importa o módulo (só depois de carregar o .env)
from core.database import asin_ja_enviado_hoje, salvar_asin_enviado

# Teste com ASIN fictício
asin_teste = "1234567890"

if asin_ja_enviado_hoje(asin_teste):
    print("❌ ASIN já foi enviado hoje")
else:
    salvar_asin_enviado(asin_teste)
    print("✅ ASIN salvo como enviado!")