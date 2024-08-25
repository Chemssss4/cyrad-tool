# par pitié ne pas volé mon code et ne rien modiffié svp sah
import requests
from colorama import Fore, Style, init


init(autoreset=True)

BRIGHT_GREEN = "\033[38;2;0;255;0m"
BRIGHT_BLUE = "\033[38;2;0;191;255m"
BRIGHT_YELLOW = "\033[38;2;255;255;0m"
BRIGHT_RED = "\033[38;2;255;69;0m"
BRIGHT_CYAN = "\033[38;2;0;255;255m"
BRIGHT_MAGENTA = "\033[38;2;255;0;255m"
BORDER_CHAR = "✦"  

def run():

    ip_address = input(f"{BRIGHT_CYAN}Entrez l'adresse IP (ex: 8.8.8.8) : ")

    try:

        response = requests.get(f"https://ipinfo.io/{ip_address}/json")


        if response.status_code == 200:
            data = response.json()


            ip = data.get("ip", "N/A")
            hostname = data.get("hostname", "N/A")
            city = data.get("city", "N/A")
            region = data.get("region", "N/A")
            country = data.get("country", "N/A")
            location = data.get("loc", "N/A")
            org = data.get("org", "N/A")
            postal = data.get("postal", "N/A")
            timezone = data.get("timezone", "N/A")


            print(f"\n{BRIGHT_MAGENTA}{BORDER_CHAR * 40}")
            print(f"{BRIGHT_BLUE}[+] IP Address    {BRIGHT_MAGENTA} » {BRIGHT_CYAN}{ip}")
            print(f"{BRIGHT_BLUE}[+] Hostname      {BRIGHT_MAGENTA} » {BRIGHT_YELLOW}{hostname}")
            print(f"{BRIGHT_BLUE}[+] City          {BRIGHT_MAGENTA} » {BRIGHT_GREEN}{city}")
            print(f"{BRIGHT_BLUE}[+] Region        {BRIGHT_MAGENTA} » {BRIGHT_GREEN}{region}")
            print(f"{BRIGHT_BLUE}[+] Country       {BRIGHT_MAGENTA} » {BRIGHT_GREEN}{country}")
            print(f"{BRIGHT_BLUE}[+] Location      {BRIGHT_MAGENTA} » {BRIGHT_YELLOW}{location}")
            print(f"{BRIGHT_BLUE}[+] Organization  {BRIGHT_MAGENTA} » {BRIGHT_CYAN}{org}")
            print(f"{BRIGHT_BLUE}[+] Postal Code   {BRIGHT_MAGENTA} » {BRIGHT_GREEN}{postal}")
            print(f"{BRIGHT_BLUE}[+] Timezone      {BRIGHT_MAGENTA} » {BRIGHT_YELLOW}{timezone}")
            print(f"{BRIGHT_MAGENTA}{BORDER_CHAR * 40}\n")
        else:
            print(f"{BRIGHT_RED}Erreur : Impossible de récupérer les informations pour l'adresse IP donnée.")

    except requests.exceptions.RequestException as e:
        print(f"{BRIGHT_RED}Erreur lors de la requête : {e}")

if __name__ == "__main__":
    run()
