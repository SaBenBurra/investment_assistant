from prettytable import PrettyTable
from models.stock import Stock
from helpers import pretty_print


def print_stock(stock: Stock):
    statistics_table = PrettyTable(padding_width=3)
    ratios_table = PrettyTable(padding_width=3)

    ratios_table.field_names = ["Oran", "Hisse", "Sektör"]
    ratios_table.add_row(["F/K", str(stock.fk), str(stock.indfk)], divider=True)
    ratios_table.add_row(["PD/DD", str(stock.pddd), str(stock.indpddd)])

    statistics_table.field_names = ["Veri", *stock.dates]
    statistics_table.add_row(["Dönen varlıklar ", *stock.current_assets], divider=True)
    statistics_table.add_row(["Duran varlıklar", *stock.fixed_assets], divider=True)
    statistics_table.add_row(["Toplam varlıklar", *stock.total_assets], divider=True)
    statistics_table.add_row(
        ["Kısa vadeli yükümlülükler", *stock.short_term_debts], divider=True
    )
    statistics_table.add_row(
        ["Uzun vadeli yükümlülükler", *stock.long_term_debts], divider=True
    )
    statistics_table.add_row(["Toplam yükümlülükler", *stock.total_debts], divider=True)
    statistics_table.add_row(["Özkaynaklar", *stock.total_equities], divider=True)
    statistics_table.add_row(
        ["Satış gelirleri (Hasılat)", *stock.total_revenues], divider=True
    )
    statistics_table.add_row(["Brüt kar", *stock.gross_profits], divider=True)
    statistics_table.add_row(
        ["Faaliyet gelirleri", *stock.operating_incomes], divider=True
    )
    statistics_table.add_row(["Net karlılık", *stock.net_profits], divider=True)

    print("Sembol: " + stock.symbol)
    print(ratios_table)
    print(statistics_table)
