import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

start_time = time.time()


def extract_expression(string):
    start_index = string.find("(")
    end_index = string.find(")")

    if start_index != -1 and end_index != -1:
        return string[start_index + 1 : end_index]
    else:
        return ""


URL = "https://www.investing.com/"
query = "/html/body/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h1"


options = Options()

options.add_argument("--disable-extensions")
options.add_argument("--disable-javascript")
options.add_argument("--blink-settings=imagesEnabled=false")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")
options.add_argument("--disable-popup-blocking")
options.page_load_strategy = "none"

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service, options=options)


all_data = []
links_file = open("links.txt", "r")
links = links_file.readlines()
start = False
for link in links:
    if "bastas" in link:
        start = True
    if not start:
        continue
    link = link.rstrip("\n")
    wait = WebDriverWait(driver, 35)

    driver.get(URL + link)
    wait.until(EC.presence_of_element_located((By.XPATH, query)))
    driver.execute_script("window.stop();")
    header = driver.find_element(
        By.XPATH,
        query,
    ).text
    symbol = extract_expression(header)
    data = {"symbol": symbol, "link": link}
    all_data.append(data)
    json_data = json.dumps(all_data)

    # JSON verisini dosyaya yazdır
    with open("all_data.json", "w") as file:
        file.write(json_data)

print("Elapsed Time: " + str(time.time() - start_time))
