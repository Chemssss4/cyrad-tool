# par pitié ne pas volé mon code et ne rien modiffié svp sah
import requests
import random
import string
import time
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

def webhook_spammer(webhook_url, spam_message, spam_count):
    try:
        for _ in range(spam_count):
            data = {'content': spam_message}
            response = requests.post(webhook_url, json=data)
            if response.status_code == 204:
                print(f"{Colors.green}Message envoyé avec succès !{Colors.reset}")
            else:
                print(f"{Colors.red}Erreur HTTP : {response.status_code}{Colors.reset}")
            time.sleep(0.1)  
    except Exception as e:
        error(e)

def run():
    try:
        print(f"{Colors.blue}Tool8 - Webhook Spammer{Colors.reset}")

        webhook_url = input(f"{Colors.yellow}Entrez l'URL du webhook : {Colors.reset}")
        spam_message = input(f"{Colors.yellow}Entrez le message à envoyer : {Colors.reset}")
        spam_count = int(input(f"{Colors.yellow}Entrez le nombre de messages à envoyer : {Colors.reset}"))

        confirm = input(f"{Colors.red}Êtes-vous sûr de vouloir spammer ce webhook ? Cette action peut être détectée et peut entraîner des restrictions. (oui/non) : {Colors.reset}").strip().lower()
        if confirm == 'oui':
            webhook_spammer(webhook_url, spam_message, spam_count)
        else:
            print(f"{Colors.yellow}Spam annulé.{Colors.reset}")

        continue_prompt()
    except Exception as e:
        error(e)

if __name__ == "__main__":
    run()
