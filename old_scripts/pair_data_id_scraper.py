import json
from bs4 import BeautifulSoup
from lxml import etree
from scrape import get_page_source

base_url = "https://www.investing.com"
with open("datas/all_data.json", "r") as file:
    all_data = json.load(file)

pair_all_data = []
length = len(all_data)
i = 0
for data in all_data:
    i = i + 1
    url = base_url + data["link"] + "-balance-sheet"
    source = get_page_source(url=url, chrome_driver_path="./chromedriver", log=False)
    soup = BeautifulSoup(source, "html.parser")
    dom = etree.HTML(str(soup))
    pair_id = dom.xpath("/html/body/div[6]/section/div[1]/div[5]")[0].attrib[
        "data-pair-id"
    ]
    data["pair_id"] = pair_id
    pair_all_data.append(data)
    save_file = open("pair_all_data.json", "w")
    json.dump(pair_all_data, save_file)
    save_file.close()
    print(str(i) + "/" + str(length))
