# par pitié ne pas volé mon code et ne rien modiffié svp sah

import requests
import os
from datetime import datetime
from pystyle import Colors



def print_error(message):
    print(f"{Colors.red}Erreur : {message}{Colors.reset}")

def print_info(message):
    print(f"{Colors.red}{message}{Colors.reset}")

def print_header(header):
    print(f"{Colors.red}{header}{Colors.reset}")

def get_age_of_account(created_at):
    created_at = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f%z")
    now = datetime.now(datetime.timezone.utc)
    age = now - created_at
    return age.days // 365  

def server_lookup():

    invitelink = input(f"{Colors.red}Insérez la partie finale du lien d'invitation du serveur Discord : {Colors.reset}").strip()


    headers = {
        'Authorization': 'bientot dispo'  
    }

    try:
        if "discord.gg" in invitelink:
            code = invitelink.split('/')[-1]
        else:
            code = invitelink
        
        res = requests.get(f"https://discord.com/api/v9/invites/{code}", headers=headers)

        if res.status_code == 200:
            res_json = res.json()

            print_header("Informations sur l'invitation :")
            print_info(f"Lien d'invitation : https://discord.gg/{res_json['code']}")
            print_info(f"Canal : {res_json['channel']['name']} ({res_json['channel']['id']})")
            print_info(f"Date d'expiration : {res_json['expires_at']}\n")

            inviter_id = res_json['inviter']['id']
            inviter_res = requests.get(f"https://discord.com/api/v9/users/{inviter_id}", headers=headers)
            if inviter_res.status_code == 200:
                inviter_json = inviter_res.json()

                print_header("Informations sur l'inviteur :")
                print_info(f"Nom d'utilisateur : {inviter_json['username']}#{inviter_json['discriminator']}")
                print_info(f"ID Utilisateur : {inviter_json['id']}")
                print_info(f"URL de l'avatar : https://cdn.discordapp.com/avatars/{inviter_json['id']}/{inviter_json['avatar']}.png")
                print_info(f"Âge du compte : {get_age_of_account(inviter_json['created_at'])} ans")
                print_info(f"Possède Nitro : {'Oui' if inviter_json.get('premium_type') else 'Non'}\n")
            else:
                print_error(f"Échec de la récupération des informations sur l'inviteur (Code de statut : {inviter_res.status_code})")

            print_header("Informations sur le serveur :")
            print_info(f"Nom : {res_json['guild']['name']}")
            print_info(f"ID Serveur : {res_json['guild']['id']}")
            print_info(f"URL de l'icône : https://cdn.discordapp.com/icons/{res_json['guild']['id']}/{res_json['guild']['icon']}.png")
            print_info(f"Bannière : {res_json['guild']['banner']}")
            print_info(f"Description : {res_json['guild']['description']}")
            print_info(f"Lien d'invitation personnalisé : {res_json['guild']['vanity_url_code']}")
            print_info(f"Niveau de vérification : {res_json['guild']['verification_level']}")
            print_info(f"Écran de chargement : {res_json['guild']['splash']}")
            print_info(f"Fonctionnalités : {', '.join(res_json['guild']['features'])}")
        else:
            print_error(f"Une erreur est survenue lors de l'envoi de la requête (Code de statut : {res.status_code})")
        
    except Exception as e:
        print_error(f"Erreur : {e}")

def run():

    while True:
        server_lookup()
        input(f"{Colors.red}\nAppuyez sur ENTER pour revenir au menu principal{Colors.reset}")

