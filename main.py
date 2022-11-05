import pickle
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)

print("Enter 1 to run 'save cookie' algorithm")
print("Enter 2 to run 'load cookie' algorithm")
try:
    qwe = int(input())
except Exception as e:
    print(e)
    print('Wrong input try again')
    sys.exit()
if qwe == 1:
    options = webdriver.ChromeOptions()
    service = Service('C:/Program Files/ChromeDriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://trucks.ati.su/?FromGeo=0_1&fromCountryId=1&ExactFromGeos=true')
    print("Do authorisation on website, then enter something in console.")
    foo = input()
    save_cookie(driver, 'cookie.pkl')
    print('Cookies saved successfully, webdriver is quiting.')
    driver.quit()
    sys.exit()
elif qwe == 2:
    options = webdriver.ChromeOptions()
    service = Service('C:/Program Files/ChromeDriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://trucks.ati.su/?FromGeo=0_1&fromCountryId=1&ExactFromGeos=true')
    load_cookie(driver, 'cookie.pkl')
    driver.get('https://trucks.ati.su/?FromGeo=0_1&fromCountryId=1&ExactFromGeos=true')
    input()
    print('Webdriver is quiting.')
    driver.quit()
    sys.exit()
else:
    print('Wrong input, try again')
    sys.exit()