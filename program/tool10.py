# par pitié ne pas volé mon code et ne rien modiffié svp sah
import requests
import os
from pystyle import Colors

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def continue_prompt():
    input(f"\n{Colors.green}Appuyez sur Entrée pour continuer...{Colors.reset}")

def error(e):
    print(f"{Colors.red}Une erreur est survenue : {e}{Colors.reset}")
    continue_prompt()
    clear()

def delete_webhook(webhook_url):
    try:
        response = requests.delete(webhook_url)
        if response.status_code == 204:
            print(f"{Colors.green}Webhook supprimé avec succès !{Colors.reset}")
        elif response.status_code == 404:
            print(f"{Colors.red}Webhook non trouvé (404). Vérifiez l'URL.{Colors.reset}")
        elif response.status_code == 403:
            print(f"{Colors.red}Interdiction d'accéder à ce webhook (403).{Colors.reset}")
        else:
            print(f"{Colors.red}Erreur HTTP : {response.status_code}{Colors.reset}")
    except Exception as e:
        error(e)

def run():
    try:

        print(f"{Colors.blue}Tool10 - Suppression de Webhook{Colors.reset}")

        webhook_url = input(f"{Colors.yellow}Entrez l'URL du webhook à supprimer : {Colors.reset}")

        confirm = input(f"{Colors.red}Êtes-vous sûr de vouloir supprimer ce webhook ? Cette action est irréversible ! (oui/non) : {Colors.reset}").strip().lower()
        if confirm == 'oui':
            delete_webhook(webhook_url)
        else:
            print(f"{Colors.yellow}Suppression annulée.{Colors.reset}")

        continue_prompt()
    except Exception as e:
        error(e)

if __name__ == "__main__":
    run()
