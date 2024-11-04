import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import datetime as dt
import pandas_datareader as web
import requests
import yfinance as yf
from sklearn.linear_model import LinearRegression
"""
start = dt.datetime(2022,1,1)
end = dt.datetime(2024,11,1)
data = yf.download('2330.TW',start=start,end=end)

#MA 移動均線算法
data['SMA_20'] = data['Close'].rolling(window=20).mean()

# plt.plot(data['SMA_20'])
# plt.plot(data['Close'])

# plt.show()
#EMA 指數移動平均
data['EMA_20'] = data['Close'].ewm(span=20,adjust=False).mean()
"""
'''
ewm()創建指數加權對象
span=20 指定EMA 窗口大小為20 ( 意思就是計算最近20個數據)
adjust=False ，EMA 計算不會進行初始調整，這使得 EMA 對最近的價格變動反應更快

'''
# plt.plot(data['EMA_20'])
# plt.plot(data['Close'])

# plt.show()
"""
#RSI
#1. 計算價格變動
delta = data['Close'].diff()
#2計算漲跌幅
gain= (delta.where(delta >0,0)).ewm(span=14,adjust=False).mean()
loss= (-delta.where(delta <0,0)).ewm(span=14,adjust=False).mean()

#3計算RS and RSI
rs = gain/loss
data['RSI'] = 100-(100/(1+rs))

fig,axs = plt.subplots(2,1,gridspec_kw={'height_ratios':[3,1]},figsize=(10,6))

axs[0].plot(data['Close'],label='Close Price')
axs[0].plot(data['SMA_20'],label='SMA',color='brown')
axs[0].set_title('Close Price with MA')
axs[0].legend()
axs[1].axhline(y=70,color='r',linestyle='--',label='Overbought (70)')
axs[1].axhline(y=30,color='g',linestyle='--',label='Overbought (30)')
axs[1].plot(data['RSI'],color='orange',label='RSI')
axs[1].set_title('RSI')
axs[1].legend()

#自動調整間距
plt.tight_layout
#顯示
plt.show()
"""
"""
#線性回歸

#將索引轉換為日期格式
data['Date'] = pd.to_datetime(data.index)
#將日期轉換為從最早日期起的天數
data['Date'] = (data['Date']-data['Date'].min()).dt.days

X = data[['Date']] # 自變量
y = data['Close']  # 目標變量

#線性回歸模型
model = LinearRegression()
model.fit(X,y)

#進行預測
data['LineAGG'] = model.predict(X)

#繪圖
plt.figure(figsize=(12,6))
plt.plot(data['Close'],label='Close Price',color='Blue')
plt.plot(data['LineAGG'],label='Linear Regression',color='orange')
plt.title('Colse Price and Linear Regression Line')
plt.legend()
plt.show()



"""

# 讀取歷史數據
start = dt.datetime(2022, 1, 1)
end = dt.datetime(2024, 11, 1)
data = yf.download('2330.TW', start=start, end=end)

# 將索引轉換為日期格式
data['Date'] = pd.to_datetime(data.index)
# 將日期轉換為從最早日期起的天數
data['Days'] = (data['Date'] - data['Date'].min()).dt.days

X = data[['Days']]  # 自變量
y = data['Close']  # 目標變量

# 線性回歸模型
model = LinearRegression()
model.fit(X, y)

# 繪圖
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Close'], label='Historical Close Price', color='Blue')

# 使用 model 預測的值
plt.plot(data['Date'], model.predict(X), label='Linear Regression', color='orange')

# 進行預測
# 未來30天
future_days = 30

# 獲取最後一個日期的天數
last_day = data['Date'].max()
# 使用模型進行預測
future_x = np.arange(data['Days'].max() + 1, data['Days'].max() + future_days + 1).reshape(-1, 1)
predicted_price = model.predict(future_x)

# 將預測結果轉換為日期格式，從最後一天開始
future_dates = [last_day + pd.Timedelta(days=i) for i in range(1, future_days + 1)]

# 顯示預測價格
plt.plot(future_dates, predicted_price, label='Future Prediction', color='red', linestyle='--')

# 設定
plt.xlim(pd.Timestamp('2022-01-01'), future_dates[-1])
plt.xlabel('Date')
plt.ylabel('Close Price')

plt.title('Close Price and Linear Regression Line with Prediction')

plt.legend()
plt.show()
