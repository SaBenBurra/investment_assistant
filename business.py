from data_access.filesystem import get_stock_data_from_json
from data_access.web import get_page_source_with_requests, get_page_source_with_selenium
from bs4 import BeautifulSoup
from models.stock import Stock
from constants import links, xpaths
from lxml import etree
from helpers import pretty_print, reverse_date
from cui import print_stock


def get_stock_data(stock_code):
    json_stock_data = get_stock_data_from_json(stock_code)

    ratios_link = links["base_link"] + json_stock_data["link"] + "-ratios"
    balance_sheet_link = links["balance_sheet_table"].format(json_stock_data["pair_id"])
    income_statement_link = links["income_statement_table"].format(
        json_stock_data["pair_id"]
    )

    ratios_source = get_page_source_with_selenium(url=ratios_link)
    balance_sheet_page_source = get_page_source_with_selenium(url=balance_sheet_link)
    income_statement_page_source = get_page_source_with_selenium(
        url=income_statement_link
    )

    ratios_soup = BeautifulSoup(ratios_source, "html.parser")
    balance_sheet_soup = BeautifulSoup(balance_sheet_page_source, "html.parser")
    income_statement_soup = BeautifulSoup(income_statement_page_source, "html.parser")

    stock = Stock(symbol=json_stock_data["symbol"])

    dom = etree.HTML(str(ratios_soup))
    stock.fk = dom.xpath(xpaths["f/k"])[0].text
    stock.indfk = dom.xpath(xpaths["ind/k"])[0].text

    for balancesheetxpath in xpaths["balance_sheet"]:
        dom = etree.HTML(str(balance_sheet_soup))
        year = dom.xpath(balancesheetxpath["year"])[0].text
        period = dom.xpath(balancesheetxpath["period"])[0].text
        stock.dates.append(period + "/" + year)
        stock.current_assets.append(
            dom.xpath(balancesheetxpath["current_assets"])[0].text.replace(",", ".")
        )
        stock.fixed_assets.append(
            dom.xpath(balancesheetxpath["fixed_assets"])[0].text.replace(",", ".")
        )
        short_term_debts = dom.xpath(balancesheetxpath["short_term_debts"])[
            0
        ].text.replace(",", ".")
        stock.short_term_debts.append(short_term_debts)
        total_debts = dom.xpath(balancesheetxpath["total_debts"])[0].text.replace(
            ",", "."
        )
        stock.long_term_debts.append(float(total_debts) - float(short_term_debts))
        stock.total_debts.append(total_debts)
        stock.total_equities.append(
            dom.xpath(balancesheetxpath["total_equities"])[0].text.replace(",", ".")
        )

    for incomestatementxpath in xpaths["income_statement"]:
        dom = etree.HTML(str(income_statement_soup))
        stock.total_revenues.append(
            dom.xpath(incomestatementxpath["total_revenue"])[0].text.replace(",", ".")
        )
        stock.gross_profits.append(
            dom.xpath(incomestatementxpath["gross_profit"])[0].text.replace(",", ".")
        )
        stock.operating_incomes.append(
            dom.xpath(incomestatementxpath["operating_income"])[0].text.replace(
                ",", "."
            )
        )
        stock.net_profits.append(
            dom.xpath(incomestatementxpath["net_profit"])[0].text.replace(",", ".")
        )
    print_stock(stock)
