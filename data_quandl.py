import pandas as pd
import os
import quandl
# import time

path = "C:/Users/fdoli/github/ScikitLearn/intraQuarter/"
api_token = open(path + 'project/api_token.txt', 'r').read()
quandl.ApiConfig.api_key = api_token

# data = quandl.get_table('WIKI/PRICES',
#                         ticker='aa',
#                         qopts={'columns': ['date', 'ticker', 'adj_close']},
#                         date={'gte': '2000-12-12', 'lte': '2014-12-30'})
# print(data)


def stock_prices():
    df = pd.DataFrame()
    statspath = path + '_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    # print(stock_list)
    isdate = False
    for each_dir in stock_list[1:]:
        try:
            # print(each_dir)
            ticker = each_dir.split('\\')[1].upper()
            # print(ticker)
            data = quandl.get_table('WIKI/PRICES',
                                    ticker=ticker,
                                    qopts={'columns': ['date', 'adj_close']},
                                    date={'gte': '2000-12-12', 'lte': '2014-12-30'})
            # print(data.head())
            data[ticker] = data['adj_close']  # create a new column named after ticker, containing the stock prices

            if not isdate:  # here we concatenate the 'date' column to use it as index afterwards
                df = pd.concat([data['date']], axis=1)
                isdate = True

            df = pd.concat([df, data[ticker]], axis=1)  # concatenating stock prices columns
        except Exception as e:
            print('exception: ', str(e))

    df.set_index('date', inplace=True)
    df.to_csv(path + 'project/stock_prices.csv')


stock_prices()
