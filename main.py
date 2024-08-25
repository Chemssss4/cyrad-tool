
# par pitié ne pas volé mon code et ne rien modiffié svp sah
# Merci a ceux qui me soutiennent malgrès les nombreux rageux



import os
import importlib
import sys
import time
import ctypes
import asyncio
import shutil
import requests
from colorama import init, Fore



init(autoreset=True)






def Slow(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  
        time.sleep(delay)  


YELLOW_LIGHT = '\033[93m'  
YELLOW_DARK = '\033[33m'  
RED_DARK_BRIGHT = '\033[38;5;196m'
ORANGE = '\033[38;5;208m'
ORANGE_FONCE = '\033[38;5;166m'
GRAY_LIGHT = '\033[48;5;238m'


THEMES = {
    '1': (Fore.BLUE, Fore.CYAN),
    '2': (YELLOW_LIGHT, YELLOW_DARK), 
    '3': (ORANGE_FONCE, ORANGE), 
    '4': (Fore.WHITE, RED_DARK_BRIGHT),
    '5': (Fore.LIGHTWHITE_EX, Fore.LIGHTBLACK_EX),  
    '6': (Fore.YELLOW, Fore.GREEN),  
    '7': (Fore.GREEN, Fore.LIGHTYELLOW_EX)  
}


current_theme = '1'

def get_theme_colors(theme_id):
    return THEMES.get(theme_id, THEMES['1'])

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_full_screen_windows():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 3)

def set_full_screen_linux():
    os.system('xdotool key F11')  

def set_full_screen_macos():

    os.system('osascript -e \'tell application "Terminal" to set bounds of front window to {0, 0, 1440, 900}\'')

def set_full_screen():
    if os.name == 'nt': 
        set_full_screen_windows()
    elif sys.platform == 'linux':  
        set_full_screen_linux()
    elif sys.platform == 'darwin': 
        set_full_screen_macos()

def adjust_menu(menu_str):
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    
    adjusted_lines = []
    for line in menu_str.splitlines():
        while len(line) > width:
            break_point = width - 1
            if line[break_point] == ' ':
                adjusted_lines.append(line[:break_point])
                line = line[break_point:].lstrip()
            else:
                adjusted_lines.append(line[:width])
                line = line[width:].lstrip()
        adjusted_lines.append(line)
    
    return '\n'.join(adjusted_lines)

def afficher_menu(theme_colors):
    clear_screen()



    main_color, accent_color = theme_colors

  
    ascii_art = f"""
{main_color}                                                                                  
                                                                                  
                                                                                 
{accent_color}                                                                                 
      ░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░  ░▒▓██████▓▒░ ░▒▓███████▓▒░        ░▒▓██████▓▒░ ░▒▓████████▓▒░░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░       ░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░        ░▒▓██████▓▒░ ░▒▓███████▓▒░ ░▒▓████████▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒▒▓███▓▒░░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░          ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░   ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░    ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░        ░▒▓██████▓▒░ ░▒▓████████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                                                       

                                                                                  
{main_color}                                                                                
"""

    
    start_time = time.time()
    while time.time() - start_time < 1:
        clear_screen()
        print("\n" * 10) 
        print(ascii_art.center(shutil.get_terminal_size().columns))
        time.sleep(0.5)
        clear_screen()
        time.sleep(0.5)

    menu = """
{1}  

  /$$$$$$                                     /$$
 /$$__  $$                                   | $$
| $$  \__/ /$$   /$$  /$$$$$$  /$$$$$$   /$$$$$$$        /$$$$$$   /$$$$$$  /$$$$$$$ 
| $$      | $$  | $$ /$$__  $$|____  $$ /$$__  $$       /$$__  $$ /$$__  $$| $$__  $$
| $$      | $$  | $$| $$  \__/ /$$$$$$$| $$  | $$      | $$  \ $$| $$$$$$$$| $$  \ $$
| $$    $$| $$  | $$| $$      /$$__  $$| $$  | $$      | $$  | $$| $$_____/| $$  | $$
|  $$$$$$/|  $$$$$$$| $$     |  $$$$$$$|  $$$$$$$      |  $$$$$$$|  $$$$$$$| $$  | $$
 \______/  \____  $$|__/      \_______/ \_______/       \____  $$ \_______/|__/  |__/
           /$$  | $$                                    /$$  \ $$
          |  $$$$$$/                                   |  $$$$$$/
           \______/                                     \______/
                                                                                                            ║ ║
                                                                                                           ║ ║
                                             DEV : nerox                                          Version : v1.0                                      ════════╝
{0}
{0}</{1}Menu{0}>{1}                                    {0}[{1}t = themes{0}]{1} {0}[{1}i = infos{0}]  {1}                                                                                                                                        
{0}[{1}01{0}]{1} ->  {0}Copier un site               {0}[{1}11{0}]{1} ->  {0}Lookup number phone               {0}[{1}21{0}]{1} ->  {0}Spam create groupe
{0}[{1}02{0}]{1} ->  {0}Raid bot discord             {0}[{1}12{0}]{1} ->  {0}Lookup ip                         {0}[{1}22{0}]{1} ->  {0}Generateur Webhook
{0}[{1}03{0}]{1} ->  {0}Discord id to token          {0}[{1}13{0}]{1} ->  {0}Username tracker                  {0}[{1}23{0}]{1} ->  {0}Token to login
{0}[{1}04{0}]{1} ->  {0}Search db                    {0}[{1}14{0}]{1} ->  {0}Ddos ip                           {0}[{1}24{0}]{1} ->  {0}Status changer en boucle
{0}[{1}05{0}]{1} ->  {0}Ip speed pinger              {0}[{1}15{0}]{1} ->  {0}Infos ce pc                       {0}[{1}25{0}]{1} ->  {0}Account nuker
{0}[{1}06{0}]{1} ->  {0}Ip port scanner              {0}[{1}16{0}]{1} ->  {0}Clear dms (Soon)                  {0}[{1}26{0}]{1} ->
{0}[{1}07{0}]{1} ->  {0}Nitro gen                    {0}[{1}17{0}]{1} ->  {0}Server infos                      {0}[{1}27{0}]{1} ->
{0}[{1}08{0}]{1} ->  {0}Webhook spammer              {0}[{1}18{0}]{1} ->  {0}MassDm token                      {0}[{1}28{0}]{1} ->
{0}[{1}09{0}]{1} ->  {0}Webhook infos                {0}[{1}19{0}]{1} ->  {0}Token Infos                       {0}[{1}29{0}]{1} ->
{0}[{1}10{0}]{1} ->  {0}Webhook delete               {0}[{1}20{0}]{1} ->  {0}Discord mass report               {0}[{1}30{0}]{1} ->
                                                                  
""".format(*theme_colors)

    lines = menu.splitlines()
    total_lines = len(lines)
    duration = 0.01 
    delay = duration / total_lines  

    for i in range(total_lines):
        clear_screen()
        print('\n'.join(lines[:i+10]))
        time.sleep(delay) 

def executer_outil(numero):
    try:
        module_name = f"program.tool{numero}"
        module = importlib.import_module(module_name)

        if asyncio.iscoroutinefunction(module.run):
            asyncio.run(module.run())
        else:
            module.run()
    except ModuleNotFoundError:
        print(f"Outil {numero} n'est pas disponible.")
    except Exception as e:
        print(f"Erreur lors de l'exécution de l'outil {numero}: {str(e)}")

def choisir_theme():
    clear_screen()
    print(f"""
{Fore.WHITE}
                            ████████████           ████
                     █████▒░░░░░░░░░░░░▒██        ██▓▓██
                  █▓▒▒░░░░░░░░░░░░░░░░░░▓██     ███▓▒▒▒▓██           {Fore.WHITE}Themes disponible:{Fore.WHITE}
               ███░░░░░░░░░░░░░░░░░░░▒███    ████▓▓▒▒▒▒▒▒███
             ██▓░░░▓█████▒░░░░░░░░▒███      ██▓▓▓▓▒▒▒▒▒▒▒▒███        {Fore.CYAN}1. DEFAULT {Fore.WHITE}
           ███░░░▓█{Fore.BLUE}▒░░░░░{Fore.WHITE}▓█▒░░░░░▓██       ██▓▓▓▓▓▒▒▒▒▒▒▒▒▓██       {YELLOW_LIGHT} 2. CHEESE{Fore.WHITE}
          ██▓░░░░██{Fore.BLUE}░░░░░░▒{Fore.WHITE}█▓░░░░▒██        ██▓▓▓▓▓▒▒▒▒▒▒▒▒▓██     {ORANGE}   3. HALLOWEEN{Fore.WHITE}
         ██▒░░░░░░▓█▓▒▒▒▓█▓░░░░░░▓██        ███▓▓▓▒▒▒▒▒▒▒▓██      {RED_DARK_BRIGHT}   4. RED-BRILLANT{Fore.WHITE}
         █▓░░░░░░░░░░░░░░░░░░░░░░░▒▓██████  ███████████████       {Fore.LIGHTWHITE_EX}   5. OLD{Fore.WHITE}
        ██▒░░░░▒█████▓░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒░████▓▓▓▓██▓██       {Fore.GREEN}  6. TOXIC{Fore.WHITE}
        ██▒░░▒█▓{Fore.RED}▒▒▒▒▒▒{Fore.WHITE}█▓░░░░░░░░░░░░░░░░░░░░░░░▓███▓▓▓▓██▒▒██      {Fore.LIGHTYELLOW_EX}  7. TROPICAL{Fore.WHITE}
        ██▒░░▒█▓{Fore.RED}▒▒▒▒▒▒{Fore.WHITE}██░░░░░░░░░░░░░░░░░░░░░░▒████▓▓▓▓██░▒██
         █▓░░░▒██▓▓▓██▓░░░░░░░░░░░░░░░░░░░░░▓████▓▓▒▒▒▒██░▓█
         ██▒░░░░░░░░░░░▒▓▓█▓▒░░░░░░░░░░░░░░░▓████▓▒░░░▒█▓▓██         
          ██▒░░░░░░░░▓█▓{Fore.YELLOW}▒▒▒▒{Fore.WHITE}▓█▓░░░░░░▓▓▓░░░░░▒▓██▓▒░░░▒████
           ██▓░░░░░░▒█▓{Fore.YELLOW}▒▒▒▒▒{Fore.WHITE}▒▓█▒░░▓█▓{Fore.CYAN}▒▒▒{Fore.WHITE}▓██░░░░░▓█▒░░░▓███
             ██▓░░░░░▒██{Fore.YELLOW}▓▒▒▒{Fore.WHITE}▓█▓░░▓█{Fore.CYAN}▒▒▒▒▒▒▒{Fore.WHITE}█▓░░░░▓█▒▒░░▓█
               ███░░░░░░████░░░░░▒█▓{Fore.CYAN}▒▒▒▒▒{Fore.WHITE}█▒░░░░░▒█▒▒░▒██
                 ████▒░░░░░░░░░░░░░░▓███▓░░░░░░▒██▓▒░▒██
                     ████▓▒░░░░░░░░░░░░░░░▒▓██████▓▒░▒██
                           ███████████████       ███████


    """)

    choix = input("Choisissez un thème (1-7) : ").strip()
    global current_theme
    if choix in THEMES:
        current_theme = choix
        print("Thème sélectionné avec succès !")
        clear_screen()
        afficher_menu(get_theme_colors(current_theme))
    else:
        print("Choix invalide, retour au menu principal.")

def main():
    global current_theme
    afficher_menu(get_theme_colors(current_theme))  
    while True:
        choix = input(get_theme_colors(current_theme)[1] + "┌──(user@roner)-[~/Menu]\n│\n└─$")

        if choix == '0':
            print("Au revoir !")
            sys.exit(0)
        elif choix == 't':
            choisir_theme()
        elif choix in ['i', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16','17','18','19','20','21','22','23','24','25']:
            executer_outil(choix)
        else:
            print("Option non valide, veuillez réessayer.")
            clear_screen()
            afficher_menu(get_theme_colors(current_theme)) 

if __name__ == "__main__":
    main()
