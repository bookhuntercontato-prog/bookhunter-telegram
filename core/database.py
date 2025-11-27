# core/database.py
import os
from supabase import create_client, Client
from datetime import datetime

# Lê as variáveis do ambiente (vem do arquivo .env)
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

# Cria o cliente do Supabase
supabase: Client = create_client(url, key)

def asin_ja_enviado_hoje(asin: str) -> bool:
    """Verifica se um ASIN já foi enviado HOJE (em UTC)"""
    hoje = datetime.utcnow().date().isoformat()
    response = supabase.table("sent_books").select("*").eq("asin", asin).eq("date", hoje).execute()
    return len(response.data) > 0

def salvar_asin_enviado(asin: str):
    """Salva o ASIN na tabela sent_books com a data de hoje (UTC)"""
    hoje = datetime.utcnow().date().isoformat()
    supabase.table("sent_books").insert({"asin": asin, "date": hoje}).execute()

    # core/database.py (adicione no final)

def salvar_promocoes_do_dia(promocoes: list):
    """Salva todas as promoções encontradas HOJE no Supabase."""
    hoje = datetime.utcnow().date().isoformat()
    
    # Primeiro, limpa promoções do dia anterior
    supabase.table("sent_books").delete().eq("date", hoje).execute()
    
    # Depois, insere as novas
    for p in promocoes:
        supabase.table("sent_books").insert({
            "asin": p["asin"],
            "date": hoje,
            "title": p["title"],
            "price": p["price"],
            "discount_percent": p["discount_percent"],
            "link": p["link"],
            "genero": p["genero"]  # novo campo!
        }).execute()

def obter_promocoes_por_genero(genero: str):
    """Obtém promoções do dia por gênero."""
    hoje = datetime.utcnow().date().isoformat()
    response = supabase.table("sent_books").select("*").eq("date", hoje).eq("genero", genero).execute()
    return response.data