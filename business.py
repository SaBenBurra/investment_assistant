from data_access.filesystem import (
    get_stock_data_from_json,
    cache_stock,
    get_stock_from_cache_if_exists,
    get_all_stock_data,
)
from data_access.web import get_page_source_with_requests, get_page_source_with_selenium
from bs4 import BeautifulSoup
from models.stock import Stock
from constants import links, xpaths
from lxml import etree
from helpers import pretty_print, reverse_date, format_number, get_dom_by_page_source
from tui import print_stock


def get_stock_data(stock_code):
    stock_code = stock_code.upper()
    if check_if_symbol_valid(stock_code) is False:
        print("Geçersiz sembol")
        return
    cache_check = get_stock_from_cache_if_exists(stock_code)
    if cache_check != False:
        cached_data = cache_check
        stock = Stock()
        for attribute, value in cached_data.items():
            setattr(stock, attribute, value)
        print_stock(stock)
        return
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
    stock.fk = format_number(dom.xpath(xpaths["f/k"])[0].text)
    stock.indfk = format_number(dom.xpath(xpaths["indf/k"])[0].text)
    stock.pddd = format_number(dom.xpath(xpaths["pd/dd"])[0].text)
    stock.indpddd = format_number(dom.xpath(xpaths["indpd/dd"])[0].text)
    stock.ebitda_margin = format_number(dom.xpath(xpaths["ebitda_margin"])[0].text)
    stock.ind_ebitda_margin = format_number(
        dom.xpath(xpaths["ind_ebitda_margin"])[0].text
    )

    for balancesheetxpath in xpaths["balance_sheet"]:
        dom = etree.HTML(str(balance_sheet_soup))
        year = dom.xpath(balancesheetxpath["year"])[0].text
        period = dom.xpath(balancesheetxpath["period"])[0].text
        if year is None or period is None:
            year = "-"
            period = "-"
        stock.dates.append(period + "/" + year)
        current_assets = format_number(
            dom.xpath(balancesheetxpath["current_assets"])[0].text
        )

        total_assets = format_number(
            dom.xpath(balancesheetxpath["total_assets"])[0].text
        )

        stock.current_assets.append(current_assets)
        stock.total_assets.append(total_assets)

        stock.fixed_assets.append(format_number(total_assets - current_assets))
        short_term_debts = format_number(
            dom.xpath(balancesheetxpath["short_term_debts"])[0].text
        )
        stock.short_term_debts.append(short_term_debts)
        total_debts = format_number(dom.xpath(balancesheetxpath["total_debts"])[0].text)
        stock.long_term_debts.append(format_number(total_debts - short_term_debts))
        stock.total_debts.append(total_debts)
        stock.total_equities.append(
            format_number(dom.xpath(balancesheetxpath["total_equities"])[0].text)
        )

    for incomestatementxpath in xpaths["income_statement"]:
        dom = etree.HTML(str(income_statement_soup))
        stock.total_revenues.append(
            format_number(dom.xpath(incomestatementxpath["total_revenue"])[0].text)
        )
        stock.gross_profits.append(
            format_number(dom.xpath(incomestatementxpath["gross_profit"])[0].text)
        )
        stock.operating_incomes.append(
            format_number(dom.xpath(incomestatementxpath["operating_income"])[0].text)
        )
        stock.net_profits.append(
            format_number(dom.xpath(incomestatementxpath["net_profit"])[0].text)
        )

    roes = []
    i = 0
    for net_profit in stock.net_profits:
        total_equity = stock.total_equities[i]
        roe = format_number(net_profit / total_equity)
        roes.append(roe)

    stock.roes = roes

    cache_stock(stock)
    print_stock(stock)


def get_stock_price(symbol):
    symbol = symbol.upper()
    json_stock_data = get_stock_data_from_json(symbol)
    url = links["base_link"] + json_stock_data["link"]
    page_source = get_page_source_with_selenium(url)
    dom = get_dom_by_page_source(page_source)
    price = dom.xpath(xpaths["price"])[0].text
    print(price, "TL")
    return price


def check_if_symbol_valid(symbol):
    all_data = get_all_stock_data()
    for data in all_data:
        if data["symbol"] == symbol.upper():
            return True

    return False
