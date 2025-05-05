# NSE TIME SERIES ANALYSIS
![stock prediction](https://www.google.com/imgres?q=stock%20predictions&imgurl=https%3A%2F%2Fmiro.medium.com%2Fv2%2Fresize%3Afit%3A2000%2F1*hhq3ybwbyA3p0dWuLFtLMQ.jpeg&imgrefurl=https%3A%2F%2Fmedium.com%2Fanalytics-vidhya%2Fquick-guide-for-stock-price-prediction-d6624eb29248&docid=ge6gubWE6w9-3M&tbnid=yLz66NiG6yIA8M&vet=12ahUKEwift-zmhIuNAxWtVaQEHcOOGQkQM3oFCIMBEAA..i&w=2000&h=1050&hcb=2&ved=2ahUKEwift-zmhIuNAxWtVaQEHcOOGQkQM3oFCIMBEAA.jpg)

### Group Members
1. Brenda Mutai
2. Sharon Momanyi
3. Stephen Munyiala
4. Justin Mbugua
   
# 1. Project Overview

This project focuses on analyzing stock price movements across all publicly listed companies on the Nairobi Securities Exchange (NSE) over the years 2023 and 2024.Using daily trading data — including prices, trading volume, Sector information — the project aims to provide actionable insights into market trends, stock performance, sector dynamics, and trading patterns. The analysis aims to help investors, analysts, and researchers better understand market behavior and identify opportunities within the Kenyan stock market.# Business Understanding.

# 2. Business Understanding
Investors and financial institutions operating on the Nairobi Securities Exchange (NSE) rely on precise information to make strategic decisions regarding stock trades. By forecasting future stock prices and identifying market trends, they can optimize investment strategies, improve portfolio management, and effectively mitigate risks. Such insights empower traders to seize profitable opportunities, avoid potential losses, and enhance overall financial stability.
Additionally, predictive models enable investors to understand market behavior better, adapt to changing conditions, and maintain a competitive edge. With tools for analyzing historical trading data, stakeholders can uncover patterns, assess the impact of external factors like economic policies or global market shifts, and make data-driven choices that align with their financial goals. These advancements are essential for thriving in a dynamic stock market environment like the NSE.

# 3. Objectives
- Provide insights into which stocks might perform well based on historical trends and predictive models, which will allow for more informed decision-making.
- Offer short-term predictions of stock prices or trends to support timely buy/sell decisions, potentially improving their profitability.
- Democratize Access to NSE Analytics.

# 4. Stakeholders
1. Retail Investors - Use forecasts to make buying/selling decisions.
2. Financial analysts - Integrate model outputs into broader financial analysis workflows.
3. Portfolio Managers - Optimize asset allocation strategies.

# 5. Data Understanding
This data was sourced from [Mendely](https://data.mendeley.com/datasets/ss5pfw8xnk/2) and the key features include:

o	Date: Trading date (e.g., "03-Jan-2023").

o	Code: Stock ticker symbol (e.g., "EGAD", "KUKZ").

o	Name: Company or index name (e.g., "Eaagads Ltd", "NSE 25-Share Index").

o	12m Low/High: 12-month lowest and highest prices.

o	Day Low/High: Daily trading range.

o	Day Price: Closing price for the day.

o	Previous: Previous day's closing price (missing for some entries).

o	Change/Change%: Absolute and percentage change from the previous day.

o	Volume: Trading volume (some entries missing or zero).

o	Adjusted Price: Not populated in the sample.

o	Sector: Classification (e.g., "Agricultural").


# 6. Data Cleaning
We merged our two datasets, handled missing values and duplicates and standardized our data. This made sure that our data was good enough for further analysis.

# 7. EXPLORATORY DATA ANALYSIS(EDA)
We explored the data using univariate, bivariate and multivariate analysis just to see the relationship between different variables. We also checked for outliers and although we identified some, we chose to keep them in the dataset because in the context of stock market data, sudden spikes or drops in price or volume are normal due to market volatility, major news events or investor sentiments. Removing them could result in loss of important information.

# 8. Feature Engineering
We created new features to ensure our models perform better.

# 9. Modeling and model evaluation
We trained different models.ie, ARIMA, XGboost and LSTM. We then deployed the best performimg model.

# 10. Conclusions and Recommendations
Based off of our findings, we reccomend:
 1.	Establishing a Retraining Strategy
 2.	Integrating with Risk Management
 3.	Monitoring Model Performance Continuously
 4.	Focus on high volume stocks
 5.	Incorporating Technical Indicators for Market Timing
 6.	Leveraging Real-Time Events for Improved Forecasting
    
# 11. Next Steps
 1.	Enhancing Feature Engineering and Integration
 2.	Expanding Data Utilization and Continuous Retraining
 3.	Improving Model Evaluation and Performance Monitoring
