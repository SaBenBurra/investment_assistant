links = {
    "base_link": "https://www.investing.com",
    "income_statement_table": "https://www.investing.com/instruments/Financials/changereporttypeajax?action=change_report_type&pair_ID={}&report_type=INC&period_type=Annual",
    "balance_sheet_table": "https://tr.investing.com/instruments/Financials/changereporttypeajax?action=change_report_type&pair_ID={}&report_type=BAL&period_type=Annual",
}
xpaths = {
    "f/k": '//*[@id="childTr"]/td/div/table/tbody/tr[1]/td[2]',
    "ind/k": "/html/body/div[6]/section/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[3]",
    "balance_sheet": [
        {
            "year": "/html/body/table/tbody[1]/tr/th[2]/span",
            "period": "/html/body/table/tbody[1]/tr/th[2]/div",
            "current_assets": "/html/body/table/tbody[2]/tr[1]/td[2]",
            "fixed_assets": "/html/body/table/tbody[2]/tr[3]/td[2]",
            "short_term_debts": "/html/body/table/tbody[2]/tr[5]/td[2]",
            "total_debts": "/html/body/table/tbody[2]/tr[7]/td[2]",
            "total_equities": "/html/body/table/tbody[2]/tr[9]/td[2]",
        },
        {
            "year": "/html/body/table/tbody[1]/tr/th[3]/span",
            "period": "/html/body/table/tbody[1]/tr/th[3]/div",
            "current_assets": "/html/body/table/tbody[2]/tr[1]/td[3]",
            "fixed_assets": "/html/body/table/tbody[2]/tr[3]/td[3]",
            "short_term_debts": "/html/body/table/tbody[2]/tr[5]/td[3]",
            "total_debts": "/html/body/table/tbody[2]/tr[7]/td[3]",
            "total_equities": "/html/body/table/tbody[2]/tr[9]/td[3]",
        },
        {
            "year": "/html/body/table/tbody[1]/tr/th[4]/span",
            "period": "/html/body/table/tbody[1]/tr/th[4]/div",
            "current_assets": "/html/body/table/tbody[2]/tr[1]/td[4]",
            "fixed_assets": "/html/body/table/tbody[2]/tr[3]/td[4]",
            "short_term_debts": "/html/body/table/tbody[2]/tr[5]/td[4]",
            "total_debts": "/html/body/table/tbody[2]/tr[7]/td[4]",
            "total_equities": "/html/body/table/tbody[2]/tr[9]/td[4]",
        },
        {
            "year": "/html/body/table/tbody[1]/tr/th[5]/span",
            "period": "/html/body/table/tbody[1]/tr/th[5]/div",
            "current_assets": "/html/body/table/tbody[2]/tr[1]/td[5]",
            "fixed_assets": "/html/body/table/tbody[2]/tr[3]/td[5]",
            "short_term_debts": "/html/body/table/tbody[2]/tr[5]/td[5]",
            "total_debts": "/html/body/table/tbody[2]/tr[7]/td[5]",
            "total_equities": "/html/body/table/tbody[2]/tr[9]/td[5]",
        },
    ],
    "income_statement": [
        {
            "total_revenue": "/html/body/table/tbody[2]/tr[1]/td[2]",
            "gross_profit": "/html/body/table/tbody[2]/tr[4]/td[2]",
            "operating_income": "/html/body/table/tbody[2]/tr[7]/td[2]",
            "net_profit": "/html/body/table/tbody[2]/tr[19]/td[2]",
        },
        {
            "total_revenue": "/html/body/table/tbody[2]/tr[1]/td[3]",
            "gross_profit": "/html/body/table/tbody[2]/tr[4]/td[3]",
            "operating_income": "/html/body/table/tbody[2]/tr[7]/td[3]",
            "net_profit": "/html/body/table/tbody[2]/tr[19]/td[3]",
        },
        {
            "total_revenue": "/html/body/table/tbody[2]/tr[1]/td[4]",
            "gross_profit": "/html/body/table/tbody[2]/tr[4]/td[4]",
            "operating_income": "/html/body/table/tbody[2]/tr[7]/td[4]",
            "net_profit": "/html/body/table/tbody[2]/tr[19]/td[4]",
        },
        {
            "total_revenue": "/html/body/table/tbody[2]/tr[1]/td[5]",
            "gross_profit": "/html/body/table/tbody[2]/tr[4]/td[5]",
            "operating_income": "/html/body/table/tbody[2]/tr[7]/td[5]",
            "net_profit": "/html/body/table/tbody[2]/tr[19]/td[5]",
        },
    ],
}
