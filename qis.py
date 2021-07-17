from selenium import webdriver
import requests
import time
import sys

DRIVER_PATH = "/usr/lib/chromium-browser/chromedriver"
QIS = "https://qis.hochschule-trier.de/qisserver/rds?state=user&type=0"
USERNAME = "my_username"
PASSWORD = "my_password"
TOKEN = "my_token"

opts = webdriver.ChromeOptions()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")
i = 4
while True:
    try:
        print("open:",i-1, flush=True)
        t = time.localtime()
        current_time = time.strftime("%d.%m | %H:%M", t)
        print(current_time, flush=True)
        print("starting..", flush=True)
        browser = webdriver.Chrome(DRIVER_PATH, options=opts)
        browser.get(QIS)
        login = browser.find_element_by_css_selector("#username").send_keys(USERNAME)
        password = browser.find_element_by_css_selector(
            ".login > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > input:nth-child(1)").send_keys(PASSWORD)
        submit = browser.find_element_by_css_selector(
            ".login > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2) > button:nth-child(1)").click()
        time.sleep(1)
        loginQis = browser.find_element_by_css_selector("#asdf").send_keys(USERNAME)
        passwordQis = browser.find_element_by_css_selector("#fdsa").send_keys(PASSWORD)
        submitQis = browser.find_element_by_css_selector(".submit").click()
        time.sleep(1)
        pruefungsverwaltung = browser.find_element_by_css_selector(".submenuCss > a:nth-child(1)").click()
        infoUberAngemeldetepPruefung = browser.find_element_by_css_selector(".liste > li:nth-child(2) > a:nth-child(1)").click()
        abschluss = browser.find_element_by_css_selector("a.regular:nth-child(2)").click()
        po19 = browser.find_element_by_css_selector(".liste1 > a:nth-child(1)").click()
        time.sleep(3)
        tabellenEintraege = browser.find_element_by_css_selector(".content > table:nth-child(6) > tbody:nth-child(1)").get_property('rows')
        if len(tabellenEintraege) != i:
            print("Da passiert was!", flush=True)
            params = {"chat_id": "704715920", "text": "Da passiert was!"}
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            message = requests.post(url, params=params)
            i -= 1
            continue
        browser.quit()
        if i == 1:
            break 
        print("No grade there yet, going to sleep", flush=True)
        time.sleep(3600)
    except:
        print("There was an error!", flush=True)
        print(sys.exc_info(), flush=True)
        time.sleep(3600)
