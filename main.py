# main.py
import os
import sys
from dotenv import load_dotenv
load_dotenv()

from core.telegram import send_telegram_message
from core.database import obter_promocoes_por_genero
from core.utils import formatar_real

def main(slot: str):
    if slot not in ["manha", "tarde", "noite"]:
        print("❌ Slot inválido. Use 'manha', 'tarde' ou 'noite'.")
        sys.exit(1)
    
    print(f"📤 Enviando promoções do slot: {slot}...")
    promocoes = obter_promocoes_por_genero(slot)
    
    if not promocoes:
        msg = "📚 <b>Nenhuma promoção encontrada agora.</b>\n\n"
        msg += "🔍 Monitoramos diariamente centenas de livros.\n"
        msg += "⏰ Próxima atualização: "
        if slot == "manha": msg += "<b>14h</b> (Ficção Científica, Fantasia)."
        elif slot == "tarde": msg += "<b>20h</b> (Terror, Suspense)."
        else: msg += "<b>9h</b> (Ficção, Best-sellers)."
        msg += "\n💬 Siga para não perder as ofertas reais!\n#bookhunter #livros"
        send_telegram_message(msg)
        return
    
    # Mensagens por horário
    titulos = {
        "manha": "📚 <b>🔥 Promoções da Manhã!</b>\n\n",
        "tarde": "🚀 <b>🔥 Promoções da Tarde!</b>\n\n",
        "noite": "🕯️ <b>🔥 Promoções da Noite!</b>\n\n"
    }
    
    rodapes = {
        "manha": "\n✅ Clique e veja a edição com desconto na página!\n#ficção #bestseller",
        "tarde": "\n🌌 Perfeito para uma pausa épica!\n#scifi #fantasia #aventura",
        "noite": "\n☠️ Não leia antes de dormir... ou leia!\n#terror #suspense #thriller"
    }
    
    msg = titulos[slot]
    for p in promocoes[:5]:
        titulo = p["title"][:60] + ("..." if len(p["title"]) > 60 else "")
        preco_fmt = formatar_real(p["price"])
        msg += f"📘 <b>{titulo}</b>\n"
        msg += f"💰 R$ {preco_fmt} | 📉 {p['discount_percent']}% OFF\n"
        msg += f"🔗 {p['link']}\n\n"
    
    msg += rodapes[slot]
    send_telegram_message(msg)
    print(f"✅ Mensagem enviada com {len(promocoes)} ofertas!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <slot>")
        sys.exit(1)
    main(sys.argv[1])