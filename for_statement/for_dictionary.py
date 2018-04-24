interest_stocks = {"Naver":10, "Samsung":5, "SK Hynix":30}

for company, stock_num in interest_stocks.items():
    print("%s: Buy %s" % (company, stock_num))


print("="*50)


for company in interest_stocks.keys():
    print("%s: Buy %s" % (company,interest_stocks[company]))