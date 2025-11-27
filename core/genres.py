# core/genres.py

# Mapeia cada ASIN para seu gênero principal
ASIN_PARA_GENERO = {
    # 📚 Manhã: Ficção, Best-sellers, BookTok
    "8595081594": "manha",  # Colleen Hoover
    "6555302411": "manha",  # É Assim Que Acaba
    "8574029486": "manha",  # Matt Haig
    "8595081578": "manha",
    "8574029494": "manha",
    "8595081586": "manha",
    "8595081560": "manha",
    "8574029478": "manha",
    "8595081552": "manha",
    "8542369831": "manha",
    "8544128870": "manha",
    "8543000428": "manha",
    "655530239X": "manha",
    "8588685444": "manha",
    "8582852507": "manha",  # Novo Conceito
    "8582852515": "manha",
    "8582852523": "manha",
    "8576832269": "manha",  # HarperCollins econômico
    "8576832277": "manha",
    "8576832285": "manha",

    # 🚀 Tarde: Sci-Fi, Fantasia, Aventura
    "8543000436": "tarde",  # O Marciano
    "6555302403": "tarde",  # Hail Mary
    "8588685452": "tarde",  # Dark Matter
    "8588685460": "tarde",
    "8544128862": "tarde",
    "8555302373": "tarde",  # Intrínseca sci-fi
    "8555302381": "tarde",
    "855530239X": "tarde",
    "8544128870": "tarde",

    # 🕯️ Noite: Terror, Suspense, Thriller
    "8525018623": "noite",  # It
    "8580391021": "noite",  # O Iluminado
    "8544128889": "noite",  # Cthulhu
    "6555666550": "noite",  # A Cabana
    "8580391013": "noite",
    "8544128897": "noite",
    "8525018631": "noite",
    "8525018615": "noite",
    "8580391005": "noite",
    "8544128862": "noite",
    "8576832293": "noite",  # DarkSide
    "8576832307": "noite",
    "8576832315": "noite",
    "6555666569": "noite",  # Pipoca & Nanquim
    "6555666577": "noite",
}

# Lista de todos os ASINs a serem monitorados
ASINS_MONITORADOS = list(ASIN_PARA_GENERO.keys())