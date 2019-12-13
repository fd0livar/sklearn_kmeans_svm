import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
from sklearn import svm, preprocessing
from matplotlib import style

style.use('ggplot')

path = "C:/Users/fdoli/github/ScikitLearn/intraQuarter/project/"

FEATURES = ['DE Ratio',
            'Trailing P/E',
            'Price/Sales',
            'Price/Book',
            'Profit Margin',
            'Operating Margin',
            'Return on Assets',
            'Return on Equity',
            'Revenue Per Share',
            'Market Cap',
            'Enterprise Value',
            'Forward P/E',
            'PEG Ratio',
            'Enterprise Value/Revenue',
            'Enterprise Value/EBITDA',
            'Revenue',
            'Gross Profit',
            'EBITDA',
            'Net Income Avl to Common ',
            'Diluted EPS',
            'Earnings Growth',
            'Revenue Growth',
            'Total Cash',
            'Total Cash Per Share',
            'Total Debt',
            'Current Ratio',
            'Book Value Per Share',
            'Cash Flow',
            'Beta',
            'Held by Insiders',
            'Held by Institutions',
            'Shares Short (as of',
            'Short Ratio',
            'Short % of Float',
            'Shares Short (prior ']


def build_data_set():
    data_df = pd.read_csv(path + 'key_stats_acc_perf_WITH_NA.csv')
    # data_df = data_df[:100]
    data_df = data_df.reindex(np.random.permutation(data_df.index))
    # data_df = data_df.replace("NaN", 0).replace("N/A", 0)
    data_df = data_df.fillna(0).replace("N/A", 0)  # this line works instead of replace NaN
    X = np.array(data_df[FEATURES].values)

    y = (data_df['Status']
         .replace('underperform', 0)
         .replace('outperform', 1)
         .values.tolist())

    X = preprocessing.scale(X)

    return X, y


def analysis():
    test_size = 1000
    X, y = build_data_set()
    print(len(X))

    clf = svm.SVC(kernel='linear', C=1.0)
    clf.fit(X[:-test_size], y[:-test_size])

    correct_count = 0

    for xx in range(1, test_size + 1):
        if clf.predict(X[-xx].reshape(1, -1))[0] == y[-xx]:
            correct_count += 1

    print('Accuracy: ', (correct_count / test_size) * 100.00)


analysis()
