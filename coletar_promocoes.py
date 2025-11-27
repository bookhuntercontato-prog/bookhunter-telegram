# coletar_promocoes.py
import os
import sys
from dotenv import load_dotenv
load_dotenv()

from core.scraper import buscar_livros_completos  # nova função
from core.database import salvar_promocoes_do_dia
from core.genres import ASIN_PARA_GENERO

def main():
    print("🔍 Coletando promoções do dia...")
    livros = buscar_livros_completos()
    
    # Adiciona gênero a cada livro
    livros_com_genero = []
    for livro in livros:
        genero = ASIN_PARA_GENERO.get(livro["asin"], "manha")  # padrão: manha
        livro["genero"] = genero
        livros_com_genero.append(livro)
    
    salvar_promocoes_do_dia(livros_com_genero)
    print(f"✅ {len(livros_com_genero)} promoções salvas para hoje.")

if __name__ == "__main__":
    main()