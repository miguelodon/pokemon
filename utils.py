import requests

# Diccionarios para traducciones
tipos_traducidos = {
    "fire": "fuego",
    "water": "agua",
    "grass": "planta",
    "electric": "eléctrico",
    "ice": "hielo",
    "fighting": "lucha",
    "poison": "veneno",
    "ground": "tierra",
    "flying": "volador",
    "psychic": "psíquico",
    "bug": "bicho",
    "rock": "roca",
    "ghost": "fantasma",
    "dragon": "dragón",
    "dark": "siniestro",
    "steel": "acero",
    "fairy": "hada"
}

habilidades_traducidas_dict = {
    "overgrow": "Espesura",
    "chlorophyll": "Clorofila",
    "blaze": "Fuego",
    "solar-power": "Poder Solar",
    "torrent": "Torrente",
    "rain-dish": "Clima Lluvioso",
    "shield-dust": "Polvo Escudo",
    "synchronize": "Sincronía",
    "intimidate": "Intimidación",
    "guts": "Agallas",
    "huge-power": "Gran Poder",
    "levitate": "Levitación",
    "static": "Estático",
    "flame-body": "Cuerpo Llama",
    "mold-breaker": "Rompe Moldes",
    "serene-grace": "Gracia Sutil",
    "speed-boost": "Aumento de Velocidad",
    "sturdy": "Firmeza",
    "wonder-guard": "Guardia Maravilla",
    "magic-guard": "Guardia Mágica",
    "adaptability": "Adaptabilidad",
    "drought": "Sequía",
    "drizzle": "Lluvia",
    "ice-body": "Cuerpo Helado",
    "poison-point": "Punto Tóxico",
    "fluffy": "Esponjoso",
    "prankster": "Bromista",
    "pickpocket": "Ladrón",
    "skill-link": "Conexión Hábil",
    "tinted-lens": "Lentes Ahumados",
    "clear-body": "Cuerpo Claro",
    "cloud-nine": "Nubes Nueve",
    "solid-rock": "Roca Sólida",
    "filter": "Filtro",
    "magic-bounce": "Rebote Mágico",
    "regenerator": "Regeneración",
    "trace": "Rastro",
    "analytical": "Analítico",
    "beast-boost": "Impulso Bestia",
    "battle-bond": "Vínculo de Batalla",
    "battery": "Batería",
    "big-pecks": "Plumas Grandes",
    "blunder-policy": "Política de Error",
    "cursed-body": "Cuerpo Maldito",
    "disguise": "Disfraz",
    "download": "Descarga",
    "draining-kiss": "Beso Drenante",
    "flame-boost": "Impulso Llama",
    "flower-gift": "Regalo Floral",
    "flower-veil": "Velo Floral",
    "forecast": "Pronóstico",
    "gale-wings": "Alas de Tormenta",
    "grassy-surge": "Oleada Herbácea",
    "heavy-metal": "Metal Pesado",
    "honey-gather": "Recolección de Miel",
    "illusion": "Ilusión",
    "imposter": "Impostor",
    "infiltrator": "Infiltrador",
    "inner-focus": "Enfoque Interno",
    "insomnia": "Insomnio",
    "keen-eye": "Ojo Agudo",
    "leaf-guard": "Guardia de Hojas",
    "light-metal": "Metal Ligero",
    "long-reach": "Alcance Largo",
    "mummy": "Momia",
    "multiscale": "Multiescala",
    "multitype": "Multitipo",
    "natural-cure": "Curación Natural",
    "no-guard": "Sin Guardias",
    "oblivious": "Despistado",
    "own-tempo": "Ritmo Propio",
    "pixilate": "Pixilado",
    "poison-touch": "Toque Tóxico",
    "power-construct": "Construcción de Poder",
    "power-of-alchemy": "Poder de Alquimia",
    "propeller-tail": "Cola Propulsora",
    "pure-power": "Poder Puro",
    "quick-feet": "Pies Rápidos",
    "rattled": "Asustado",
    "reckless": "Imprudente",
    "rivalry": "Rivalidad",
    "sand-rush": "Aceleración en Arena",
    "sand-stream": "Tormenta de Arena",
    "sap-sipper": "Succionador de Savia",
    "shadow-tag": "Etiqueta Sombra",
    "shed-skin": "Piel Desprendida",
    "simple": "Sencillo",
    "slow-start": "Inicio Lento",
    "sniper": "Francotirador",
    "snow-cloak": "Capa de Nieve",
    "snow-warning": "Advertencia de Nieve",
    "soul-heart": "Corazón del Alma",
    "suction-cups": "Ventosas",
    "swarm": "Enjambre",
    "sweet-veil": "Velo Dulce",
    "swift-swim": "Nado Rápido",
    "tangled-feet": "Pies Enredados",
    "technician": "Técnico",
    "telepathy": "Telepatía",
    "thick-fat": "Grasa Gruesa",
    "truant": "Holgazán",
    "turboblaze": "Llama Turbo",
    "unburden": "Desahogo",
    "unaware": "Ignorante",
    "vital-spirit": "Espíritu Vital",
    "water-absorb": "Absorción de Agua",
    "water-bubble": "Burbuja de Agua",
    "wonder-guard": "Guardia Maravilla",
    "zodiac": "Zodiaco",
    "damp": "Humedad",
    "air-lock": "Esclusa de aire",
    # Agrega más habilidades según sea necesario
}

# Diccionario de habilidades y sus inmunidades
habilidades_inmunidades = {
    "levitate": ["ground"],
    "immunity": ["poison"],
    "water-absorb": ["water"],
    "volt-absorb": ["electric"],
    "flash-fire": ["fire"],
    # Agrega más habilidades e inmunidades según sea necesario
}

def obtener_informacion_pokemon(nombre):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nombre.lower()}')
    
    if response.status_code == 200:
        pokemon = response.json()
        
        # Conversión de altura y peso
        pokemon['altura'] = pokemon['height'] / 10  # de decímetros a metros
        pokemon['peso'] = pokemon['weight'] / 10  # de hectogramos a kilogramos
        
        # Extraer tipos
        tipos = [tipo['type']['name'] for tipo in pokemon['types']]
        
        # Obtener debilidades, fortalezas e inmunidades para cada tipo
        debilidades, fortalezas, inmunidades = obtener_relaciones_tipo(tipos)

        # Extraer habilidades del Pokémon
        habilidades_en_ingles = [habilidad['ability']['name'] for habilidad in pokemon['abilities']]
        
        # Agregar inmunidades basadas en habilidades
        for habilidad in habilidades_en_ingles:
            if habilidad in habilidades_inmunidades:
                for inmunidad in habilidades_inmunidades[habilidad]:
                    inmunidades.add(inmunidad)

        # Traducir debilidades, fortalezas e inmunidades al español
        pokemon['debilidades'] = traducir_debilidades(debilidades)
        pokemon['fortalezas'] = traducir_fortalezas(fortalezas)
        pokemon['inmunidades'] = traducir_inmunidades(inmunidades)
        pokemon['habilidades'] = traducir_habilidades(habilidades_en_ingles)

        pokemon['tipos'] = [tipos_traducidos[tipo] for tipo in tipos if tipo in tipos_traducidos]
        
        return pokemon
    else:
        return None

def obtener_relaciones_tipo(tipos):
    debilidades = {}
    fortalezas = {}
    inmunidades = set()
    
    for tipo in tipos:
        tipo_response = requests.get(f'https://pokeapi.co/api/v2/type/{tipo}')
        if tipo_response.status_code == 200:
            tipo_data = tipo_response.json()
            
            # Agregar debilidades
            for debilidad in tipo_data['damage_relations']['double_damage_from']:
                tipo_debilidad = debilidad['name']
                debilidades[tipo_debilidad] = debilidades.get(tipo_debilidad, 0) + 1
            
           
            # Agregar fortalezas
            for fortaleza in tipo_data['damage_relations']['half_damage_from']:
                tipo_fortaleza = fortaleza['name']
                fortalezas[tipo_fortaleza] = fortalezas.get(tipo_fortaleza, 0) + 1
            
            # Agregar inmunidades
            for inmunidad in tipo_data['damage_relations']['no_damage_from']:
                inmunidades.add(inmunidad['name'])

    return debilidades, fortalezas, inmunidades

def traducir_debilidades(debilidades):
    debilidades_finales = []
    for tipo, count in debilidades.items():
        if count == 2:  # Debilidad x4
            debilidades_finales.append((tipo, 4))
        else:  # Debilidad x2
            debilidades_finales.append((tipo, 2))

    return [
        f"{tipos_traducidos[debilidad[0]]} (x{debilidad[1]})" 
        for debilidad in debilidades_finales if debilidad[0] in tipos_traducidos
    ]

def traducir_fortalezas(fortalezas):
    fortalezas_finales = []
    for tipo, count in fortalezas.items():
        if count == 2:  # Fortaleza x0.25
            fortalezas_finales.append((tipo, 0.25))
        else:  # Fortaleza x0.5
            fortalezas_finales.append((tipo, 0.5))

    return [
        f"{tipos_traducidos[fortaleza[0]]} (x{fortaleza[1]})" 
        for fortaleza in fortalezas_finales if fortaleza[0] in tipos_traducidos
    ]

def traducir_inmunidades(inmunidades):
    return [
        tipos_traducidos[inmunidad] 
        for inmunidad in inmunidades if inmunidad in tipos_traducidos
    ]

def traducir_habilidades(habilidades_en_ingles):
    return [
        habilidades_traducidas_dict.get(habilidad, habilidad.replace("-", " ")) for habilidad in habilidades_en_ingles
    ]

# Fin del archivo utils.py