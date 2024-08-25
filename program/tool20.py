# par pitié ne pas volé mon code et ne rien modiffié svp sah
import requests
import threading
import time
from pystyle import Colors

RAISON_PAR_DÉFAUT = "Contenu inapproprié"  # DEFAULT_REPORT_REASON

# Variable globale pour indiquer si le token est invalide
token_invalide = False

def SignalementMassif(token, serveur_id, canal_id, message_id, raison):
    global token_invalide
    # Vérifier d'abord si le token est valide
    if not vérifier_token(token):
        print(f"{Colors.red}Le jeton est invalide. Arrêt du processus de signalement.")
        return

    for _ in range(500):
        # Si le token est détecté comme invalide pendant l'exécution, arrêter les threads
        if token_invalide:
            break
        threading.Thread(target=Signaler, args=(token, serveur_id, canal_id, message_id, raison)).start()

def vérifier_token(token):
    """Vérifie si le jeton est valide en faisant une requête de test."""
    url = 'https://discordapp.com/api/v8/users/@me'
    en_tetes = {
        'Authorization': token
    }
    réponse = requests.get(url, headers=en_tetes)
    
    if réponse.status_code in (401, 403):  # Code 401 ou 403 signifie token invalide
        return False
    return True

def Signaler(token, serveur_id, canal_id, message_id, raison):
    global token_invalide
    url = 'https://discordapp.com/api/v8/report'
    en_tetes = {  # headers
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'fr-FR',
        'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
        'Content-Type': 'application/json',
        'Authorization': token
    }
    données = {  # payload
        'channel_id': canal_id,
        'message_id': message_id,
        'guild_id': serveur_id,
        'reason': raison
    }

    # Ajouter un délai d'une seconde avant chaque signalement
    time.sleep(1)
    
    réponse = requests.post(url, json=données, headers=en_tetes)
    
    statut = réponse.status_code
    message_réponse = réponse.json().get('message', 'Erreur inconnue')

    if statut == 401 or statut == 403:
        print(f"{Colors.red}Token invalide détecté lors du signalement. Arrêt du processus de signalement.")
        token_invalide = True
        return

    if statut == 201:
        print("Signalement envoyé avec succès !\n")
    else:
        print(f"Erreur : {message_réponse} | Code statut : {statut}\n")

async def run():
    token = input(f"{Colors.red}Entrez votre jeton Discord : ")
    serveur_id = input(f"{Colors.red}Entrez l'ID du serveur : ")
    canal_id = input(f"{Colors.red}Entrez l'ID du canal : ")
    message_id = input(f"{Colors.red}Entrez l'ID du message : ")
    
    raison = input(f"{Colors.red}Entrez la raison du signalement (par défaut : {RAISON_PAR_DÉFAUT}) : ").strip()
    if not raison:
        raison = RAISON_PAR_DÉFAUT

    SignalementMassif(token, serveur_id, canal_id, message_id, raison)
