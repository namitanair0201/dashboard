import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
# #import fbprophet

time = [ 0.000064852, 0.000125767, 0.000108508, 0.000095767, 0.000078508, 0.000095767, 0.000078508,
        0.000095767, 0.000078508, 0.000175428, 0.000019328, 0.000019328, 0.000022828, 0.000019328, 0.000019328,
        0.000019328, 0.000110511, 0.00004966, 0.000110575, 0.000108316, 0.000080575, 0.000078316, 0.000080575,
        0.000078316, 0.000080575, 0.000078316, 0.000096052, 0.000049596, 0.000125511, 0.000095511, 0.000108252,
        0.000050572, 0.000095511, 0.000078252, 0.000095511, 0.000060711, 0.00002671, 0.00002671, 0.000065511,
        0.000078252, 0.000095511, 0.000078252, 0.000160172, 0.00004998, 0.000110895, 0.000108636, 0.000080895,
        0.000078636, 0.000080895, 0.000095895, 0.000078636, 0.000078636, 0.000115556, 0.000019328, 0.000019328,
        0.000049468, 0.000110383, 0.000080383, 0.000026582, 0.000049724
    ]

time.sort()
print('[', end = '')
for number in time:
    print('{0:.9f}'.format(number),', ', end = '')
print(']')
# # #m = fbprophet.Prophet()

# # headers = ['ds', 'y']
# df = pd.read_csv('transactions.csv')

# #print(df['UnixTimestamp'].tail(10))

# df['ds'] = df['UnixTimestamp'].map(lambda x: datetime.strptime(str(x), '%m/%d/%Y %H:%M:%S %p'))
# print(df.index())
# x= df['ds']
# x.to_csv("hell.csv")
# # x = df['ds']
# # y = df['y']

# # # pl
# # plt.plot(x,y)
# # # beautify the x-labels
# # #plt.gcf().autofmt_xdate()

# # plt.show()

# # #m.fit(df)

# # #future = m.make_future_dataframe(periods=3)
# # #forecast = m.predict(future)
# # #m.plot(forecast)
# # #m.show()
# # ##print("hello")
# # #df["DateTime"] = pd.to_datetime(df["DateTime"])
# # ##print(df.dtypes)
# # #
# # #df['ds'] = df['DateTime']
# # #df['y'] = df['TxnFee']
# # #df.set_index('DateTime')
# # #plt.xlabel('DateTime')
# # #plt.ylabel('TxnFee')
# # #plt.plot(df)
# # #plt.show()

# # #3/5/2019 9:31:33 AM,0.000125319