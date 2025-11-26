# keywords.py - Automobile and general conversation keywords

# General conversation keywords that should always be allowed
GENERAL_CONVERSATION_KEYWORDS = [
    # French greetings
    "bonjour", "salut", "coucou", "hello", "hi", "hey", "bonsoir", "bonne nuit",
    "yo", "wesh", "salam", "hey", "hola",
    
    # French politeness
    "merci", "remercie", "thanks", "thank you", "merci beaucoup", "merci bien",
    "s'il te plaît", "s'il vous plaît", "please", "stp", "svp", "de rien", "je t'en prie",
    
    # Farewells
    "au revoir", "bye", "adieu", "ciao", "à plus", "à bientôt", "salut", "goodbye",
    "see you", "à demain", "bonne journée", "bonne soirée",
    
    # Help requests
    "aide", "help", "assistance", "support", "aide-moi", "peux-tu m'aider", "j'ai besoin d'aide",
    "est-ce que tu peux m'aider", "je besoin d'assistance",
    
    # Repetition requests
    "répète", "repeat", "encore", "again", "peux-tu répéter", "tu peux répéter",
    "redire", "redis", "je n'ai pas compris", "pas compris", "incompris",
    "explique à nouveau", "reprends", "recommence",
    
    # Questions words
    "quoi", "comment", "pourquoi", "quand", "où", "qui", "quel", "quelle", "quels", "quelles",
    "combien", "lequel", "laquelle", "est-ce que", "qu'est-ce que", "que", "quelle est",
    
    # Explanations
    "explique", "définis", "define", "explain", "définition", "meaning", "signification",
    "que veut dire", "c'est quoi", "qu'est-ce que c'est",
    
    # Affirmations/Negations
    "oui", "non", "ok", "d'accord", "bien", "good", "yes", "no", "okay", "parfait",
    "exact", "correct", "faux", "wrong", "incorrect",
    
    # General conversation
    "ça va", "comment ça va", "vas bien", "tu vas bien", "comment tu vas", "how are you",
    "what's up", "quoi de neuf", "bien et toi", "très bien", "super", "génial", "cool",
    "parfait", "excellent", "formidable",
    
    # Understanding checks
    "compris", "understand", "entendu", "d'accord", "ok", "je vois", "je comprends",
    "pas de problème", "no problem", "bien reçu",
    
    # Time references
    "maintenant", "now", "aujourd'hui", "today", "demain", "tomorrow", "hier", "yesterday",
    "tout de suite", "immédiatement", "later", "plus tard",
    
    # Confirmation
    "vraiment", "really", "sérieusement", "seriously", "c'est vrai", "are you sure",
    "es-tu sûr", "tu es sûr", "certain", "certainement",
    
    # Appreciation
    "bravo", "félicitations", "congratulations", "good job", "bon travail", "well done",
    "super travail", "excellent travail",
    
    # Simple commands
    "stop", "arrête", "continue", "vas-y", "go ahead", "proceed", "next", "suivant",
    "précédent", "previous", "back", "retour"
]

# Comprehensive automobile keywords
AUTOMOBILE_KEYWORDS = [
    # Vehicle types
    "voiture", "automobile", "véhicule", "auto", "moto", "moton", "scooter", "camion",
    "utilitaire", "fourgon", "bus", "autobus", "autocar", "car", "poids lourd", 
    "semi-remorque", "remorque", "caravane", "camping-car", "van", "pick-up", "suv",
    "crossover", "berline", "break", "citadine", "sportive", "cabriolet", "coupé",
    "monospace", "limousine", "traction", "propulsion", "4x4", "quatre quatre",
    
    # Car brands (French and international)
    "renault", "peugeot", "citroën", "citroen", "ds", "bugatti", "alpine",
    "dacia", "seat", "skoda", "cupra",  # Added missing European brands
    "bmw", "mercedes", "mercedes-benz", "audi", "volkswagen", "vw", "opel",
    "ford", "fiat", "alfa romeo", "lancia", "ferrari", "lamborghini", "maserati",
    "porsche", "volvo", "saab", "tesla", "rivian", "lucid",
    "mini", "land rover", "jaguar", "aston martin", "bentley", "rolls royce", "mclaren",  # British brands
    "toyota", "honda", "nissan", "infiniti", "lexus", "mazda", "mitsubishi", "subaru",
    "suzuki", "daihatsu", "isuzu",
    "hyundai", "kia", "genesis", "ssangyong",
    "chevrolet", "cadillac", "buick", "gmc", "jeep", "dodge", "chrysler",
    "ram", "lincoln",
    "mg", "byd", "nio", "xpeng", "great wall", "haval", "chery", "geely",  # Chinese brands
    # Popular models (for better detection)
    "clio", "megane", "captur", "duster", "sandero", "logan",  # Renault/Dacia models
    "golf", "polo", "passat", "tiguan", "touareg",  # VW models
    "serie 3", "serie 5", "x3", "x5",  # BMW models
    "classe a", "classe c", "classe e", "gle", "glc",  # Mercedes models
    "308", "208", "3008", "5008", "2008",  # Peugeot models
    "c3", "c4", "c5", "berlingo",  # Citroen models
    "corolla", "yaris", "rav4", "camry",  # Toyota models
    
    # Engine and powertrain
    "moteur", "moteurs", "motorisation", "cylindre", "cylindrée", "soupape", "piston",
    "vilebrequin", "arbre à cames", "culasse", "bloc moteur", "turbo", "turbocompresseur",
    "compresseur", "suralimentation", "atmosphérique", "injection", "injecteur",
    "carburateur", "allumage", "bougie", "bougie préchauffage", "bobine", "distributeur",
    "courroie", "courroie distribution", "chaîne distribution", "embrayage", "volant moteur",
    "transmission", "boîte vitesse", "boite vitesse", "boîte manuelle", "boîte automatique",
    "cv", "chevaux", "puissance", "couple", "régime", "rpm", "accélération", "vitesse max",
    
    # Fuel and energy
    "carburant", "essence", "diesel", "gazole", "gpl", "gnv", "éthanol", "bioéthanol",
    "hybride", "hybride rechargeable", "électrique", "batterie", "pile combustible",
    "hydrogène", "charge", "chargeur", "borne", "recharge", "autonomie", "consommation",
    
    # Braking system
    "frein", "freins", "freinage", "disque", "disques", "plaquette", "plaquettes",
    "étrier", "étriers", "tambour", "maître cylindre", "servofrein", "frein main",
    "frein stationnement", "abs", "anti-blocage", "esp", "stabilité", "traction control",
    "aide freinage", "freinage urgence", "regenerative", "régénération",
    
    # Suspension and steering
    "suspension", "amortisseur", "ressort", "triangle", "rotule", "biellette",
    "barre stabilisatrice", "direction", "direction assistée", "crémaillère",
    "boîtier direction", "volant", "pneumatique", "pneus", "gomme", "pneu",
    "pression", "gonflage", "roue", "roues", "jante", "enjoliveur", "alliance",
    
    # Electrical system
    "batterie", "accumulateur", "alternateur", "démarreur", "allumage", "bougie",
    "bobine", "distributeur", "allumeur", "régulateur", "dynamo", "fusible",
    "relais", "câble", "câblage", "prise obd", "diagnostic", "calculateur",
    "ecu", "unitée contrôle", "capteur", "sonde", "actionneur",
    
    # Interior features
    "tableau bord", "tableau de bord", "compteur", "odomètre", "tachymètre",
    "compte-tours", "jauge", "voyant", "témoin", "indicateur", "volant", "leveur vitre",
    "rétroviseur", "miroir", "siège", "sièges", "appuie-tête", "accoudoir",
    "ceinture", "ceintures", "airbag", "coussin gonflable", "climatisation",
    "chauffage", "ventilation", "autoradio", "gps", "navigation", "bluetooth",
    "usb", "allume-cigare", "chargeur", "cigarette", "lecteur cd", "radio",
    
    # Exterior features
    "phare", "phares", "feu", "feux", "projecteur", "led", "xénon", "halogène",
    "feux croisement", "feux route", "feux antibrouillard", "feux stop",
    "feux position", "clignotant", "warning", "feux recul", "plaque", "immatriculation",
    "rétroviseur", "rétro", "essuie-glace", "lave-glace", "pare-brise", "vitre",
    "portière", "hayon", "coffre", "capot", "pare-chocs", "aileron", "spoiler",
    
    # Maintenance and repair
    "entretien", "maintenance", "révision", "vidange", "filtre", "filtre à huile",
    "filtre à air", "filtre à carburant", "filtre habitacle", "filtre pollen",
    "huile", "huile moteur", "lubrifiant", "graisse", "liquide", "liquide frein",
    "liquide refroidissement", "antigel", "liquide lave-glace", "liquide direction",
    "niveau", "contrôle", "vérification", "diagnostic", "panne", "dépannage",
    "réparation", "garage", "mécanicien", "atelier", "carrosserie", "peinture",
    
    # Warning lights and indicators
    "check engine", "voyant moteur", "température", "surchauffe", "pression huile",
    "niveau huile", "batterie", "charge", "frein", "frein main", "airbag", "srs",
    "ceinture", "abs", "esp", "traction", "stabilité", "direction", "pression pneus",
    "tpms", "entretien", "maintenance", "service", "filtre particules", "fap",
    "adblue", "scr", "échappement", "catalyseur", "pot catalytique",
    
    # Driving and safety
    "conduite", "conduire", "chauffeur", "conducteur", "permis", "permis conduire",
    "code route", "sécurité", "sécurité routière", "accident", "collision",
    "assurance", "assurance auto", "carte grise", "certificat immatriculation",
    "contrôle technique", "vignette", "crit'air", "pollution", "émission",
    
    # Car buying and selling
    "achat", "acheter", "vente", "vendre", "occasion", "neuf", "kilométrage", "km",
    "carrosserie", "équipement", "option", "accessoire", "promotion", "financement",
    "crédit", "leasing", "lld", "location", "reprise", "échange", "cote", "prix",
    
    # Technical terms
    "carrosserie", "châssis", "caisse", "train roulant", "transmission", "différentiel",
    "cardan", "pont", "suspension", "amortisseur", "frein", "embrayage", "boîte",
    "moteur", "refroidissement", "échappement", "allumage", "alimentation",
    "électricité", "électronique", "informatique", "connectivité", "adb", "canbus"
]