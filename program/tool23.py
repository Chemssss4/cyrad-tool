# par pitié ne pas volé mon code et ne rien modiffié svp sah
import requests
import time
import os
from pystyle import Colors
from selenium import webdriver





def autologintitle():
    print(f"{Colors.red}Auto Login Tool")

def setTitle(title):
    print(f"{Colors.blue}{title}")

def autologin():
    autologintitle()
    
    entertoken = input(f"{Colors.red}Enter the token :")
    
    validityTest = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': entertoken, 'Content-Type': 'application/json'})
    if validityTest.status_code != 200:
        print(f"{Colors.red}\nInvalid token")
        input(f"{Colors.red}Press ENTER to exit")
        return
    
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get('https://discord.com/login')
        
        js = ('function login(token) {'
              'setInterval(() => {'
              'document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);'
              'setTimeout(() => {location.reload();}, 500);}')
        
        time.sleep(3)
        driver.execute_script(js + f'login("{entertoken}")')
        time.sleep(10)
        
        if driver.current_url == 'https://discord.com/login':

            autologintitle()
            print(f"{Colors.red}Connection Failed")
            driver.close()
        else:

            autologintitle()
            print(f"{Colors.green}Connection Established")
        
        input(f"{Colors.red}Press ENTER to exit")
    
    except Exception as e:
        print(f"{Colors.red}A problem occurred: {e}")
        time.sleep(2)


def run():
    autologin()

if __name__ == "__main__":
    run()
