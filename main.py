import string
import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = Options()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36')
options.add_argument('cookie=cf_clearance=wwkL4euFXHwknG.PXi.IMvqBikbUXrF.wgyq6K.m9hM-1636561181-0-250; __cf_bm=cTAm90WogEqGikZtculo6o.XhJbFrV5SitetbP3Z_Uw-1636561181-0-AYIxIK9rKFRTqQs/dp1oW45lLJxzMZrqBg/7O/IwR2U1D2FxZpq7IOnujYim+icNy2Dc2sdxq4Rge6vse7SaXV8=; referrer=https://namemc.com/minecraft-names?time=20211208T213040Z&length_op=eq&length=3&sort=asc')

caps = DesiredCapabilities().CHROME
caps['pageLoadStrategy'] = 'eager'

driver = webdriver.Chrome(options=options, desired_capabilities=caps)

driver.get('https://namemc.com/minecraft-names?sort=asc&length_op=eq&length=3&lang=&searches=0')

for i in range(50):
    three_letter = True

    if not i:
        i += 1
    else:
        i += i + 1

    try:
        name = driver.find_element(By.XPATH, f'/html/body/main/div/div[4]/div/table/tbody/tr[{i}]/td[1]/a').get_attribute('text')
    except:
        continue

    for c in name:
        if c.lower() not in string.ascii_lowercase:
            three_letter = False

    if three_letter:
        filename = '3L.txt'
    else:
        filename = '3C.txt'

    print(name)

    with open(filename, 'a') as f:
        f.write(f'{name}\n')

driver.quit()
