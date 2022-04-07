####################################################
#   Bacchetti Enrico, Lingua Marco, Shiuan-Su Wei  #
#              MAFINRISK 2021-2022                 #               
#         Numerical Methods 2nd assignment         #
#            professor. Gianluca Fusai             #
#                                                  #
#         -   Auxiliary Python code    -           #
#                                                  #
####################################################


# This code allows the user to download options data necessary to the calibration
# procedure, and to perform some numerical methods to extrapolate implied volatily
# from market quotes (see Table 5 in the report).

import pandas as pd
import numpy as np
import yfinance as yf
import datetime
from pandas import DataFrame
from numpy import log as ln
from math import exp, sqrt
from scipy.stats import norm


def callBS(S,K,T, vol, r):
    d1 = ((r + 1/2 * vol**2) * T + ln(S/K))/ (vol * sqrt(T) )
    d2 = ((r - 1/2 * vol**2) * T + ln(S/K))/ (vol * sqrt(T) )
    return S * norm.cdf(d1) - K * exp(-r*T) * norm.cdf(d2)

def putBS(S,K,T, vol, r):
    d1 = ((r + 1/2 * vol**2) * T - ln(K/S))/ (vol * sqrt(T) )
    d2 = ((r - 1/2 * vol**2) * T - ln(K/S))/ (vol * sqrt(T) )
    return K * norm.cdf(-d2) - S * exp(-r*T) * norm.cdf(-d1)
    
def c_IV_NR(S,K,T,r,cMarket,tol=0.00001):
    
    vol = 0.5
    max_iter = 200
    
    for k in range(max_iter):
        bs_price = callBS(S, K, T, vol, r)
        Fprime = K*exp(-r*T)*norm.pdf((r + 1/2 * vol**2) * T - ln(K/S))/ (vol * sqrt(T) )*sqrt(T)
        F = bs_price - cMarket

        vol_new = vol - F/Fprime
        
        new_bs_price = callBS(S, K, T, vol_new, r)
        if (abs(vol-vol_new) < tol or abs(new_bs_price-cMarket) < tol):
            break

        vol = vol_new

    implied_vol = vol_new
    return implied_vol

def p_IV_NR(S,K,T,r,pMarket,tol=0.00001):
    
    
    vol = 0.5
    max_iter = 200
    
    for k in range(max_iter):
        bs_price = putBS(S, K, T, vol, r)
        Fprime = K*exp(-r*T)*norm.pdf((r + 1/2 * vol**2) * T - ln(K/S))/ (vol * sqrt(T) )*sqrt(T)
        F = bs_price - pMarket

        vol_new = vol - F/Fprime
        
        new_bs_price = putBS(S, K, T, vol_new, r)
        if (abs(vol-vol_new) < tol or abs(new_bs_price-pMarket) < tol):
            break

        vol = vol_new

    implied_vol = vol_new
    return implied_vol

def c_IV_bisection(S,K,T,r,cMarket,a,b):

    
    tol = 0.00001;


    while (b-a > tol):
        if callBS(S,K,T,(a+b)/2, r) - cMarket > 0:
            b = (a+b)/2
        else:
            a = (a+b)/2

    return a

def p_IV_bisection(S,K,T,r,pMarket,a,b):

    
    tol = 0.00001;


    while (b-a > tol):
        if putBS(S,K,T,(a+b)/2, r) - pMarket > 0:
            b = (a+b)/2
        else:
            a = (a+b)/2

    return a

def options_chain(symbol):

    

    tk = yf.Ticker(symbol)
    # Expiration dates
    exps = tk.options

    # Get options for each expiration
    options = pd.DataFrame()
    for e in exps:
        opt = tk.option_chain(e)
        opt = pd.DataFrame().append(opt.calls).append(opt.puts)
        opt['expirationDate'] = e
        options = options.append(opt, ignore_index=True)

    # Bizarre error in yfinance that gives the wrong expiration date
    # Add 1 day to get the correct expiration date
    options['expirationDate'] = pd.to_datetime(options['expirationDate']) + datetime.timedelta(days = 1)
    options['dte'] = (options['expirationDate'] - datetime.datetime.today()).dt.days / 365
    
    # Boolean column if the option is a CALL
    options['CALL'] = options['contractSymbol'].str[4:].apply(
        lambda x: "C" in x)
    
    options[['bid', 'ask', 'strike']] = options[['bid', 'ask', 'strike']].apply(pd.to_numeric)
    options['mark'] = (options['bid'] + options['ask']) / 2 # Calculate the midpoint of the bid-ask
    
    # Drop unnecessary and meaningless columns
    options = options.drop(columns = ['expirationDate','contractSymbol','volume','bid','ask','contractSize',
                                      'currency', 'change', 'percentChange', 'lastTradeDate', 'lastPrice'])

    return options

# Get data - select a ticker

df = options_chain('TSLA') 

# data cleaning 

df = df.drop(df[df.openInterest < 400].index) #exclude too illiquid options
df = df.drop(df[df.impliedVolatility < 0.01].index) #exclude too small volatilities

#df.to_excel('data.xlsx') #release to save data

# Finding implied volatility for calls

S = 1100 #closing price 20th march
T = 0.965 #maturity
r = 0.02 # risk-free 

K_c = 2400 #call strike
price_c = 48.575 #call mkt price

a_c = 0.5 #call interval lower bound
b_c = 0.7 #call interval upper bound

c_IV_NR(S,K_c,T,r, price_c)
c_IV_bisection(S, K_c , T , r , price_c , a_c ,b_c)

# Finding implied volatility for puts

K_p = 350 #put strike
price_p = 2.08 #put mkt price

a_p = 0.1 #put interval lower bound
b_p = 1.5 #put interval upper bound, large enough to include values above 1

p_IV_NR(S,K_p,T,r, price_p)
p_IV_bisection(S, K_p , T , r , price_p , a_p ,b_p)




