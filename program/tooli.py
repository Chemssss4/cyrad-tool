# program/tool1.py

import os

def run():
    """Affiche les informations de l'outil et permet de recharger."""
    while True:
        # Efface l'écran
        os.system('cls' if os.name == 'nt' else 'clear')

        # Deuxième partie: affichage des informations
        print("""\
                                                                      .+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.
                                                                     (       ,----..                           ___                            ___          )
                                                                      )     /   /   \\                        ,--.'|_                        ,--.'|_       ( 
                                                                     (     |   :     :  ,---.        ,---,   |  | :,'                       |  | :,'       )
                                                                      )    .   |  ;. / '   ,\\   ,-+-. /  |  :  : ' :                       :  : ' :      ( 
                                                                     (     .   ; /--` /   /   | ,--.'|'   |.;__,'  /    ,--.--.     ,---. .;__,'  /        )
                                                                      )    ;   | ;   .   ; ,. :|   |  ,"' ||  |   |    /       \\   /     \\|  |   |        ( 
                                                                     (     |   : |   '   | |: :|   | /  | |:__,'| :   .--.  .-. | /    / ':__,'| :         )
                                                                      )    .   | '___'   | .; :|   | |  | |  '  : |__  \\__\\/ : . ..    ' /   '  : |__      ( 
                                                                     (     '   ; : .'|   :    ||   | |  |/   |  | '.'| ," .--.; |'   ; :__  |  | '.'|      )
                                                                      )    '   | '/  :\\   \\  / |   | |--'    ;  :    ;/  /  ,.  |'   | '.'| ;  :    ;     ( 
                                                                     (     |   :    /  `----'  |   |/        |  ,   /;  :   .'   \\   :    : |  ,   /       )
                                                                      )     \\   \\ .'           '---'          ---`-' |  ,     .-./\\   \\  /   ---`-'       ( 
                                                                     (       `---`                                    `--`---'     `----'                  )
                                                                      "+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+" 
""")

        # Troisième partie: affichage des informations de l'outil
        print("""\
                                                                         ╔══════════════════════════════════════════════════════════════════════════╗
                                                                         ║                         Informations sur l'outil                         ║
                                                                         ║                                                                          ║
                                                                         ║  cyrad est un outil complet et sécurisé pour effectuer diverses    ║
                                                                         ║  tâches informatiques. Développé pour les administrateurs système,       ║
                                                                         ║  les ingénieurs réseau et les développeurs, il offre une large gamme     ║
                                                                         ║  de fonctionnalités pour faciliter la gestion et l'analyse des données.  ║
                                                                         ║                                                                          ║
                                                                         ║  Fonctionnalités principales :                                           ║
                                                                         ║  - Recherche d'informations sur les adresses IP                          ║
                                                                         ║  - Analyse de liens URL et validation de sécurité                        ║
                                                                         ║  - Conversion et encodage de texte                                       ║
                                                                         ║  - Et bien plus encore !                                                 ║
                                                                         ╚═════════════════════════════╗          ╔═════════════════════════════════╝
                                                                                                       ║          ║
                                                                                                  ╔════╝          ╚═══════╗
                                                                                                  ║> Github :   Chemssss4 ║
                                                                                                  ║> discord: cyrad gen  ║
                                                                                                  ╚═══════════════════════╝ 
""")

        # Attendre que l'utilisateur appuie sur une touche pour revenir au menu
        choix = input("\nAppuyez sur [Entrée] pour revenir au menu ").strip().lower()
        
        if choix == '':
            # Arrêter l'exécution de l'outil pour revenir au menu principal
            break
