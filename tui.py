from prettytable import PrettyTable, ORGMODE
from models.stock import Stock
from helpers import pretty_print, format_number
from constants import links


def print_stock(stock: Stock):
    statistics_table = PrettyTable(padding_width=3)
    statistics_table.set_style(ORGMODE)
    statistics_table.header = False
    ratios_table = PrettyTable(padding_width=3)
    ratios_table.field_names = ["Oran", "Hisse", "Sektör"]
    ratios_table.add_row(
        [
            "F/K",
            format_number(stock.fk, as_float_str=True),
            format_number(str(stock.indfk), as_float_str=True),
        ],
        divider=True,
    )
    ratios_table.add_row(
        [
            "PD/DD",
            format_number(str(stock.pddd), as_float_str=True),
            format_number(str(stock.indpddd), as_float_str=True),
        ],
        divider=True,
    )
    ratios_table.add_row(
        [
            "Favök marjı (Faaliyet Karlılığı)",
            format_number(str(stock.ebitda_margin), as_float_str=True),
            format_number(str(stock.ind_ebitda_margin), as_float_str=True),
        ],
        divider=True,
    )
    ratios_table.add_row(
        ["ROE", format_number(str(stock.roes[0]), as_float_str=True), "-"]
    )

    statistics_table.add_row(["", *stock.dates], divider=True)
    statistics_table.add_row(
        [
            "Dönen varlıklar ",
            *[
                format_number(element, as_float_str=True)
                for element in stock.current_assets
            ],
        ],
        divider=True,
    )
    statistics_table.add_row(
        [
            "Duran varlıklar",
            *[
                format_number(element, as_float_str=True)
                for element in stock.fixed_assets
            ],
        ],
        divider=True,
    )
    statistics_table.add_row(
        [
            "Toplam varlıklar",
            *[
                format_number(element, as_float_str=True)
                for element in stock.total_assets
            ],
        ],
        divider=True,
    )
    statistics_table.add_row(
        [
            "Kısa vadeli yükümlülükler",
            *[
                format_number(element, as_float_str=True)
                for element in stock.short_term_debts
            ],
        ],
        divider=True,
    )
    statistics_table.add_row(
        [
            "Uzun vadeli yükümlülükler",
            *[
                format_number(element, as_float_str=True)
                for element in stock.long_term_debts
            ],
        ],
        divider=True,
    )
    statistics_table.add_row(
        [
            "Toplam yükümlülükler",
            *[
                format_number(element, as_float_str=True)
                for element in stock.total_debts
            ],
        ],
        divider=True,
    )
    statistics_table.add_row(
        [
            "Özkaynaklar",
            *[
                format_number(element, as_float_str=True)
                for element in stock.total_equities
            ],
        ],
        divider=True,
    )
    statistics_table.add_row(
        [
            "Satış gelirleri (Hasılat)",
            *[
                format_number(element, as_float_str=True)
                for element in stock.total_revenues
            ],
        ],
        divider=True,
    )
    statistics_table.add_row(
        [
            "Brüt kar",
            *[
                format_number(element, as_float_str=True)
                for element in stock.gross_profits
            ],
        ],
        divider=True,
    )
    statistics_table.add_row(
        [
            "Faaliyet gelirleri",
            *[
                format_number(element, as_float_str=True)
                for element in stock.operating_incomes
            ],
        ],
        divider=True,
    )
    statistics_table.add_row(
        [
            "Net karlılık",
            *[
                format_number(element, as_float_str=True)
                for element in stock.net_profits
            ],
        ],
        divider=True,
    )
    statistics_table.add_row(
        [
            "Roe değeri",
            *[format_number(element, as_float_str=True) for element in stock.roes],
        ],
        divider=True,
    )

    print("Sembol: " + stock.symbol)
    print(ratios_table)
    print("\n")
    print(statistics_table)
    print("\nGrafik linki: " + links["stock_chart"].format(stock.pair_id))
