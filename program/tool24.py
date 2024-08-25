# par pitié ne pas volé mon code et ne rien modiffié svp sah

import requests
import time
import threading
from pystyle import Colors

def obtenir_entetes(token):
    entetes = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }
    return entetes

def lire_statuts():
    print(f"\n {Colors.red}Entrez les statuts que vous souhaitez définir et tapez 'FIN' lorsque vous avez terminé :")
    statuts = []
    index = 1
    
    while True:
        statut = input(f'Statut {index} : ')
        
        if statut.upper() == "FIN":
            break
        
        statuts.append(statut)
        index += 1
    
    return statuts

def obtenir_id_utilisateur(token):
    entetes = obtenir_entetes(token)
    try:
        r = requests.get("https://discord.com/api/v6/users/@me", headers=entetes)
        if r.status_code == 200:
            return r.json()['id']
        else:
            return None
    except Exception as e:
        return None

def changer_statut(token, texte):
    entetes = obtenir_entetes(token)
    parametres = {
        'custom_status': {
            'text': texte,
        },
    }
    try:
        r = requests.patch("https://discord.com/api/v6/users/@me/settings", headers=entetes, json=parametres)
        if r.status_code == 200:
            print(f'token={token[:20]}... [RÉUSSI]')
        else:
            print(f"token={token[:20]}... [ERREUR] ({r.status_code})")
    except Exception as e:
        pass

def gestionnaire_statuts():
    token = input(f'{Colors.red}Entrez le token : ')
    
    statuts = lire_statuts()
    
    while True:
        try:
            frequence_temps = int(input(f'{Colors.red}Temps entre chaque changement de statut (en secondes) : '))
            break
        except ValueError:
            print(f'{Colors.red}Veuillez entrer un nombre entier pour le temps.')
    
    id_utilisateur = obtenir_id_utilisateur(token)
    if not id_utilisateur:
        print("Impossible de récupérer l'ID de l'utilisateur. Arrêt du programme.")
        return
        
    try:
        while True:
            for texte in statuts:
                thread = threading.Thread(target=changer_statut, args=(token, texte))
                thread.start()
                thread.join()
                time.sleep(frequence_temps)
    except KeyboardInterrupt:
        print(f"\nInterruption du changement de statut.")

def run():
    gestionnaire_statuts()

if __name__ == "__main__":
    run()
