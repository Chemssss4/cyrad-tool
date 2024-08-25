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

def get_webhook_info(webhook_url):
    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            webhook_info = response.json()
            print(f"{Colors.blue}Informations sur le webhook :{Colors.reset}")
            print(f"ID : {webhook_info['id']}")
            print(f"Token : {webhook_info['token']}")
            print(f"Name : {webhook_info['name']}")
            print(f"Avatar : {webhook_info['avatar']}")
            print(f"Type  : {'bot' if webhook_info['type'] == 1 else 'webhook utilisateur'}")
            print(f"Channel ID : {webhook_info['channel_id']}")
            print(f"Server ID  : {webhook_info['guild_id']}")

            print("\nUser information associated with the Webhook:")
            if 'user' in webhook_info and webhook_info['user']:
                user_info = webhook_info['user']
                print(f"ID : {user_info['id']}")
                print(f"Name : {user_info['username']}")
                print(f"DisplayName : {user_info['global_name']}")
                print(f"Number : {user_info['discriminator']}")
                print(f"Avatar : {user_info['avatar']}")
                print(f"Flags : {user_info['flags']} Publique: {user_info['public_flags']}")
                print(f"Color : {user_info['accent_color']}")
                print(f"Decoration : {user_info['avatar_decoration_data']}")
                print(f"Banner : {user_info['banner_color']}")
                print("")
        else:
            print(f"{Colors.red}Erreur HTTP : {response.status_code}{Colors.reset}")
    except Exception as e:
        error(e)

def run():
    try:
        print(f"{Colors.blue}Tool9 - Informations sur le Webhook{Colors.reset}")

        webhook_url = input(f"{Colors.yellow}Entrez l'URL du webhook : {Colors.reset}")
        get_webhook_info(webhook_url)

        continue_prompt()
    except Exception as e:
        error(e)

if __name__ == "__main__":
    run()
