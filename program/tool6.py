# par pitié ne pas volé mon code et ne rien modiffié svp sah
import socket
import threading
from datetime import datetime
from colorama import init
from colorsys import hsv_to_rgb
import queue


init(autoreset=True)


def get_rgb_color(hue):
    rgb = hsv_to_rgb(hue, 1.0, 1.0)
    return tuple(int(255 * x) for x in rgb)


def get_color_code(rgb):
    return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"

def get_color_gradient(text, start_color=(0.0, 1.0, 1.0), end_color=(0.6, 1.0, 1.0)):
    """Applique un dégradé de couleurs sur un texte."""
    gradient_text = ""
    length = len(text)

    for i, char in enumerate(text):

        ratio = i / length
        hue = start_color[0] + ratio * (end_color[0] - start_color[0])
        rgb = get_rgb_color(hue)
        color_code = get_color_code(rgb)
        gradient_text += f"{color_code}{char}"

    return gradient_text

def scan_port(ip, port, result_queue):
    """Scanne un port spécifique sur une IP et place le résultat dans une queue."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.1)  
        result = sock.connect_ex((ip, port))
        current_time = datetime.now().strftime("%H:%M:%S")
        if result == 0:
 
            status = get_color_gradient(f"[{current_time} Europe] IP: {ip} / Port: {port} is OPEN", start_color=(0.0, 1.0, 1.0), end_color=(0.3, 1.0, 1.0))
        else:
    
            status = get_color_gradient(f"[{current_time} Europe] IP: {ip} / Port: {port} is CLOSED", start_color=(0.6, 1.0, 1.0), end_color=(0.9, 1.0, 1.0))
        result_queue.put(status)

def scan_ports(ip):
    """Scanne les ports spécifiés sur une IP et affiche les résultats en direct."""
    print(get_color_gradient(f"Scanning ports on IP: {ip}...\n"))

    num_threads = 50  
    result_queue = queue.Queue()
    threads = []


    for port in range(1, 1025):
        if len(threads) >= num_threads:

            for thread in threads:
                thread.join()
            threads = []
        
        thread = threading.Thread(target=scan_port, args=(ip, port, result_queue))
        thread.start()
        threads.append(thread)


    for thread in threads:
        thread.join()


    while not result_queue.empty():
        print(result_queue.get())

def run():
    """Fonction principale pour exécuter le scan de ports."""
    ip = input("Veuillez entrer l'adresse IP à scanner: ")
    try:

        socket.inet_aton(ip)
    except socket.error:
        print(get_color_gradient(f"Erreur: Adresse IP non valide {ip}.", start_color=(0.0, 1.0, 1.0), end_color=(0.1, 1.0, 1.0)))
        return
    
    scan_ports(ip)

if __name__ == "__main__":
    run()
