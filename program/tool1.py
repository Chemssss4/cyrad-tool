# par pitié ne pas volé mon code et ne rien modiffié svp sah
import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from colorama import init, Fore


init(autoreset=True)

def run():
    print("Exécution de l'outil 2...")


    url = input(Fore.MAGENTA + "Entrez l'URL du site web : ")


    if not urlparse(url).scheme:
        url = "http://" + url


    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
    except requests.RequestException as e:
        print(Fore.RED + f"Erreur lors de la récupération de la page : {str(e)}")
        return


    title = soup.title.string if soup.title else "site"
    title = sanitize_title(title)


    output_dir = os.path.join("output", title)
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    except PermissionError:
        print(Fore.RED + "Erreur : Accès refusé lors de la création du dossier.")
        print(Fore.YELLOW + "Suggestion : Essayez d'ouvrir ce script dans Visual Studio Code et réessayez.")
        return


    html_filename = os.path.join(output_dir, "index.html")
    try:
        with open(html_filename, 'w', encoding='utf-8') as html_file:
            html_file.write(str(soup))
            print(Fore.GREEN + f"Fichier HTML principal enregistré : {html_filename}")
    except PermissionError:
        print(Fore.RED + f"Erreur : Accès refusé lors de l'enregistrement du fichier HTML.")
        print(Fore.YELLOW + "Suggestion : Essayez d'ouvrir ce script dans Visual Studio Code et réessayez.")
        return
    except Exception as e:
        print(Fore.RED + f"Erreur inattendue lors de l'enregistrement du fichier HTML : {str(e)}")
        return


    css_links = soup.find_all('link', rel='stylesheet')
    for link in css_links:
        css_href = link.get('href')
        if css_href:
            css_url = urljoin(url, css_href)
            css_content = download_file(css_url, "CSS")
            if css_content:
                css_filename = os.path.join(output_dir, sanitize_filename(os.path.basename(css_href)))
                try:
                    with open(css_filename, 'w', encoding='utf-8') as css_file:
                        css_file.write(css_content)
                        print(Fore.GREEN + f"Fichier CSS trouvé et sauvegardé : {css_filename}")
                except PermissionError:
                    print(Fore.RED + f"Erreur : Accès refusé lors de l'enregistrement du fichier CSS : {css_filename}.")
                    print(Fore.YELLOW + "Suggestion : Essayez d'ouvrir ce script dans Visual Studio Code et réessayez.")


    js_links = soup.find_all('script')
    for script in js_links:
        js_src = script.get('src')
        if js_src:
            js_url = urljoin(url, js_src)
            js_content = download_file(js_url, "JS")
            if js_content:
                js_filename = os.path.join(output_dir, sanitize_filename(os.path.basename(js_src)))
                try:
                    with open(js_filename, 'w', encoding='utf-8') as js_file:
                        js_file.write(js_content)
                        print(Fore.GREEN + f"Fichier JS trouvé et sauvegardé : {js_filename}")
                except PermissionError:
                    print(Fore.RED + f"Erreur : Accès refusé lors de l'enregistrement du fichier JS : {js_filename}.")
                    print(Fore.YELLOW + "Suggestion : Essayez d'ouvrir ce script dans Visual Studio Code et réessayez.")

    img_tags = soup.find_all('img')
    for img in img_tags:
        img_src = img.get('src')
        if img_src:
            img_url = urljoin(url, img_src)
            img_content = download_file(img_url, "Image")
            if img_content:
                img_filename = os.path.join(output_dir, sanitize_filename(os.path.basename(img_src)))
                try:
                    with open(img_filename, 'wb') as img_file:
                        img_file.write(img_content)
                        print(Fore.GREEN + f"Image trouvée et sauvegardée : {img_filename}")
                except PermissionError:
                    print(Fore.RED + f"Erreur : Accès refusé lors de l'enregistrement de l'image : {img_filename}.")
                    print(Fore.YELLOW + "Suggestion : Essayez d'ouvrir ce script dans Visual Studio Code et réessayez.")

def sanitize_title(title):
    """
    Nettoie le titre du site pour qu'il soit compatible avec les noms de dossiers.
    """

    title = re.sub(r'[<>:"/\\|?*]', '_', title)

    title = re.sub(r'[^\x20-\x7E]', '', title)

    title = title.strip()
    return title

def sanitize_filename(filename):
    """
    Nettoie le nom du fichier pour qu'il soit compatible avec le système de fichiers.
    """
   
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)

    filename = re.sub(r'[^\x20-\x7E]', '', filename)
    return filename

def download_file(file_url, file_type):
    try:
        response = requests.get(file_url)
        response.raise_for_status()
        if file_type == "Image":
            return response.content 
        return response.text
    except requests.RequestException as e:
        print(Fore.RED + f"Erreur lors du téléchargement de {file_type} : {file_url} - {str(e)}")
        return None
