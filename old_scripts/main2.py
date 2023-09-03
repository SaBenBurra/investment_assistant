from bs4 import BeautifulSoup
from lxml import etree
from scrape import get_page_source
import json

base_url = "https://www.investing.com"

with open("./datas/bist100_data.json", "r") as file:
    bist100data = json.load(file)

codes = []
i = 0
for data in bist100data:
    i = i + 1
    found = False
    url = base_url + data["link"] + "-ratios"
    try:
        source = get_page_source(url, chrome_driver_path="./chromedriver", log=False)
    except KeyboardInterrupt:
        exit()
    except:
        print("ERROR: " + data["symbol"])

    soup = BeautifulSoup(source, "html.parser")
    dom = etree.HTML(str(soup))
    fk = dom.xpath('//*[@id="childTr"]/td/div/table/tbody/tr[1]/td[2]')[0].text
    enfk = dom.xpath(
        "/html/body/div[6]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[3]"
    )[0].text
    price = dom.xpath('//*[@id="last_last"]')[0].text
    try:
        if float(fk) < float(enfk) / 2 and float(price) < 100:
            main_source = get_page_source(
                base_url + data["link"], chrome_driver_path="./chromedriver", log=False
            )
            soup = BeautifulSoup(main_source, "html.parser")

            industry = (
                soup.find(
                    "div",
                    class_="flex justify-between border-b border-t md:border-t-0 border-[#E6E9EB] pt-2 md:pt-0 pb-2",
                )
                .find("a")
                .text
            )
            stock_log = (
                data["symbol"]
                + " industry: "
                + industry
                + "  price: "
                + price
                + "  fk: "
                + fk
                + "  enfk: "
                + enfk
            )
            file = open("cheap_stocks.txt", "a")
            file.write(stock_log + "\n")
            file.close()
            found = True
    except:
        pass
    if found:
        print(str(i) + "/100 Found!")
        continue
    print(str(i) + "/100")
