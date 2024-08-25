# par pitié ne pas volé mon code et ne rien modiffié svp sah
import os
import platform
import psutil
import socket
from datetime import datetime
from colorama import init, Fore

# Initialiser colorama
init(autoreset=True)
ROUGE = Fore.RED
RESET = Fore.RESET

def obtenir_infos_systeme():
    """Recueille et retourne les informations du système."""
    infos = {}
    

    infos['Système d\'exploitation'] = platform.system()
    infos['Version OS'] = platform.version()
    infos['Architecture'] = platform.architecture()[0]
    infos['Nom de la machine'] = platform.node()
    infos['Nom du processeur'] = platform.processor()
    infos['Date et heure'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    

    infos['Cœurs logiques'] = psutil.cpu_count(logical=True)
    infos['Cœurs physiques'] = psutil.cpu_count(logical=False)
    infos['Fréquence CPU'] = f"{psutil.cpu_freq().current} MHz"
    

    mem = psutil.virtual_memory()
    infos['Mémoire RAM totale'] = f"{mem.total / (1024 ** 3):.2f} Go"
    infos['Mémoire RAM disponible'] = f"{mem.available / (1024 ** 3):.2f} Go"
    infos['Mémoire RAM utilisée'] = f"{mem.used / (1024 ** 3):.2f} Go"
    

    disque = psutil.disk_usage('/')
    infos['Espace disque total'] = f"{disque.total / (1024 ** 3):.2f} Go"
    infos['Espace disque utilisé'] = f"{disque.used / (1024 ** 3):.2f} Go"
    infos['Espace disque libre'] = f"{disque.free / (1024 ** 3):.2f} Go"
    

    infos['Adresse IP locale'] = socket.gethostbyname(socket.gethostname())
    
    return infos

def afficher_infos(infos):
    """Affiche les informations recueillies."""
    print(f"{ROUGE}=== Informations sur le système ==={RESET}")
    for cle, valeur in infos.items():
        print(f"{ROUGE}{cle} : {RESET}{valeur}")

def principal():
    """Fonction principale pour afficher les informations du PC."""

    infos_systeme = obtenir_infos_systeme()
    afficher_infos(infos_systeme)

def run():
    """Point d'entrée pour l'exécution du module."""
    principal()

if __name__ == "__main__":
    run()
