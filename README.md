# Stock Market Prediction Using Prophet and Streamlit
This repository provides a Streamlit-based web application for stock market prediction using Facebook's Prophet model. The app allows users to forecast stock prices for a given company ticker symbol over a specified period. Additionally, it visualizes training, testing, and prediction results.

----

# Features
- Fetches historical stock data using the Yahoo Finance API.
- Implements Prophet to forecast future stock prices.
- Provides interactive visualization of training, testing, and predictions.
- Allows users to download historical data and forecast results.
- Deployed using Streamlit for an intuitive user interface.

---

# Requirements
Ensure you have the following Python dependencies installed:

```
matplotlib==3.7.1  
pandas==2.0.2  
prophet==1.1.5  
pytz==2023.3.post1  
streamlit==1.29.0  
yfinance==0.2.33
```

# Installation
1. Clone the Repository
```
git clone https://github.com/arindammajee/Stock-Market-Forecasting-App.git  
cd Stock-Market-Forecasting-App  
```
2. Install Dependencies
Make sure Python 3.x and pip are installed on your machine. Install the required packages using the requirements.txt file:
```
pip install -r requirements.txt  
```

---

# How to Run
## Run the Streamlit App
```
streamlit run ProphetModel.py
```
## Using the App
- Enter the company ticker symbol (e.g., AAPL for Apple, TCS.NS for Tata Consultancy Services).
- Specify the forecast period in days.
- Click on Forecast stock prices to view results.
- Download historical and forecasted data as CSV files from the app.

# Notebooks
This repository includes two Jupyter Notebooks for in-depth explanations of the code. You can explore the step-by-step implementation of stock data processing and prediction.

# Live Demo
The app is hosted on Streamlit. You can access it directly via the following link: [```https://stockmarketforecasting.streamlit.app/```](https://stockmarketforecasting.streamlit.app/)

# File Structure
```
Stock-Market-Forecasting-App/  
│  
├── ProphetModel.py         # Main Python script for the Streamlit app  
├── requirements.txt        # List of required dependencies  
├── companies/              # Folder where company-specific data and results are saved  
└── notebooks/              # Jupyter Notebooks for detailed implementation
```

# Author
Arindam Majee
For queries or suggestions, feel free to reach out!


