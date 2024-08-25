# par pitié ne pas volé mon code et ne rien modiffié svp sah
import subprocess
import sys

def ping_ip(ip_address, count=100):
    """Pinger une adresse IP rapidement un nombre spécifique de fois et afficher les résultats en direct."""
    print(f"Pinging {ip_address} {count} times:")


    command = ['ping', '-c', str(count), '-i', '0.2', ip_address] if sys.platform != 'win32' else ['ping', '-n', str(count), '-w', '200', ip_address]

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)


        for line in process.stdout:
            print(line.strip())
        
        process.wait()  

    except Exception as e:
        print(f"Erreur lors du ping de l'adresse {ip_address}: {str(e)}")

def run():
    """Fonction principale pour exécuter le ping rapide."""
    ip_address = input("Veuillez entrer une adresse IP à pinger: ")
    ping_ip(ip_address)
