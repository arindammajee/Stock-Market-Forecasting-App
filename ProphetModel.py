#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from prophet import Prophet
import datetime
import pytz
import yfinance as yf
import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

class ProphetTicker:
    def __init__(self, ticker, past_period='3y', interval='1d'):
        self.ticker = ticker
        self.past_period = past_period
        self.interval = interval
        self.stockTicker = yf.Ticker(ticker)
        self.stockInfo = self.stockTicker.info
        self.stocks = self.stockTicker.history(period=self.past_period, interval=self.interval)
        #self.stocks['Average'] = self.stocks[['Open', 'High', 'Low', 'Close']].mean(numeric_only=True, axis=1)
        #self.df = self.stocks.drop(columns=['Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits'])
        self.df = self.stocks.copy()
        self.df ['Average']= self.stocks[['Open', 'High', 'Low', 'Close']].mean(numeric_only=True, axis=1)
        print(self.df)
        self.df['Average'] = self.df['Average'].rolling(5).mean()
        self.df = self.df.dropna()
        self.df = self.df.rename(columns={'Average': 'y'})
        self.df['ds'] = self.df.index
        self.df['ds'] = self.df['ds'].apply(lambda x: x.date())
        self.df = self.df.reset_index()
        self.train_df = self.df[:int(len(self.df)*0.97)]
        self.folder_path = f'companies/{self.ticker}'
        if os.path.exists(self.folder_path)==False:
            os.mkdir(self.folder_path)
        self.data_path = os.path.join(self.folder_path, f'{ticker}_data.csv')
        self.stocks.to_csv(self.data_path)
    
    def ModelTrain(self):
        self.model = Prophet()
        self.model.fit(self.train_df)
        return self.data_path
    
    def FutureForecast(self, future_period=120):
        self.future = self.model.make_future_dataframe(periods=60)
        self.future['day'] = self.future['ds'].dt.weekday
        self.future = self.future[self.future['day'] < 5]
        self.forecast = self.model.predict(self.future)
        self.forecast = self.forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
        self.forecast_path = f'{self.folder_path}/{self.ticker}_Forecast.csv'
        self.forecast.to_csv(self.forecast_path)

        plt.plot(self.forecast[['ds']], self.forecast[['yhat']])
        plt.fill_between(self.forecast['ds'], self.forecast['yhat_upper'], self.forecast['yhat_lower'], color='silver')
        fig1 = self.model.plot(self.forecast)
        plt.legend(["Training"])
        color = int(len(self.df)*0.03 +1)*['green']
        plt.scatter(self.df['ds'][int(len(self.df)*0.97):], self.df['y'][int(len(self.df)*0.97):], c=color, linewidths=0.2)
        plt.xlabel("Days")
        plt.ylabel("Stock Price (Average of OHLC)")
        plt.title(f"Training and Testing on {self.ticker} Stock Price with SMA")
        plt.legend(['Training Data', 'Fitted Line', 'Confidence Region', 'Test Data'], loc='upper left')

        self.image_path = f'{self.folder_path}/{self.ticker}_TrainTest_SMA.png' 
        fig1.savefig(self.image_path, dpi=480, bbox_inches='tight')

        return self.image_path, self.forecast_path





if __name__=="__main__":
   html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Stock Market Forecasting </h2>
    <h5 style="color:white;text-align:center;"> Welcome to our AI - based Stock Market Forecasting System. </h5>
    </div>
    """
   st.markdown(html_temp, unsafe_allow_html = True)
   if(True):
        company_ticker = st.text_input("Enter the company ticker here.", "TCS.NS", key="comp")
        future_period = st.text_input("How many days forecast you want? ", "60", key="future_period")
        if st.button("Forecast stock prices"):
            TickerModel = ProphetTicker(ticker=company_ticker)
            data_path = TickerModel.ModelTrain()
            image_path, forecast_path = TickerModel.FutureForecast(future_period=int(future_period))
            st.image(image_path, caption='')

            with open(forecast_path, 'rb') as f:
                st.download_button('Download The Forecast as CSV', f, file_name=forecast_path.split('/')[-1])  
            with open(data_path, 'rb') as f:
                st.download_button('Download The original stock data as CSV', f, file_name=data_path.split('/')[-1])