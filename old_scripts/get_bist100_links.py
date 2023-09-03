from selenium import webdriver
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

start_time = time.time()

# url = "https://www.investing.com/indices/ise-100-components"
url = "https://www.investing.com/equities/yazicilar-holding-ratios"
query = "body :last-child"  # xpath query
options = Options()

options.add_argument("--headless")
options.add_argument("--disable-extensions")
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
)
options.add_argument("--enable-javascript")
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
wait = WebDriverWait(driver, 20)

driver.get(url)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, query)))
driver.execute_script("window.stop();")

soup = BeautifulSoup(driver.page_source, "html.parser")
rows = (
    soup.find("table", class_="genTbl closedTbl crossRatesTbl elpTbl elp25")
    .find("tbody")
    .findAll("tr")
)
bist100links = []
for row in rows:
    bist100links.append(row.findAll("td")[1].find("a")["href"])

all_data_file = open("datas/all_data.json", "r")

all_data = json.load(all_data_file)

bist100data = []

for link in bist100links:
    for data in all_data:
        if data["link"].rstrip("\n") == link:
            bist100data.append({"symbol": data["symbol"], "link": link})

bist100data_file = open("bist100_data.json", "w")

json.dump(bist100data, bist100data_file, indent=4)
