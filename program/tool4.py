# par pitié ne pas volé mon code et ne rien modiffié svp sah
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from colorama import Fore, Style, init


init(autoreset=True)


os.environ['WDM_LOG_LEVEL'] = '0'
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option('excludeSwitches', ['enable-logging'])


mot = input("Veuillez entrer un mot pour la recherche : ")


driver = webdriver.Chrome(options=options)

try:

    driver.get("https://bfsearcher.com/searcher/searcher.php/test")


    search_bar = driver.find_element(By.ID, "word")
    search_bar.send_keys(mot)


    search_button = driver.find_element(By.CLASS_NAME, "search-button")
    search_button.click()


    print(Fore.GREEN + Style.BRIGHT + "Recherche en cours..." + Style.RESET_ALL)


    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "body")))


    page_content = driver.find_element(By.TAG_NAME, "body").text


    for line in page_content.splitlines():
        if "Email :" in line or "Password :" in line:
            print(line)

finally:

    driver.quit()
