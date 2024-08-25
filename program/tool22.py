# par pitié ne pas volé mon code et ne rien modiffié svp sah
import requests
import random
import string
import json
import threading


class color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    WHITE = '\033[97m'
    RESET = '\033[0m'


def current_time_hour():
    from datetime import datetime
    return datetime.now().strftime('%H:%M:%S')


def Error(message):
    print(f"{color.RED}Erreur: {message}{color.RESET}")


def send_webhook(embed_content, webhook_url):
    payload = {
        'embeds': [embed_content]
    }

    headers = {
        'Content-Type': 'application/json'
    }

    requests.post(webhook_url, data=json.dumps(payload), headers=headers)


def webhook_check(check_webhook_url, use_webhook, webhook_url):
    first = ''.join([str(random.randint(0, 9)) for _ in range(19)])
    second = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([68])))
    webhook_test_code = f"{first}/{second}"
    webhook_test_url = f"https://discord.com/api/webhooks/{webhook_test_code}"

    try:
        response = requests.head(webhook_test_url)
        if response.status_code == 200:
            result = f"{color.GREEN}[{color.WHITE}{current_time_hour()}{color.GREEN}] Statut: {color.WHITE}Valide{color.GREEN} | Webhook: {color.WHITE}{webhook_test_code}{color.GREEN}"
            if use_webhook:
                embed_content = {
                    'title': 'Webhook Valide !',
                    'description': f"**__Webhook:__**\n```{webhook_test_url}```",
                    'color': 3066993  
                }
                send_webhook(embed_content, webhook_url)
            print(result)
        else:
            print(f"{color.RED}[{color.WHITE}{current_time_hour()}{color.RED}] {color.WHITE}Invalide{color.RED} | Webhook: {color.WHITE}{webhook_test_code}{color.RED}")
    except Exception as e:
        print(f"{color.RED}[{color.WHITE}{current_time_hour()}{color.RED}] {color.WHITE}Erreur{color.RED} | Webhook: {color.WHITE}{webhook_test_code}{color.RED}")


def request(threads_number, use_webhook, webhook_url):
    threads = []
    try:
        for _ in range(int(threads_number)):
            t = threading.Thread(target=webhook_check, args=(webhook_url, use_webhook, webhook_url))
            t.start()
            threads.append(t)
    except Exception as e:
        Error(f"Erreur lors de la création des threads: {e}")

    for thread in threads:
        thread.join()


def run():
    use_webhook = input(f"{color.RED}\nSouhaitez-vous utiliser un webhook pour recevoir les résultats ? (y/n) -> {color.RESET}")
    webhook_url = None
    if use_webhook.lower() in ['y', 'yes']:
        webhook_url = input(f"{color.RED}URL du Webhook pour recevoir les résultats -> {color.RESET}")

    try:
        threads_number = int(input(f"{color.RED}Nombre de threads -> {color.RESET}"))
    except ValueError:
        Error("Nombre invalide. Veuillez entrer un nombre entier.")
        return

    while True:
        request(threads_number, use_webhook.lower() in ['y', 'yes'], webhook_url)

if __name__ == "__main__":
    run()
