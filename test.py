import requests

print(
    requests.get(
        "https://www.investing.com/instruments/Financials/changereporttypeajax?action=change_report_type&pair_ID=19557&report_type=INC&period_type=Annual"
    ).text
)
