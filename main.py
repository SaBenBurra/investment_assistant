import sys
from business import get_stock_data, get_stock_price

first = True
while True:
    print(
        """
1- Fiyat Sorgulama
2- Analiz Verisi Görüntüleme
    
          """
    )
    process_number = input("Lütfen işlem seçiniz: ")
    if process_number == "1":
        symbol = input("Hisse sembolü giriniz: ")
        print("\n\n")
        get_stock_price(symbol)
    elif process_number == "2":
        symbol = input("Hisse sembolü giriniz: ")
        print("\n\n")
        get_stock_data(symbol)

    input()
