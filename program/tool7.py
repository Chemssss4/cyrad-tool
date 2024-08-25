# par pitié ne pas volé mon code et ne rien modiffié svp sah
import requests
import json
import random
import string
import threading
from datetime import datetime


class color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

lock = threading.Lock()  


valid_links = []
invalid_count = 0

def current_time_hour():
    """Retourne l'heure actuelle formatée."""
    return datetime.now().strftime("%H:%M:%S")

def send_webhook(embed_content, webhook_url, username_webhook, avatar_webhook):
    """Envoie un message au webhook."""
    payload = {
        'embeds': [embed_content],
        'username': username_webhook,
        'avatar_url': avatar_webhook
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    return response.status_code

def nitro_check(webhook, webhook_url, color_webhook, username_webhook, avatar_webhook):
    """Vérifie un code Nitro généré aléatoirement."""
    global valid_links, invalid_count

    code_nitro = ''.join([random.choice(string.ascii_uppercase + string.digits) for _ in range(16)])
    url_nitro = f'https://discord.gift/{code_nitro}'
    response = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code_nitro}?with_application=false&with_subscription_plan=true', timeout=1)
    
    lock.acquire()  
    try:
        if response.status_code == 200:
            embed_content = {
                'title': f'Nitro Valid !',
                'description': f"**__Nitro:__**\n```{url_nitro}```",
                'color': color_webhook,
                'footer': {
                    "text": username_webhook,
                    "icon_url": avatar_webhook,
                }
            }
            if webhook in ['y', 'Y', 'Yes', 'yes', 'YES']:
                send_webhook(embed_content, webhook_url, username_webhook, avatar_webhook)
            valid_links.append(url_nitro)
            print(f"{color.GREEN}[{color.WHITE}{current_time_hour()}{color.GREEN}] Status:  {color.WHITE}Valid{color.GREEN}  | Nitro: {color.WHITE}{url_nitro}{color.RESET}")
        else:
            invalid_count += 1
            print(f"{color.RED}[{color.WHITE}{current_time_hour()}{color.RED}] Valide ou invalide: {color.WHITE}Invalid{color.RED} | Nitro: {color.WHITE}{url_nitro}{color.RESET}")
    finally:
        lock.release()  

def request(threads_number, webhook, webhook_url, color_webhook, username_webhook, avatar_webhook):
    """Lance les threads pour vérifier les codes Nitro."""
    threads = []
    
    for _ in range(threads_number):
        t = threading.Thread(target=nitro_check, args=(webhook, webhook_url, color_webhook, username_webhook, avatar_webhook))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

def CheckWebhook(webhook_url):
    """Vérifie si le webhook est valide en envoyant un message de test."""
    print(f"{color.RED}\nVérification du webhook...{color.RESET}")
    
    embed_content = {
        'title': 'NITRO GEN BY https://github.com/akadebian',
        'description': 'Test de webhook',
        'color': 16711680,  
        'footer': {
            "text": "Akadebian",
            "icon_url": "https://img.freepik.com/photos-premium/dessin-demon-noir-aux-yeux-rouges_839169-24240.jpg",
        }
    }

    response_code = send_webhook(embed_content, webhook_url, "NitroGen", "https://img.freepik.com/photos-premium/dessin-demon-noir-aux-yeux-rouges_839169-24240.jpg")
    
    if response_code == 204:  
        print(f"{color.GREEN}[+] Webhook valide{color.RESET}")
    else:
        print(f"{color.RED}[-] Webhook invalide{color.RESET}")
        exit(1)

def send_final_report(webhook_url, valid_links, invalid_count, username_webhook, avatar_webhook):
    """Envoie un rapport final au webhook avec les résultats des vérifications."""
    valid_count = len(valid_links)
    valid_links_str = "\n".join(valid_links) if valid_links else "Aucun"

    embed_content = {
        'title': 'Rapport final - Nitro Gen',
        'description': f"**Liens valides :** {valid_count}\n**Liens invalides :** {invalid_count}\n\n**Codes valides :**\n{valid_links_str}",
        'color': 65280,  
        'footer': {
            "text": username_webhook,
            "icon_url": avatar_webhook,
        }
    }

    send_webhook(embed_content, webhook_url, username_webhook, avatar_webhook)

def run():
    """Fonction principale du générateur de Nitro."""
    global valid_links, invalid_count
    
    try:
        webhook = input(f"{color.RED}\nWebhook ? (y/n) -> {color.RESET}")
        if webhook in ['y', 'Y', 'Yes', 'yes', 'YES']:
            webhook_url = input(f"{color.RED}Webhook URL -> {color.RESET}")
            CheckWebhook(webhook_url)
        else:
            webhook_url = None

        try:
            threads_number = int(input(f"{color.WHITE}Nombre de codes Nitro à générer -> {color.RESET}"))
        except ValueError:
            print(f"{color.RED}Erreur: Veuillez entrer un nombre valide.{color.RESET}")
            return

      
        color_webhook = 16711680  
        username_webhook = "Nitro gen by akadebian / roner tools"
        avatar_webhook = "https://img.freepik.com/photos-premium/dessin-demon-noir-aux-yeux-rouges_839169-24240.jpg"

        request(threads_number, webhook, webhook_url, color_webhook, username_webhook, avatar_webhook)
        
        if webhook in ['y', 'Y', 'Yes', 'yes', 'YES']:
            send_final_report(webhook_url, valid_links, invalid_count, username_webhook, avatar_webhook)
    except Exception as e:
        print(f"{color.RED}Erreur: {str(e)}{color.RESET}")

if __name__ == "__main__":
    run()
