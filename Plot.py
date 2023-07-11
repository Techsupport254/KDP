from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import yfinance as yf

import yfinance as yf

# stock_info.keys() for other properties you can explore
stock_info = yf.Ticker('KDP').info
market_price = stock_info['regularMarketPrice']


df1 = pd.read_csv(r"PredictedValues.csv")
df2 = pd.read_csv(r"Clean_CSV.csv")

df1.rename(columns={'Unnamed: 0': 'Year'}, inplace=True)
df2.drop(df2.columns[0], axis=1, inplace=True)

# combine the two dataframes into one such that df1 is the first starting from 2032 to 2023 and df2 is the second starting from 2022 to 2004
df3 = pd.concat([df1, df2], axis=0, ignore_index=True)
df3 = df3.sort_values(by=['Year'], ascending=False)
df3 = df3.reset_index(drop=True)
print(df3)

# download the csv file
df3.to_csv(r"CombinedValues.csv")


# plot size
plt.figure(figsize=(20, 8))

plt.plot(df3['Year'], df3['TotalRevenue'], label='TotalRevenue')
plt.plot(df3['Year'], df3['CostOfRevenue'], label='CostOfRevenue')
plt.plot(df3['Year'], df3['GrossProfit'], label='GrossProfit')
plt.plot(df3['Year'], df3['FreeCashFlow'], label='FreeCashFlow')
plt.plot(df3['Year'], df3['OperatingIncome'], label='OperatingIncome')

plt.legend()

textbox = 'Firm Title: KDP (Keurig Dr Pepper Inc)\nValuation Date: 01-Apr-23\nLatest FYE: 31-Dec-22\nWACC: 6.75%\nKDP DCF Value: https://www.alphaspread.com/security/nasdaq/kdp/dcf-valuation/base-case#dcf-value-calculation\nCurrent Stock Price: ${:.2f}'.format(
    market_price)
plt.text(0.5, 0.95, textbox, transform=plt.gca().transAxes, fontsize=6,
         verticalalignment='top', horizontalalignment='center', bbox=dict(facecolor='white', alpha=0.8))

plt.xlabel('Year')
plt.ylabel('Billion USD')

plt.title('KDP (Keurig Dr Pepper Inc) Valuation')

plt.xticks(df3['Year'])
plt.xticks(rotation=45)

plt.grid(True)

plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(
    lambda x, loc: "{:,}".format(int(x/1000000000)) + 'B'))

plt.show()
