import sys
from business import get_stock_data

if len(sys.argv) > 1:
    stock_symbol = sys.argv[1]
else:
    stock_symbol = input("Sembol girin: ")
get_stock_data(stock_symbol.upper())
