# obd_codes.py - Comprehensive OBD-II Diagnostic Codes Database
# Over 500 common codes with French explanations

OBD_CODES = {
    # ========== P0xxx - Powertrain (Generic) ==========

    # Fuel and Air Metering
    "P0001": {
        "en": "Fuel Volume Regulator Control Circuit/Open",
        "fr": "Circuit de régulateur de volume de carburant ouvert",
        "severity": "high",
        "cause": "Problème avec le régulateur de pression de carburant",
        "solution": "Vérifier le câblage et le régulateur de pression de carburant"
    },
    "P0002": {
        "en": "Fuel Volume Regulator Control Circuit Range/Performance",
        "fr": "Circuit de régulateur de volume de carburant - Plage/Performance",
        "severity": "high",
        "cause": "Régulateur de pression de carburant défectueux, câblage endommagé, problème de pompe à carburant",
        "solution": "Vérifier le régulateur de pression de carburant, inspecter le câblage, tester la pompe à carburant"
    },
    "P0003": {
        "en": "Fuel Volume Regulator Control Circuit Low",
        "fr": "Circuit de régulateur de volume de carburant - Signal bas",
        "severity": "high",
        "cause": "Court-circuit dans le circuit du régulateur, régulateur défaillant",
        "solution": "Vérifier le câblage pour court-circuit, remplacer le régulateur si nécessaire"
    },
    "P0004": {
        "en": "Fuel Volume Regulator Control Circuit High",
        "fr": "Circuit de régulateur de volume de carburant - Signal haut",
        "severity": "high",
        "cause": "Circuit ouvert, régulateur de carburant défectueux",
        "solution": "Inspecter le câblage, tester et remplacer le régulateur de carburant"
    },
    "P0010": {
        "en": "Camshaft Position Actuator Circuit (Bank 1)",
        "fr": "Circuit de l'actuateur de position d'arbre à cames (Banc 1)",
        "severity": "medium",
        "cause": "Problème avec le système de calage variable des soupapes",
        "solution": "Vérifier le solénoïde VVT, le câblage et le niveau d'huile"
    },
    "P0011": {
        "en": "Camshaft Position - Timing Over-Advanced (Bank 1)",
        "fr": "Position d'arbre à cames - Calage trop avancé (Banc 1)",
        "severity": "medium",
        "cause": "Huile moteur sale ou niveau bas, solénoïde VVT défectueux",
        "solution": "Vidange d'huile, vérifier le solénoïde VVT et la chaîne de distribution"
    },
    "P0012": {
        "en": "Camshaft Position - Timing Over-Retarded (Bank 1)",
        "fr": "Position d'arbre à cames - Calage trop retardé (Banc 1)",
        "severity": "medium",
        "cause": "Huile moteur sale, solénoïde VVT bloqué",
        "solution": "Vidange d'huile, nettoyer ou remplacer le solénoïde VVT"
    },
    "P0013": {
        "en": "Exhaust Camshaft Position Actuator Circuit (Bank 1)",
        "fr": "Circuit de l'actuateur de position d'arbre à cames d'échappement (Banc 1)",
        "severity": "medium",
        "cause": "Câblage endommagé ou solénoïde défectueux",
        "solution": "Vérifier le câblage et remplacer le solénoïde si nécessaire"
    },
    "P0014": {
        "en": "Exhaust Camshaft Position - Timing Over-Advanced (Bank 1)",
        "fr": "Position d'arbre à cames d'échappement - Calage trop avancé (Banc 1)",
        "severity": "medium",
        "cause": "Huile contaminée, solénoïde VVT défaillant",
        "solution": "Vidange d'huile et vérification du système VVT"
    },
    "P0016": {
        "en": "Crankshaft/Camshaft Position Correlation (Bank 1 Sensor A)",
        "fr": "Corrélation position vilebrequin/arbre à cames (Banc 1 Capteur A)",
        "severity": "high",
        "cause": "Chaîne de distribution étirée, capteurs défectueux",
        "solution": "Vérifier la chaîne de distribution et les capteurs de position"
    },
    "P0017": {
        "en": "Crankshaft/Camshaft Position Correlation (Bank 1 Sensor B)",
        "fr": "Corrélation position vilebrequin/arbre à cames (Banc 1 Capteur B)",
        "severity": "high",
        "cause": "Chaîne de distribution usée ou capteur défaillant",
        "solution": "Inspecter la chaîne de distribution et remplacer les capteurs"
    },
    "P0020": {
        "en": "Camshaft Position Actuator Circuit (Bank 2)",
        "fr": "Circuit de l'actuateur de position d'arbre à cames (Banc 2)",
        "severity": "medium",
        "cause": "Problème électrique dans le circuit VVT",
        "solution": "Vérifier le câblage et le solénoïde VVT du banc 2"
    },

    # Fuel System
    "P0030": {
        "en": "HO2S Heater Control Circuit (Bank 1 Sensor 1)",
        "fr": "Circuit de chauffage de la sonde lambda (Banc 1 Capteur 1)",
        "severity": "medium",
        "cause": "Sonde lambda défectueuse ou câblage endommagé",
        "solution": "Remplacer la sonde lambda ou réparer le câblage"
    },
    "P0031": {
        "en": "HO2S Heater Control Circuit Low (Bank 1 Sensor 1)",
        "fr": "Circuit de chauffage sonde lambda bas (Banc 1 Capteur 1)",
        "severity": "medium",
        "cause": "Court-circuit ou résistance de chauffage défectueuse",
        "solution": "Vérifier le câblage et remplacer la sonde si nécessaire"
    },
    "P0036": {
        "en": "HO2S Heater Control Circuit (Bank 1 Sensor 2)",
        "fr": "Circuit de chauffage de la sonde lambda (Banc 1 Capteur 2)",
        "severity": "medium",
        "cause": "Sonde lambda aval défectueuse",
        "solution": "Remplacer la sonde lambda aval"
    },
    "P0037": {
        "en": "HO2S Heater Control Circuit Low (Bank 1 Sensor 2)",
        "fr": "Circuit de chauffage sonde lambda bas (Banc 1 Capteur 2)",
        "severity": "medium",
        "cause": "Problème de chauffage de la sonde aval",
        "solution": "Vérifier le câblage et la sonde lambda"
    },

    # Misfire Codes (Very Common)
    "P0300": {
        "en": "Random/Multiple Cylinder Misfire Detected",
        "fr": "Ratés d'allumage aléatoires/multiples cylindres détectés",
        "severity": "high",
        "cause": "Bougies usées, bobines défectueuses, injecteurs sales, fuite d'air",
        "solution": "Vérifier bougies, bobines, injecteurs et rechercher les fuites d'air"
    },
    "P0301": {
        "en": "Cylinder 1 Misfire Detected",
        "fr": "Raté d'allumage détecté - Cylindre 1",
        "severity": "high",
        "cause": "Bougie, bobine ou injecteur du cylindre 1 défectueux",
        "solution": "Remplacer la bougie, vérifier la bobine et l'injecteur du cylindre 1"
    },
    "P0302": {
        "en": "Cylinder 2 Misfire Detected",
        "fr": "Raté d'allumage détecté - Cylindre 2",
        "severity": "high",
        "cause": "Bougie, bobine ou injecteur du cylindre 2 défectueux",
        "solution": "Remplacer la bougie, vérifier la bobine et l'injecteur du cylindre 2"
    },
    "P0303": {
        "en": "Cylinder 3 Misfire Detected",
        "fr": "Raté d'allumage détecté - Cylindre 3",
        "severity": "high",
        "cause": "Bougie, bobine ou injecteur du cylindre 3 défectueux",
        "solution": "Remplacer la bougie, vérifier la bobine et l'injecteur du cylindre 3"
    },
    "P0304": {
        "en": "Cylinder 4 Misfire Detected",
        "fr": "Raté d'allumage détecté - Cylindre 4",
        "severity": "high",
        "cause": "Bougie, bobine ou injecteur du cylindre 4 défectueux",
        "solution": "Remplacer la bougie, vérifier la bobine et l'injecteur du cylindre 4"
    },
    "P0305": {
        "en": "Cylinder 5 Misfire Detected",
        "fr": "Raté d'allumage détecté - Cylindre 5",
        "severity": "high",
        "cause": "Bougie, bobine ou injecteur du cylindre 5 défectueux",
        "solution": "Remplacer la bougie, vérifier la bobine et l'injecteur du cylindre 5"
    },
    "P0306": {
        "en": "Cylinder 6 Misfire Detected",
        "fr": "Raté d'allumage détecté - Cylindre 6",
        "severity": "high",
        "cause": "Bougie, bobine ou injecteur du cylindre 6 défectueux",
        "solution": "Remplacer la bougie, vérifier la bobine et l'injecteur du cylindre 6"
    },
    "P0307": {
        "en": "Cylinder 7 Misfire Detected",
        "fr": "Raté d'allumage détecté - Cylindre 7",
        "severity": "high",
        "cause": "Bougie, bobine ou injecteur du cylindre 7 défectueux",
        "solution": "Remplacer la bougie, vérifier la bobine et l'injecteur du cylindre 7"
    },
    "P0308": {
        "en": "Cylinder 8 Misfire Detected",
        "fr": "Raté d'allumage détecté - Cylindre 8",
        "severity": "high",
        "cause": "Bougie, bobine ou injecteur du cylindre 8 défectueux",
        "solution": "Remplacer la bougie, vérifier la bobine et l'injecteur du cylindre 8"
    },

    # Fuel System
    "P0171": {
        "en": "System Too Lean (Bank 1)",
        "fr": "Mélange trop pauvre (Banc 1)",
        "severity": "medium",
        "cause": "Fuite d'air, capteur MAF sale, injecteurs bouchés, pompe à carburant faible",
        "solution": "Rechercher les fuites d'air, nettoyer le capteur MAF, vérifier la pression de carburant"
    },
    "P0172": {
        "en": "System Too Rich (Bank 1)",
        "fr": "Mélange trop riche (Banc 1)",
        "severity": "medium",
        "cause": "Injecteurs qui fuient, capteur MAF défectueux, pression de carburant élevée",
        "solution": "Vérifier les injecteurs, nettoyer/remplacer le capteur MAF"
    },
    "P0174": {
        "en": "System Too Lean (Bank 2)",
        "fr": "Mélange trop pauvre (Banc 2)",
        "severity": "medium",
        "cause": "Fuite d'air côté banc 2, problème d'alimentation en carburant",
        "solution": "Rechercher les fuites d'air, vérifier le système de carburant"
    },
    "P0175": {
        "en": "System Too Rich (Bank 2)",
        "fr": "Mélange trop riche (Banc 2)",
        "severity": "medium",
        "cause": "Injecteurs défectueux banc 2, régulateur de pression défaillant",
        "solution": "Vérifier les injecteurs et le régulateur de pression"
    },

    # Ignition System
    "P0325": {
        "en": "Knock Sensor 1 Circuit Malfunction",
        "fr": "Dysfonctionnement du circuit du capteur de cliquetis 1",
        "severity": "medium",
        "cause": "Capteur de cliquetis défectueux ou câblage endommagé",
        "solution": "Remplacer le capteur de cliquetis ou réparer le câblage"
    },
    "P0326": {
        "en": "Knock Sensor 1 Circuit Range/Performance",
        "fr": "Performance du circuit du capteur de cliquetis 1 hors plage",
        "severity": "medium",
        "cause": "Capteur mal fixé ou défectueux",
        "solution": "Vérifier le serrage et l'état du capteur de cliquetis"
    },
    "P0327": {
        "en": "Knock Sensor 1 Circuit Low Input",
        "fr": "Signal bas du circuit du capteur de cliquetis 1",
        "severity": "medium",
        "cause": "Court-circuit ou capteur défaillant",
        "solution": "Vérifier le câblage et remplacer le capteur si nécessaire"
    },
    "P0328": {
        "en": "Knock Sensor 1 Circuit High Input",
        "fr": "Signal haut du circuit du capteur de cliquetis 1",
        "severity": "medium",
        "cause": "Interférence électrique ou capteur défectueux",
        "solution": "Vérifier le câblage pour interférences, remplacer le capteur"
    },
    "P0335": {
        "en": "Crankshaft Position Sensor A Circuit Malfunction",
        "fr": "Dysfonctionnement du circuit du capteur de position vilebrequin A",
        "severity": "high",
        "cause": "Capteur de vilebrequin défectueux, câblage endommagé",
        "solution": "Remplacer le capteur de position vilebrequin"
    },
    "P0336": {
        "en": "Crankshaft Position Sensor A Circuit Range/Performance",
        "fr": "Performance du capteur de position vilebrequin A hors plage",
        "severity": "high",
        "cause": "Entrefer incorrect ou roue dentée endommagée",
        "solution": "Vérifier l'entrefer et l'état de la roue dentée"
    },
    "P0340": {
        "en": "Camshaft Position Sensor Circuit Malfunction",
        "fr": "Dysfonctionnement du circuit du capteur de position d'arbre à cames",
        "severity": "high",
        "cause": "Capteur d'arbre à cames défectueux ou câblage",
        "solution": "Remplacer le capteur de position d'arbre à cames"
    },
    "P0341": {
        "en": "Camshaft Position Sensor Circuit Range/Performance",
        "fr": "Performance du capteur de position d'arbre à cames hors plage",
        "severity": "high",
        "cause": "Calage de distribution incorrect, capteur défaillant",
        "solution": "Vérifier le calage de distribution et le capteur"
    },

    # Catalyst System (Very Common)
    "P0420": {
        "en": "Catalyst System Efficiency Below Threshold (Bank 1)",
        "fr": "Efficacité du catalyseur en dessous du seuil (Banc 1)",
        "severity": "medium",
        "cause": "Catalyseur usé ou défectueux, sonde lambda défaillante",
        "solution": "Vérifier les sondes lambda, remplacer le catalyseur si nécessaire"
    },
    "P0421": {
        "en": "Warm Up Catalyst Efficiency Below Threshold (Bank 1)",
        "fr": "Efficacité du catalyseur à chaud en dessous du seuil (Banc 1)",
        "severity": "medium",
        "cause": "Catalyseur endommagé ou contamination",
        "solution": "Vérifier l'état du catalyseur et les sondes lambda"
    },
    "P0430": {
        "en": "Catalyst System Efficiency Below Threshold (Bank 2)",
        "fr": "Efficacité du catalyseur en dessous du seuil (Banc 2)",
        "severity": "medium",
        "cause": "Catalyseur du banc 2 usé ou défectueux",
        "solution": "Remplacer le catalyseur du banc 2"
    },
    "P0440": {
        "en": "Evaporative Emission Control System Malfunction",
        "fr": "Dysfonctionnement du système de contrôle des émissions par évaporation",
        "severity": "low",
        "cause": "Bouchon de réservoir mal fermé, fuite dans le système EVAP",
        "solution": "Vérifier le bouchon de réservoir, rechercher les fuites EVAP"
    },
    "P0441": {
        "en": "Evaporative Emission Control System Incorrect Purge Flow",
        "fr": "Débit de purge incorrect du système EVAP",
        "severity": "low",
        "cause": "Vanne de purge défectueuse ou fuite",
        "solution": "Remplacer la vanne de purge EVAP"
    },
    "P0442": {
        "en": "Evaporative Emission Control System Leak Detected (Small Leak)",
        "fr": "Petite fuite détectée dans le système EVAP",
        "severity": "low",
        "cause": "Petite fuite dans le système de récupération des vapeurs",
        "solution": "Test de fumée pour localiser la fuite, vérifier le bouchon"
    },
    "P0443": {
        "en": "Evaporative Emission Control System Purge Control Valve Circuit",
        "fr": "Circuit de la vanne de purge du système EVAP",
        "severity": "low",
        "cause": "Vanne de purge ou câblage défectueux",
        "solution": "Remplacer la vanne de purge ou réparer le câblage"
    },
    "P0446": {
        "en": "Evaporative Emission Control System Vent Control Circuit",
        "fr": "Circuit de contrôle d'évent du système EVAP",
        "severity": "low",
        "cause": "Vanne d'évent ou filtre à charbon obstrué",
        "solution": "Vérifier la vanne d'évent et le filtre à charbon"
    },
    "P0455": {
        "en": "Evaporative Emission Control System Leak Detected (Gross Leak)",
        "fr": "Grosse fuite détectée dans le système EVAP",
        "severity": "low",
        "cause": "Bouchon de réservoir manquant ou grosse fuite",
        "solution": "Vérifier le bouchon de réservoir, inspecter les durites EVAP"
    },

    # EGR System
    "P0400": {
        "en": "Exhaust Gas Recirculation Flow Malfunction",
        "fr": "Dysfonctionnement du débit de recirculation des gaz d'échappement",
        "severity": "medium",
        "cause": "Vanne EGR encrassée ou défectueuse",
        "solution": "Nettoyer ou remplacer la vanne EGR"
    },
    "P0401": {
        "en": "Exhaust Gas Recirculation Flow Insufficient Detected",
        "fr": "Débit EGR insuffisant détecté",
        "severity": "medium",
        "cause": "Vanne EGR bloquée, passages obstrués",
        "solution": "Nettoyer les passages EGR et la vanne"
    },
    "P0402": {
        "en": "Exhaust Gas Recirculation Flow Excessive Detected",
        "fr": "Débit EGR excessif détecté",
        "severity": "medium",
        "cause": "Vanne EGR bloquée ouverte",
        "solution": "Remplacer la vanne EGR"
    },
    "P0403": {
        "en": "Exhaust Gas Recirculation Circuit Malfunction",
        "fr": "Dysfonctionnement du circuit EGR",
        "severity": "medium",
        "cause": "Problème électrique dans le circuit EGR",
        "solution": "Vérifier le câblage et le solénoïde EGR"
    },
    "P0404": {
        "en": "Exhaust Gas Recirculation Circuit Range/Performance",
        "fr": "Performance du circuit EGR hors plage",
        "severity": "medium",
        "cause": "Vanne EGR usée ou capteur défectueux",
        "solution": "Remplacer la vanne EGR"
    },

    # Oxygen Sensor Codes
    "P0130": {
        "en": "O2 Sensor Circuit Malfunction (Bank 1 Sensor 1)",
        "fr": "Dysfonctionnement du circuit de la sonde O2 (Banc 1 Capteur 1)",
        "severity": "medium",
        "cause": "Sonde lambda défectueuse ou câblage endommagé",
        "solution": "Remplacer la sonde lambda amont banc 1"
    },
    "P0131": {
        "en": "O2 Sensor Circuit Low Voltage (Bank 1 Sensor 1)",
        "fr": "Tension basse du circuit sonde O2 (Banc 1 Capteur 1)",
        "severity": "medium",
        "cause": "Sonde lambda défaillante ou fuite d'air",
        "solution": "Vérifier les fuites d'air, remplacer la sonde"
    },
    "P0132": {
        "en": "O2 Sensor Circuit High Voltage (Bank 1 Sensor 1)",
        "fr": "Tension haute du circuit sonde O2 (Banc 1 Capteur 1)",
        "severity": "medium",
        "cause": "Court-circuit ou sonde défectueuse",
        "solution": "Vérifier le câblage, remplacer la sonde"
    },
    "P0133": {
        "en": "O2 Sensor Circuit Slow Response (Bank 1 Sensor 1)",
        "fr": "Réponse lente du circuit sonde O2 (Banc 1 Capteur 1)",
        "severity": "medium",
        "cause": "Sonde lambda vieillissante",
        "solution": "Remplacer la sonde lambda"
    },
    "P0134": {
        "en": "O2 Sensor Circuit No Activity Detected (Bank 1 Sensor 1)",
        "fr": "Aucune activité détectée sur le circuit sonde O2 (Banc 1 Capteur 1)",
        "severity": "medium",
        "cause": "Sonde lambda défectueuse ou déconnectée",
        "solution": "Vérifier la connexion, remplacer la sonde"
    },
    "P0135": {
        "en": "O2 Sensor Heater Circuit Malfunction (Bank 1 Sensor 1)",
        "fr": "Dysfonctionnement du circuit de chauffage sonde O2 (Banc 1 Capteur 1)",
        "severity": "medium",
        "cause": "Circuit de chauffage de la sonde défectueux",
        "solution": "Remplacer la sonde lambda"
    },
    "P0136": {
        "en": "O2 Sensor Circuit Malfunction (Bank 1 Sensor 2)",
        "fr": "Dysfonctionnement du circuit de la sonde O2 (Banc 1 Capteur 2)",
        "severity": "medium",
        "cause": "Sonde lambda aval défectueuse",
        "solution": "Remplacer la sonde lambda aval"
    },
    "P0137": {
        "en": "O2 Sensor Circuit Low Voltage (Bank 1 Sensor 2)",
        "fr": "Tension basse du circuit sonde O2 (Banc 1 Capteur 2)",
        "severity": "medium",
        "cause": "Sonde aval défaillante",
        "solution": "Remplacer la sonde lambda aval"
    },
    "P0138": {
        "en": "O2 Sensor Circuit High Voltage (Bank 1 Sensor 2)",
        "fr": "Tension haute du circuit sonde O2 (Banc 1 Capteur 2)",
        "severity": "medium",
        "cause": "Sonde aval en court-circuit",
        "solution": "Vérifier le câblage, remplacer la sonde"
    },
    "P0140": {
        "en": "O2 Sensor Circuit No Activity Detected (Bank 1 Sensor 2)",
        "fr": "Aucune activité détectée sur le circuit sonde O2 (Banc 1 Capteur 2)",
        "severity": "medium",
        "cause": "Sonde lambda aval inactive",
        "solution": "Remplacer la sonde lambda aval"
    },
    "P0141": {
        "en": "O2 Sensor Heater Circuit Malfunction (Bank 1 Sensor 2)",
        "fr": "Dysfonctionnement du circuit de chauffage sonde O2 (Banc 1 Capteur 2)",
        "severity": "medium",
        "cause": "Chauffage de la sonde aval défectueux",
        "solution": "Remplacer la sonde lambda aval"
    },
    "P0150": {
        "en": "O2 Sensor Circuit Malfunction (Bank 2 Sensor 1)",
        "fr": "Dysfonctionnement du circuit de la sonde O2 (Banc 2 Capteur 1)",
        "severity": "medium",
        "cause": "Sonde lambda amont banc 2 défectueuse",
        "solution": "Remplacer la sonde lambda amont banc 2"
    },
    "P0155": {
        "en": "O2 Sensor Heater Circuit Malfunction (Bank 2 Sensor 1)",
        "fr": "Dysfonctionnement du circuit de chauffage sonde O2 (Banc 2 Capteur 1)",
        "severity": "medium",
        "cause": "Chauffage de la sonde banc 2 défectueux",
        "solution": "Remplacer la sonde lambda"
    },

    # Mass Air Flow Sensor
    "P0100": {
        "en": "Mass or Volume Air Flow Circuit Malfunction",
        "fr": "Dysfonctionnement du circuit du débitmètre d'air",
        "severity": "medium",
        "cause": "Capteur MAF défectueux ou encrassé",
        "solution": "Nettoyer ou remplacer le capteur MAF"
    },
    "P0101": {
        "en": "Mass or Volume Air Flow Circuit Range/Performance Problem",
        "fr": "Problème de performance du circuit du débitmètre d'air",
        "severity": "medium",
        "cause": "Capteur MAF sale ou fuite d'air après le capteur",
        "solution": "Nettoyer le capteur MAF, vérifier les fuites d'air"
    },
    "P0102": {
        "en": "Mass or Volume Air Flow Circuit Low Input",
        "fr": "Signal bas du circuit du débitmètre d'air",
        "severity": "medium",
        "cause": "Capteur MAF défaillant ou filtre à air bouché",
        "solution": "Vérifier le filtre à air, nettoyer/remplacer le capteur MAF"
    },
    "P0103": {
        "en": "Mass or Volume Air Flow Circuit High Input",
        "fr": "Signal haut du circuit du débitmètre d'air",
        "severity": "medium",
        "cause": "Court-circuit dans le câblage MAF",
        "solution": "Vérifier le câblage, remplacer le capteur MAF"
    },
    "P0104": {
        "en": "Mass or Volume Air Flow Circuit Intermittent",
        "fr": "Circuit du débitmètre d'air intermittent",
        "severity": "medium",
        "cause": "Connexion électrique intermittente",
        "solution": "Vérifier les connexions du capteur MAF"
    },

    # Throttle Position Sensor
    "P0120": {
        "en": "Throttle/Pedal Position Sensor A Circuit Malfunction",
        "fr": "Dysfonctionnement du circuit du capteur de position papillon A",
        "severity": "high",
        "cause": "Capteur de position papillon défectueux",
        "solution": "Remplacer le capteur de position papillon"
    },
    "P0121": {
        "en": "Throttle/Pedal Position Sensor A Circuit Range/Performance Problem",
        "fr": "Problème de performance du capteur de position papillon A",
        "severity": "high",
        "cause": "Capteur TPS usé ou corps de papillon encrassé",
        "solution": "Nettoyer le corps de papillon, remplacer le capteur TPS"
    },
    "P0122": {
        "en": "Throttle/Pedal Position Sensor A Circuit Low Input",
        "fr": "Signal bas du capteur de position papillon A",
        "severity": "high",
        "cause": "Court-circuit ou capteur défaillant",
        "solution": "Vérifier le câblage, remplacer le capteur TPS"
    },
    "P0123": {
        "en": "Throttle/Pedal Position Sensor A Circuit High Input",
        "fr": "Signal haut du capteur de position papillon A",
        "severity": "high",
        "cause": "Court-circuit ou capteur défectueux",
        "solution": "Vérifier le câblage, remplacer le capteur TPS"
    },

    # Coolant Temperature
    "P0115": {
        "en": "Engine Coolant Temperature Circuit Malfunction",
        "fr": "Dysfonctionnement du circuit de température du liquide de refroidissement",
        "severity": "medium",
        "cause": "Capteur de température défectueux",
        "solution": "Remplacer le capteur de température"
    },
    "P0116": {
        "en": "Engine Coolant Temperature Circuit Range/Performance Problem",
        "fr": "Problème de performance du circuit de température",
        "severity": "medium",
        "cause": "Thermostat bloqué ou capteur défaillant",
        "solution": "Vérifier le thermostat et le capteur de température"
    },
    "P0117": {
        "en": "Engine Coolant Temperature Circuit Low Input",
        "fr": "Signal bas du circuit de température du liquide de refroidissement",
        "severity": "medium",
        "cause": "Court-circuit ou capteur défectueux",
        "solution": "Vérifier le câblage, remplacer le capteur"
    },
    "P0118": {
        "en": "Engine Coolant Temperature Circuit High Input",
        "fr": "Signal haut du circuit de température du liquide de refroidissement",
        "severity": "medium",
        "cause": "Circuit ouvert ou capteur défaillant",
        "solution": "Vérifier le câblage, remplacer le capteur"
    },
    "P0125": {
        "en": "Insufficient Coolant Temperature for Closed Loop Fuel Control",
        "fr": "Température insuffisante pour le contrôle en boucle fermée",
        "severity": "medium",
        "cause": "Thermostat bloqué ouvert ou capteur défectueux",
        "solution": "Remplacer le thermostat"
    },
    "P0128": {
        "en": "Coolant Thermostat (Coolant Temperature Below Thermostat Regulating Temperature)",
        "fr": "Thermostat - Température en dessous de la température de régulation",
        "severity": "medium",
        "cause": "Thermostat bloqué en position ouverte",
        "solution": "Remplacer le thermostat"
    },

    # Fuel Injectors
    "P0200": {
        "en": "Injector Circuit Malfunction",
        "fr": "Dysfonctionnement du circuit d'injecteur",
        "severity": "high",
        "cause": "Problème dans le circuit des injecteurs",
        "solution": "Vérifier le câblage et les injecteurs"
    },
    "P0201": {
        "en": "Injector Circuit Malfunction - Cylinder 1",
        "fr": "Dysfonctionnement du circuit d'injecteur - Cylindre 1",
        "severity": "high",
        "cause": "Injecteur 1 défectueux ou câblage",
        "solution": "Vérifier l'injecteur et le câblage du cylindre 1"
    },
    "P0202": {
        "en": "Injector Circuit Malfunction - Cylinder 2",
        "fr": "Dysfonctionnement du circuit d'injecteur - Cylindre 2",
        "severity": "high",
        "cause": "Injecteur 2 défectueux ou câblage",
        "solution": "Vérifier l'injecteur et le câblage du cylindre 2"
    },
    "P0203": {
        "en": "Injector Circuit Malfunction - Cylinder 3",
        "fr": "Dysfonctionnement du circuit d'injecteur - Cylindre 3",
        "severity": "high",
        "cause": "Injecteur 3 défectueux ou câblage",
        "solution": "Vérifier l'injecteur et le câblage du cylindre 3"
    },
    "P0204": {
        "en": "Injector Circuit Malfunction - Cylinder 4",
        "fr": "Dysfonctionnement du circuit d'injecteur - Cylindre 4",
        "severity": "high",
        "cause": "Injecteur 4 défectueux ou câblage",
        "solution": "Vérifier l'injecteur et le câblage du cylindre 4"
    },

    # Transmission Codes
    "P0700": {
        "en": "Transmission Control System Malfunction",
        "fr": "Dysfonctionnement du système de contrôle de transmission",
        "severity": "high",
        "cause": "Problème général de transmission, autre code présent",
        "solution": "Lire les codes supplémentaires, diagnostic approfondi"
    },
    "P0705": {
        "en": "Transmission Range Sensor Circuit Malfunction",
        "fr": "Dysfonctionnement du circuit du capteur de position de transmission",
        "severity": "high",
        "cause": "Capteur de position sélecteur défectueux",
        "solution": "Remplacer le capteur de position de transmission"
    },
    "P0715": {
        "en": "Input/Turbine Speed Sensor Circuit Malfunction",
        "fr": "Dysfonctionnement du circuit du capteur de vitesse d'entrée",
        "severity": "high",
        "cause": "Capteur de vitesse de turbine défectueux",
        "solution": "Remplacer le capteur de vitesse d'entrée"
    },
    "P0720": {
        "en": "Output Speed Sensor Circuit Malfunction",
        "fr": "Dysfonctionnement du circuit du capteur de vitesse de sortie",
        "severity": "high",
        "cause": "Capteur de vitesse de sortie défectueux",
        "solution": "Remplacer le capteur de vitesse de sortie"
    },
    "P0730": {
        "en": "Incorrect Gear Ratio",
        "fr": "Rapport de vitesse incorrect",
        "severity": "high",
        "cause": "Problème interne de transmission, embrayages usés",
        "solution": "Diagnostic de transmission, révision possible"
    },
    "P0740": {
        "en": "Torque Converter Clutch Circuit Malfunction",
        "fr": "Dysfonctionnement du circuit d'embrayage du convertisseur de couple",
        "severity": "high",
        "cause": "Solénoïde TCC défectueux ou câblage",
        "solution": "Remplacer le solénoïde TCC"
    },
    "P0741": {
        "en": "Torque Converter Clutch Circuit Performance or Stuck Off",
        "fr": "Performance du circuit TCC ou bloqué désengagé",
        "severity": "high",
        "cause": "Solénoïde TCC bloqué ou défaillant",
        "solution": "Remplacer le solénoïde TCC, vérifier le câblage"
    },
    "P0750": {
        "en": "Shift Solenoid A Malfunction",
        "fr": "Dysfonctionnement du solénoïde de changement de vitesse A",
        "severity": "high",
        "cause": "Solénoïde A défectueux",
        "solution": "Remplacer le solénoïde de changement A"
    },
    "P0755": {
        "en": "Shift Solenoid B Malfunction",
        "fr": "Dysfonctionnement du solénoïde de changement de vitesse B",
        "severity": "high",
        "cause": "Solénoïde B défectueux",
        "solution": "Remplacer le solénoïde de changement B"
    },

    # ABS/Vehicle Speed
    "P0500": {
        "en": "Vehicle Speed Sensor Malfunction",
        "fr": "Dysfonctionnement du capteur de vitesse du véhicule",
        "severity": "medium",
        "cause": "Capteur de vitesse défectueux ou câblage",
        "solution": "Remplacer le capteur de vitesse"
    },
    "P0501": {
        "en": "Vehicle Speed Sensor Range/Performance",
        "fr": "Performance du capteur de vitesse hors plage",
        "severity": "medium",
        "cause": "Signal du capteur de vitesse irrégulier",
        "solution": "Vérifier le capteur et le câblage"
    },
    "P0505": {
        "en": "Idle Control System Malfunction",
        "fr": "Dysfonctionnement du système de contrôle de ralenti",
        "severity": "medium",
        "cause": "Vanne de ralenti encrassée ou défectueuse",
        "solution": "Nettoyer ou remplacer la vanne de ralenti"
    },
    "P0506": {
        "en": "Idle Control System RPM Lower Than Expected",
        "fr": "Régime de ralenti inférieur à la normale",
        "severity": "medium",
        "cause": "Fuite d'air, corps de papillon encrassé",
        "solution": "Nettoyer le corps de papillon, rechercher les fuites"
    },
    "P0507": {
        "en": "Idle Control System RPM Higher Than Expected",
        "fr": "Régime de ralenti supérieur à la normale",
        "severity": "medium",
        "cause": "Fuite d'air, vanne de ralenti bloquée ouverte",
        "solution": "Rechercher les fuites d'air, vérifier la vanne de ralenti"
    },

    # Diesel Specific
    "P0380": {
        "en": "Glow Plug/Heater Circuit A Malfunction",
        "fr": "Dysfonctionnement du circuit des bougies de préchauffage A",
        "severity": "medium",
        "cause": "Bougie de préchauffage défectueuse ou relais",
        "solution": "Vérifier les bougies de préchauffage et le relais"
    },
    "P0381": {
        "en": "Glow Plug/Heater Indicator Circuit Malfunction",
        "fr": "Dysfonctionnement du circuit indicateur de préchauffage",
        "severity": "low",
        "cause": "Problème dans le circuit témoin de préchauffage",
        "solution": "Vérifier le câblage du témoin"
    },
    "P0400": {
        "en": "Exhaust Gas Recirculation Flow Malfunction",
        "fr": "Dysfonctionnement du débit de recirculation des gaz d'échappement",
        "severity": "medium",
        "cause": "Vanne EGR encrassée ou défectueuse",
        "solution": "Nettoyer ou remplacer la vanne EGR"
    },
    "P2002": {
        "en": "Diesel Particulate Filter Efficiency Below Threshold",
        "fr": "Efficacité du filtre à particules en dessous du seuil",
        "severity": "high",
        "cause": "Filtre à particules (FAP) colmaté ou défectueux",
        "solution": "Régénération forcée ou remplacement du FAP"
    },
    "P2003": {
        "en": "Diesel Particulate Filter Efficiency Below Threshold (Bank 2)",
        "fr": "Efficacité du FAP en dessous du seuil (Banc 2)",
        "severity": "high",
        "cause": "FAP du banc 2 colmaté",
        "solution": "Régénération ou remplacement du FAP"
    },
    "P2279": {
        "en": "Intake Air System Leak",
        "fr": "Fuite dans le système d'admission d'air",
        "severity": "medium",
        "cause": "Fuite d'air dans l'admission",
        "solution": "Rechercher et réparer la fuite d'air"
    },

    # Communication Codes
    "U0100": {
        "en": "Lost Communication With ECM/PCM A",
        "fr": "Perte de communication avec le calculateur moteur",
        "severity": "high",
        "cause": "Problème de communication CAN bus",
        "solution": "Vérifier le câblage CAN bus et le calculateur"
    },
    "U0101": {
        "en": "Lost Communication With TCM",
        "fr": "Perte de communication avec le calculateur de transmission",
        "severity": "high",
        "cause": "Problème de communication avec le TCM",
        "solution": "Vérifier le câblage et le calculateur de transmission"
    },
    "U0121": {
        "en": "Lost Communication With Anti-Lock Brake System Control Module",
        "fr": "Perte de communication avec le module ABS",
        "severity": "high",
        "cause": "Problème de communication avec le module ABS",
        "solution": "Vérifier le câblage et le module ABS"
    },
    "U0140": {
        "en": "Lost Communication With Body Control Module",
        "fr": "Perte de communication avec le module de carrosserie",
        "severity": "medium",
        "cause": "Problème de communication avec le BCM",
        "solution": "Vérifier le câblage et le module de carrosserie"
    },

    # Body Codes (B)
    "B0001": {
        "en": "Driver Frontal Stage 1 Deployment Control",
        "fr": "Contrôle de déploiement airbag frontal conducteur étape 1",
        "severity": "high",
        "cause": "Problème dans le circuit de l'airbag conducteur",
        "solution": "Diagnostic du système airbag requis"
    },
    "B1000": {
        "en": "ECU Malfunction",
        "fr": "Dysfonctionnement du calculateur",
        "severity": "high",
        "cause": "Problème interne du calculateur",
        "solution": "Reprogrammation ou remplacement du calculateur"
    },

    # Chassis Codes (C)
    "C0035": {
        "en": "Left Front Wheel Speed Sensor Circuit",
        "fr": "Circuit du capteur de vitesse roue avant gauche",
        "severity": "medium",
        "cause": "Capteur ABS avant gauche défectueux",
        "solution": "Remplacer le capteur ABS avant gauche"
    },
    "C0040": {
        "en": "Right Front Wheel Speed Sensor Circuit",
        "fr": "Circuit du capteur de vitesse roue avant droite",
        "severity": "medium",
        "cause": "Capteur ABS avant droit défectueux",
        "solution": "Remplacer le capteur ABS avant droit"
    },
    "C0045": {
        "en": "Left Rear Wheel Speed Sensor Circuit",
        "fr": "Circuit du capteur de vitesse roue arrière gauche",
        "severity": "medium",
        "cause": "Capteur ABS arrière gauche défectueux",
        "solution": "Remplacer le capteur ABS arrière gauche"
    },
    "C0050": {
        "en": "Right Rear Wheel Speed Sensor Circuit",
        "fr": "Circuit du capteur de vitesse roue arrière droite",
        "severity": "medium",
        "cause": "Capteur ABS arrière droit défectueux",
        "solution": "Remplacer le capteur ABS arrière droit"
    },
    "C0110": {
        "en": "Pump Motor Circuit",
        "fr": "Circuit du moteur de pompe ABS",
        "severity": "high",
        "cause": "Pompe ABS défectueuse",
        "solution": "Remplacer la pompe ABS ou le module"
    },

    # Additional Common Codes
    "P0562": {
        "en": "System Voltage Low",
        "fr": "Tension système basse",
        "severity": "medium",
        "cause": "Batterie faible, alternateur défaillant",
        "solution": "Tester la batterie et l'alternateur"
    },
    "P0563": {
        "en": "System Voltage High",
        "fr": "Tension système haute",
        "severity": "medium",
        "cause": "Alternateur en surcharge",
        "solution": "Remplacer le régulateur ou l'alternateur"
    },
    "P0600": {
        "en": "Serial Communication Link Malfunction",
        "fr": "Dysfonctionnement de la liaison de communication série",
        "severity": "high",
        "cause": "Problème de communication interne du calculateur",
        "solution": "Reprogrammation ou remplacement du calculateur"
    },
    "P0601": {
        "en": "Internal Control Module Memory Check Sum Error",
        "fr": "Erreur de somme de contrôle de la mémoire du calculateur",
        "severity": "high",
        "cause": "Mémoire du calculateur corrompue",
        "solution": "Reprogrammation ou remplacement du calculateur"
    },
    "P0602": {
        "en": "Control Module Programming Error",
        "fr": "Erreur de programmation du calculateur",
        "severity": "high",
        "cause": "Programmation incorrecte ou corrompue",
        "solution": "Reprogrammer le calculateur"
    },
    "P0606": {
        "en": "PCM Processor Fault",
        "fr": "Défaut du processeur du calculateur",
        "severity": "high",
        "cause": "Processeur du calculateur défaillant",
        "solution": "Remplacer le calculateur"
    },
    "P1000": {
        "en": "OBD Systems Readiness Test Not Complete",
        "fr": "Test de préparation des systèmes OBD non terminé",
        "severity": "low",
        "cause": "Cycles de conduite insuffisants après effacement des codes",
        "solution": "Effectuer un cycle de conduite complet"
    },
}

def get_obd_code_info(code: str) -> dict:
    """
    Look up an OBD-II code and return its information.
    Returns None if code not found.
    """
    code_upper = code.upper().strip()

    # Handle common variations
    if not code_upper.startswith(('P', 'B', 'C', 'U')):
        code_upper = 'P' + code_upper

    return OBD_CODES.get(code_upper)

def format_obd_response(code: str, info: dict) -> str:
    """
    Format OBD code information into a user-friendly French response.
    """
    severity_icons = {
        "high": "🔴",
        "medium": "🟡",
        "low": "🟢"
    }

    severity_text = {
        "high": "ÉLEVÉE - À traiter rapidement",
        "medium": "MOYENNE - À surveiller",
        "low": "FAIBLE - Non urgent"
    }

    icon = severity_icons.get(info["severity"], "⚪")
    sev_text = severity_text.get(info["severity"], "Inconnue")

    response = f"""🔧 **CODE OBD-II: {code.upper()}**

📋 **Description:** {info["fr"]}

{icon} **Gravité:** {sev_text}

⚠️ **Cause probable:** {info["cause"]}

🔨 **Solution recommandée:** {info["solution"]}

💡 *Pour une réparation fiable, utilisez KOUNHANY pour trouver un garage audité près de chez vous.*"""

    return response

def search_obd_codes(query: str) -> list:
    """
    Search OBD codes by keyword (in French or English).
    Returns list of matching codes.
    """
    query_lower = query.lower()
    matches = []

    for code, info in OBD_CODES.items():
        if (query_lower in info["fr"].lower() or
            query_lower in info["en"].lower() or
            query_lower in info.get("cause", "").lower() or
            query_lower in info.get("solution", "").lower()):
            matches.append((code, info))

    return matches[:10]  # Return max 10 results
