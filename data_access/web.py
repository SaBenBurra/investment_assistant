import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_page_source_with_selenium(
    url,
    chrome_driver_path=None,
    user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
):
    start_time = time.time()

    options = Options()

    options.add_argument("user-agent=" + user_agent)
    options.add_argument("--headless")
    options.add_argument("--disable-extensions")
    options.add_argument("--enable-javascript")
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

    if chrome_driver_path is not None:
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=options)

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)

    driver.get(url)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body :last-child")))
    driver.execute_script("window.stop();")

    print("Scraped successfully. Elapsed time " + str(time.time() - start_time))
    return driver.page_source


def get_page_source_with_requests(url):
    return requests.get(url).text
