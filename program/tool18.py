# par pitié ne pas volé mon code et ne rien modiffié svp sah
import requests
import os
import threading
import sys
from pystyle import Colors

def print_title(title):
    print(f"{Colors.red}{'=' * 60}\n{title}\n{'=' * 60}{Colors.reset}")

def print_error(message):
    print(f"{Colors.red}Erreur : {message}{Colors.reset}")

def print_info(message):
    print(f"{Colors.red}{message}{Colors.reset}")

def get_dm_channel_ids(token_discord):
    try:
        print_info("Récupération des ID des canaux DM...")
        response = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token_discord})
        
        if response.status_code == 200:
            channels = response.json()
            dm_channel_ids = [channel['id'] for channel in channels if channel['type'] == 1]
            print_info(f"ID des canaux DM récupérés : {dm_channel_ids}")
            return dm_channel_ids
        else:
            print_error(f"Code de statut {response.status_code} : Impossible de récupérer les canaux DM.")
            return []

    except Exception as e:
        print_error(f"Erreur lors de la récupération des ID des canaux DM : {e}")
        return []

def mass_dm(token_discord, dm_channel_ids, message):
    try:
        print_info("Envoi des messages...")
        for channel_id in dm_channel_ids:
            response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",
                                     headers={'Authorization': token_discord, 'Content-Type': 'application/json'},
                                     json={"content": message})
            if response.status_code == 200:
                print_info(f"Message envoyé au canal ID : {channel_id}")
            else:
                print_error(f"Code de statut {response.status_code} : Impossible d'envoyer le message au canal ID : {channel_id}")

    except Exception as e:
        print_error(f"Erreur lors de l'envoi du message : {e}")

def execute_mass_dm():
    try:
        print_title("Exécution de l'envoi de messages")
        token_discord = input(f"{Colors.red}Entrez votre jeton Discord : {Colors.reset}").strip()
        message = input(f"{Colors.red}Entrez le message à envoyer : {Colors.reset}").strip()

        if not token_discord or not message:
            print_error("Jeton ou message manquant. Veuillez réessayer.")
            return

        dm_channel_ids = get_dm_channel_ids(token_discord)

        if not dm_channel_ids:
            print_error("Aucun ID de canal DM collecté. Sortie.")
            return

        print_info(f"Nombre total d'ID de canaux DM collectés : {len(dm_channel_ids)}")

        proceed = input(f"{Colors.red}Voulez-vous envoyer le message à tous les canaux DM collectés ? (o/n) : {Colors.reset}").strip().lower()

        if proceed == 'o':
            for channel_id in dm_channel_ids:
                t = threading.Thread(target=mass_dm, args=(token_discord, [channel_id], message))
                t.start()
                t.join()
                print_info(f"Envoi des messages terminé pour le canal {channel_id}.")
        else:
            print_info("Sortie sans envoi de messages.")

        input(f"{Colors.red}Appuyez sur Entrée pour revenir au menu principal...{Colors.reset}")

    except Exception as e:
        print_error(f"Erreur : {e}")

def display_menu():
    menu = f"""
{Colors.red}Roner - Menu Principal{Colors.reset}
{Colors.red}───────────────────────────────{Colors.reset}
1. Envoi de messages de masse aux canaux Discord
2. Quitter
    """
    print(menu)

def handle_menu_choice(choice):
    if choice == '1':
        execute_mass_dm()
    elif choice == '2':
        print_info("Fermeture du programme.")
        sys.exit(0)  
    else:
        print_error("Choix invalide. Veuillez entrer une option valide.")

def run():
    while True:
        try:
            display_menu()
            choice = input(f"{Colors.red}Entrez votre choix : {Colors.reset}").strip()
            print_info(f"Choix de l'utilisateur : {choice}")
            handle_menu_choice(choice)
        except Exception as e:
            print_error(f"Erreur dans le menu : {e}")
