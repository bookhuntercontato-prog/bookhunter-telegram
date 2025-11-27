# core/utils.py
from typing import Union

# Código de afiliado (mantido exatamente como no seu projeto)
AFILIADO = "bookhunter06b-20"

# Palavras que indicam que NÃO é livro físico
NAO_LIVRO = {
    "boneco", "funko", "filme", "video", "série", "camiseta", "jogo", "download",
    "prime video", "bluray", "dvd", "adorno", "figura", "colecionável", "assista"
}

def eh_livro(titulo: str) -> bool:
    """Verifica se o título parece ser de um livro físico (não vídeo, boneco, etc.)"""
    if not titulo:
        return False
    t = titulo.lower()
    return not any(p in t for p in NAO_LIVRO)

def formatar_real(valor: Union[int, float, None]) -> str:
    """
    Converte valor para formato monetário brasileiro: R$ XX,XX
    Lida com valores em centavos (ex: 2590 → R$ 25,90) ou reais (ex: 25.9 → R$ 25,90)
    """
    if valor is None:
        return "0,00"
    try:
        # Se for inteiro grande ou float > 1000, provavelmente está em centavos
        if isinstance(valor, int) and valor > 500:
            valor = valor / 100.0
        elif isinstance(valor, float) and valor > 1000:
            valor = valor / 100.0
        
        return f"{valor:.2f}".replace('.', ',')
    except (TypeError, ValueError):
        return "0,00"