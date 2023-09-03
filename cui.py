from prettytable import PrettyTable
from models.stock import Stock
from helpers import pretty_print


def print_stock(stock: Stock):
    table = PrettyTable(padding_width=3)

    print("Sembol: " + stock.symbol)
    print("F/K Oranı:" + str(stock.fk))
    table.field_names = ["Veri", *stock.dates]
    table.add_row(["Dönen varlıklar ", *stock.current_assets], divider=True)
    table.add_row(["Duran varlıklar", *stock.fixed_assets], divider=True)
    table.add_row(["Kısa vadeli yükümlülükler", *stock.short_term_debts], divider=True)
    table.add_row(["Uzun vadeli yükümlülükler", *stock.long_term_debts], divider=True)
    table.add_row(["Toplam yükümlülükler", *stock.total_debts], divider=True)
    table.add_row(["Özkaynaklar", *stock.total_equities], divider=True)
    table.add_row(["Satış gelirleri (Hasılat)", *stock.total_revenues], divider=True)
    table.add_row(["Brüt kar", *stock.gross_profits], divider=True)
    table.add_row(["Faaliyet gelirleri", *stock.operating_incomes], divider=True)
    table.add_row(["Net karlılık", *stock.net_profits], divider=True)

    print(table)
