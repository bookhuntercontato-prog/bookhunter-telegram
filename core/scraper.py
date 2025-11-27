# core/scraper.py
import os
import requests
from core.utils import eh_livro, AFILIADO
from core.genres import ASINS_MONITORADOS

def buscar_livros_completos() -> list:
    """Verifica todos os ASINs monitorados e retorna os com desconto."""
    api_key = os.getenv("AXESSO_API_KEY")
    if not api_key:
        raise ValueError("❌ AXESSO_API_KEY não configurada no .env")

    headers = {"x-api-key": api_key}
    promocoes = []
    
    print(f"  Verificando {len(ASINS_MONITORADOS)} livros na Axesso...")
    
    for asin in ASINS_MONITORADOS:
        try:
            response = requests.get(
                "https://api.axesso.de/amazon-data-service/product-details",
                headers=headers,
                params={"domainCode": "amazon.com.br", "asin": asin},
                timeout=10
            )
            
            if response.status_code != 200:
                continue
            
            data = response.json()
            title = data.get("title", "")
            if not eh_livro(title):
                continue
            
            price_data = data.get("price", {})
            price = price_data.get("value")
            if price is None or price <= 0:
                continue
            
            is_on_sale = price_data.get("isOnSale", False)
            list_price = data.get("listPrice", {}).get("value")
            if not is_on_sale or list_price is None or list_price <= price:
                continue
            
            discount_percent = int(100 - (price / list_price * 100))
            if discount_percent < 5:
                continue
            
            link = f"https://www.amazon.com.br/dp/{asin}?tag={AFILIADO}"
            
            promocoes.append({
                'asin': asin,
                'title': title,
                'price': price,
                'discount_percent': discount_percent,
                'link': link
            })
            
        except Exception:
            continue
    
    print(f"✅ Encontrados {len(promocoes)} livros com desconto.")
    return promocoes