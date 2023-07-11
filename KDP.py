# fetch data from file/files
import pandas as pd
import numpy as np

df1 = pd.read_csv(r"C:\Users\kirui\Downloads\KDP_annual_financials.csv")
df2 = pd.read_csv(r"C:\Users\kirui\Downloads\KDP_annual_cash-flow.csv")

# clean data
df1 = df1.dropna()
df2 = df2.dropna()

# drop ttm column from df1 i.e column 1
df1.drop(df1.columns[1], axis=1, inplace=True)
df2.drop(df2.columns[1], axis=1, inplace=True)

TotalRevenue = df1.iloc[0]
CostOfRevenue = df1.iloc[2]
OperatingIncome = df1.iloc[7]
FreeCashFlow = df2.iloc[-1]

# DROP INDEX 0
TotalRevenue = TotalRevenue[1:]
CostOfRevenue = CostOfRevenue[1:]
OperatingIncome = OperatingIncome[1:]
FreeCashFlow = FreeCashFlow[1:]

# convert index to datetime
TotalRevenue.index = pd.to_datetime(TotalRevenue.index)
CostOfRevenue.index = pd.to_datetime(CostOfRevenue.index)
OperatingIncome.index = pd.to_datetime(OperatingIncome.index)
FreeCashFlow.index = pd.to_datetime(FreeCashFlow.index)

# remove commas from TotalRevenue and gross profit
TotalRevenue = TotalRevenue.str.replace(',', '')
CostOfRevenue = CostOfRevenue.str.replace(',', '')
OperatingIncome = OperatingIncome.str.replace(',', '')
FreeCashFlow = FreeCashFlow.str.replace(',', '')

# make date time as a year only
TotalRevenue.index = TotalRevenue.index.year
CostOfRevenue.index = CostOfRevenue.index.year
OperatingIncome.index = OperatingIncome.index.year
FreeCashFlow.index = FreeCashFlow.index.year

# Store the values in a list as arrays
TotalRevenue = TotalRevenue.values
CostOfRevenue = CostOfRevenue.values
OperatingIncome = OperatingIncome.values
FreeCashFlow = FreeCashFlow.values

# convert the values to numeric
TotalRevenue = pd.to_numeric(TotalRevenue)
CostOfRevenue = pd.to_numeric(CostOfRevenue)
OperatingIncome = pd.to_numeric(OperatingIncome)
FreeCashFlow = pd.to_numeric(FreeCashFlow)

# iterrate through the gross profit and store each value in a list
GrossProfitList = []
for i in range(len(TotalRevenue)):
    for j in range(len(CostOfRevenue)):
        if i == j:
            GrossProfit = TotalRevenue[i] - CostOfRevenue[j]
            GrossProfitList.append(GrossProfit)

# convert the list to a dataframe
GrossProfitList = pd.DataFrame(GrossProfitList)

# add the total revenue and gross profit to a dataframe
df = pd.DataFrame({'TotalRevenue': TotalRevenue,
                  'CostOfRevenue': CostOfRevenue, 'GrossProfit': GrossProfitList[0], 'OperatingIncome': OperatingIncome,
                  'FreeCashFlow': FreeCashFlow})
print(df)

# append year to the dataframe by iterratting through the index
year = []
# year starts from 2022 to 2004
for i in range(2022, 2003, -1):
    year.append(i)


# add the year to the dataframe at the beginning
df.insert(0, 'Year', year)

# download the dataframe to a csv file
df.to_csv(r"Clean_CSV.csv")


# filter data for past 5 years for TotalRevenue, GrossProfit and OperatingIncome
TotalRevenue = TotalRevenue[0:5]
GrossProfit = GrossProfitList[0][0:5]
OperatingIncome = OperatingIncome[0:5]

# print in a dataframe with year
df = pd.DataFrame({'Year': year[0:5], 'TotalRevenue': TotalRevenue,
                    'GrossProfit': GrossProfit, 'OperatingIncome': OperatingIncome})
print(df)